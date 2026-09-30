from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from dev.rag_mvp.literature_review import (
    LiteratureClaim,
    RagMvpError,
    assess_with_generator,
    build_claim_evidence_bundle,
    load_literature_claims,
    render_literature_review,
)
from dev.rag_mvp.rag import IngestedDocument, Passage, index_documents


def _document(
    locator: Path,
    text: str,
    *,
    citation_key: str,
    corpus_role: str = "reference",
) -> IngestedDocument:
    source_sha256 = hashlib.sha256(str(locator).encode()).hexdigest()
    source_id = f"rag:sha256:{source_sha256}"
    return IngestedDocument(
        source_id=source_id,
        source_sha256=source_sha256,
        locator=str(locator),
        citation_key=citation_key,
        bibtex_entry_present=True,
        corpus_role=corpus_role,
        byte_length=100,
        page_count=4,
        extractor_name="test",
        extractor_version="1",
        warnings=(),
        passages=(
            Passage(
                passage_id=f"rag-passage:sha256:{source_sha256}",
                source_id=source_id,
                source_sha256=source_sha256,
                locator=str(locator),
                page_index=2,
                printed_page_label="3",
                word_start=0,
                word_end=len(text.split()),
                block_ids=("block:test",),
                text=text,
            ),
        ),
    )


def test__load_literature_claims__rejects_duplicate_json_members(
    tmp_path: Path,
) -> None:
    claims = tmp_path / "claims.jsonl"
    claims.write_text(
        '{"claim_id":"C1","claim_id":"C2","section":"s",'
        '"claim":"text","queries":["query"]}\n',
        encoding="utf-8",
    )

    with pytest.raises(RagMvpError, match="duplicate member"):
        load_literature_claims(claims)


def test__build_claim_evidence_bundle__uses_reference_sources_only(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "one.pdf",
                "A metal has a Fermi surface and fractional occupations.",
                citation_key="one",
            ),
            _document(
                tmp_path / "two.pdf",
                "Metallic integration near a Fermi surface needs care.",
                citation_key="two",
            ),
            _document(
                tmp_path / "self.pdf",
                "A metal has a Fermi surface.",
                citation_key="self",
                corpus_role="manuscript",
            ),
        ),
    )
    claim = LiteratureClaim(
        claim_id="C1",
        section="spectral",
        claim="Metals have a Fermi surface.",
        queries=("metal Fermi surface", "fractional occupations metal"),
    )

    bundle = build_claim_evidence_bundle(database, claim, total_limit=4)

    assert {item.citation_key for item in bundle.evidence} == {"one", "two"}
    assert tuple(item.label for item in bundle.evidence) == ("E1", "E2")
    assert all(item.physical_page == 3 for item in bundle.evidence)


def test__assess_with_generator__enforces_citation_and_correction_contract(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "one.pdf",
                "Finite temperature gives fractional Fermi occupations.",
                citation_key="one",
            ),
        ),
    )
    claim = LiteratureClaim(
        claim_id="C1",
        section="thermal",
        claim="Every smearing is physical temperature.",
        queries=("finite temperature Fermi occupations",),
    )
    bundle = build_claim_evidence_bundle(database, claim)
    response = json.dumps(
        {
            "status": "QUALIFIED",
            "summary": "The evidence addresses Fermi temperature only.",
            "corrected_claim": (
                "Fermi-Dirac occupations represent an electronic temperature."
            ),
            "assumptions": ["Fermi-Dirac statistics"],
            "citations": ["E1"],
            "source_requests": ["Acquire numerical-smearing method papers."],
        }
    )

    assessment = assess_with_generator(
        bundle,
        lambda model, system, prompt: response,
    )

    assert assessment.status == "QUALIFIED"
    assert assessment.citations == ("E1",)
    assert assessment.assessment_status == "AUTOMATED_UNREVIEWED"


def test__render_literature_review__preserves_review_status_and_evidence(
    tmp_path: Path,
) -> None:
    database = tmp_path / "rag.sqlite3"
    index_documents(
        database,
        (
            _document(
                tmp_path / "one.pdf",
                "An insulator has a filled band separated by a gap.",
                citation_key="one",
            ),
        ),
    )
    claim = LiteratureClaim(
        claim_id="C1",
        section="spectral",
        claim="An insulator has a gap.",
        queries=("insulator filled band gap",),
    )
    bundle = build_claim_evidence_bundle(database, claim)
    assessment = assess_with_generator(
        bundle,
        lambda model, system, prompt: json.dumps(
            {
                "status": "SUPPORTED",
                "summary": "The source directly states the band picture.",
                "corrected_claim": None,
                "assumptions": ["Independent-particle band description"],
                "citations": ["E1"],
                "source_requests": [],
            }
        ),
    )

    review = render_literature_review((bundle,), (assessment,))

    assert "AUTOMATED_UNREVIEWED" in review
    assert "### C1 — SUPPORTED" in review
    assert "`@one`, physical page 3" in review
