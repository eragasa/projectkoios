from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from dev.rag_mvp.rag import (
    IngestedDocument,
    Passage,
    RagMvpError,
    answer,
    audit_citations,
    citation_proposal,
    database_counts,
    discover_pdfs,
    display_page_label,
    extract_pdf,
    index_documents,
    load_bibtex_keys,
    load_citation_claims,
    search,
)

pymupdf: Any = pytest.importorskip("pymupdf")


def _write_pdf(path: Path) -> None:
    document = pymupdf.open()
    first = document.new_page(width=420, height=420)
    first.insert_textbox(
        (30, 60, 390, 300),
        "Effective mass follows from the curvature of an electronic band. "
        "Wannier interpolation evaluates derivatives on dense meshes.",
        fontsize=11,
    )
    first.insert_text((205, 400), "1", fontsize=9)
    second = document.new_page(width=420, height=420)
    second.insert_textbox(
        (30, 60, 390, 300),
        "A separate control topic discusses Bayesian calibration.",
        fontsize=11,
    )
    second.insert_text((205, 400), "2", fontsize=9)
    document.save(path)
    document.close()


def _document(
    locator: Path,
    text: str,
    *,
    corpus_role: str = "reference",
    citation_key: str = "example2024",
) -> IngestedDocument:
    source_sha256 = hashlib.sha256(str(locator).encode()).hexdigest()
    source_id = f"rag:sha256:{source_sha256}"
    passage = Passage(
        passage_id=f"rag-passage:sha256:{source_sha256}",
        source_id=source_id,
        source_sha256=source_sha256,
        locator=str(locator),
        page_index=2,
        printed_page_label="3",
        word_start=0,
        word_end=len(text.split()),
        block_ids=("block:example",),
        text=text,
    )
    return IngestedDocument(
        source_id=source_id,
        source_sha256=source_sha256,
        locator=str(locator),
        citation_key=citation_key,
        bibtex_entry_present=True,
        corpus_role=corpus_role,
        byte_length=100,
        page_count=3,
        extractor_name="test-extractor",
        extractor_version="1",
        warnings=(),
        passages=(passage,),
    )


def test__extract_pdf__creates_page_bounded_source_linked_passages(
    tmp_path: Path,
) -> None:
    pdf = tmp_path / "article.pdf"
    _write_pdf(pdf)

    result = extract_pdf(pdf, chunk_words=20, overlap_words=5)

    assert result.page_count == 2
    assert result.passages
    assert {item.page_index for item in result.passages} == {0, 1}
    assert all(item.block_ids for item in result.passages)
    assert all(
        item.source_sha256 == result.source_sha256 for item in result.passages
    )
    assert "effective mass" in " ".join(
        item.text.casefold() for item in result.passages
    )


def test__search__returns_ranked_page_linked_bm25_evidence(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    document = _document(
        tmp_path / "article.pdf",
        "Effective mass is obtained from electronic band curvature.",
    )
    index_documents(database, (document,))

    hits = search(database, "effective mass band curvature")

    assert len(hits) == 1
    assert hits[0].rank == 1
    assert hits[0].passage.page_index == 2
    assert hits[0].passage.printed_page_label == "3"
    assert hits[0].passage.block_ids == ("block:example",)
    assert database_counts(database) == (1, 1)
    assert database.stat().st_mode & 0o777 == 0o600


def test__answer__requires_valid_local_evidence_citations(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "article.pdf",
                "Effective mass is obtained from electronic band curvature.",
            ),
        ),
    )

    valid = answer(
        database,
        "How is effective mass obtained?",
        generate=lambda model, system, prompt: (
            "It follows from band curvature [S1]."
        ),
    )
    invalid = answer(
        database,
        "How is effective mass obtained?",
        generate=lambda model, system, prompt: "It follows from curvature.",
    )

    assert valid.text == "It follows from band curvature [S1]."
    assert valid.citations == (1,)
    assert invalid.text == "INSUFFICIENT_EVIDENCE"
    assert invalid.citations == ()


def test__citation_proposal__searches_only_references_and_validates_labels(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "reference.pdf",
                "Parallel transport produces a smooth Bloch gauge.",
                citation_key="reference2024",
            ),
            _document(
                tmp_path / "manuscript.pdf",
                "Parallel transport produces a smooth Bloch gauge.",
                corpus_role="manuscript",
                citation_key="self",
            ),
        ),
    )
    response = json.dumps(
        {
            "assessments": [
                {
                    "source": 1,
                    "status": "DIRECT_SUPPORT",
                    "rationale": "The passage states the claim directly.",
                }
            ]
        }
    )

    proposal = citation_proposal(
        database,
        "parallel transport smooth Bloch gauge",
        classify=True,
        generate=lambda model, system, prompt: response,
    )

    assert proposal.assessment == "AUTOMATED_UNREVIEWED"
    assert len(proposal.candidates) == 1
    assert proposal.candidates[0].citation_key == "reference2024"
    assert proposal.candidates[0].support_status == "DIRECT_SUPPORT"


def test__load_bibtex_keys__preserves_exact_keys(tmp_path: Path) -> None:
    bibliography = tmp_path / "references.bib"
    bibliography.write_text(
        "@article{Example2024,\n  title = {Example}\n}\n",
        encoding="utf-8",
    )

    assert load_bibtex_keys(bibliography) == {"example2024": "Example2024"}


def test__audit_citations__reports_hits_and_corpus_gaps(tmp_path: Path) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "reference.pdf",
                "Parallel transport produces a smooth Bloch gauge.",
                citation_key="reference2024",
            ),
        ),
    )
    claims_path = tmp_path / "claims.jsonl"
    manuscript_sha256 = "a" * 64
    claims_path.write_text(
        "\n".join(
            (
                json.dumps(
                    {
                        "claim_id": "claim-1",
                        "manuscript_sha256": manuscript_sha256,
                        "lines": "1-2",
                        "claim": "Parallel transport produces a smooth gauge.",
                        "query": "parallel transport smooth Bloch gauge",
                        "expected_keys": ["reference2024"],
                        "expected_outcome": "candidate_source",
                    }
                ),
                json.dumps(
                    {
                        "claim_id": "claim-2",
                        "manuscript_sha256": manuscript_sha256,
                        "lines": "3-4",
                        "claim": "A missing source makes a second claim.",
                        "query": "parallel transport",
                        "expected_keys": ["missing2024"],
                        "expected_outcome": "corpus_gap_possible",
                    }
                ),
            )
        ),
        encoding="utf-8",
    )

    audit = audit_citations(database, load_citation_claims(claims_path))

    assert audit.evaluated_claims == 1
    assert audit.corpus_gap_claims == 1
    assert audit.hit_at_1 == 1.0
    assert audit.hit_at_k == 1.0
    assert audit.mean_reciprocal_rank == 1.0


def test__display_page_label__decodes_utf16_without_changing_storage() -> None:
    assert display_page_label("<FEFF00310035>") == "15"
    assert display_page_label("xiv") == "xiv"
    assert display_page_label(None) == "none"


def test__discover_pdfs__rejects_symlinked_input(tmp_path: Path) -> None:
    source = tmp_path / "source.pdf"
    source.write_bytes(b"%PDF-1.7\n")
    symlink = tmp_path / "linked.pdf"
    symlink.symlink_to(source)

    with pytest.raises(RagMvpError, match="symlinked input"):
        discover_pdfs((symlink,))
