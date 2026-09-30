from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dev.rag_mvp.rag import (
    DEFAULT_CHUNK_WORDS,
    DEFAULT_MAX_PDF_BYTES,
    DEFAULT_MODEL,
    DEFAULT_OVERLAP_WORDS,
    DEFAULT_TOP_K,
    RagMvpError,
    answer,
    audit_citations,
    citation_proposal,
    database_counts,
    discover_pdfs,
    display_page_label,
    extract_pdf,
    index_documents,
    initialize_database,
    load_bibtex_keys,
    load_citation_claims,
    ollama_version,
    search,
)


def _default_database() -> Path:
    configured = os.environ.get("KOIOS_RAG_DB")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".local/share/projectkoios/rag-mvp.sqlite3"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="koios-rag-mvp",
        description="Exploratory local PDF RAG with evidence-linked passages.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=_default_database(),
        help="private SQLite index path",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    ingest = commands.add_parser("ingest", help="extract and index PDFs")
    ingest.add_argument("paths", nargs="+", type=Path)
    ingest.add_argument(
        "--role", choices=("reference", "manuscript"), required=True
    )
    ingest.add_argument(
        "--bibtex",
        type=Path,
        help="BibTeX catalog used only to mark exact filename-key matches",
    )
    ingest.add_argument("--chunk-words", type=int, default=DEFAULT_CHUNK_WORDS)
    ingest.add_argument(
        "--overlap-words", type=int, default=DEFAULT_OVERLAP_WORDS
    )
    ingest.add_argument(
        "--max-pdf-bytes", type=int, default=DEFAULT_MAX_PDF_BYTES
    )

    search_command = commands.add_parser(
        "search", help="retrieve BM25 passages"
    )
    search_command.add_argument("query")
    search_command.add_argument("--limit", type=int, default=DEFAULT_TOP_K)
    search_command.add_argument("--role", choices=("reference", "manuscript"))

    cite = commands.add_parser(
        "cite", help="find reference-only citation candidates for a claim"
    )
    cite.add_argument("claim")
    cite.add_argument(
        "--query", help="optional shorter retrieval query for the exact claim"
    )
    cite.add_argument("--limit", type=int, default=DEFAULT_TOP_K)
    cite.add_argument("--classify", action="store_true")
    cite.add_argument("--model", default=DEFAULT_MODEL)

    audit = commands.add_parser(
        "audit", help="evaluate reference retrieval for a private claim set"
    )
    audit.add_argument("claims", type=Path)
    audit.add_argument("--limit", type=int, default=DEFAULT_TOP_K)
    audit.add_argument("--output", type=Path)

    ask = commands.add_parser("ask", help="answer using local Ollama")
    ask.add_argument("question")
    ask.add_argument("--limit", type=int, default=DEFAULT_TOP_K)
    ask.add_argument("--model", default=DEFAULT_MODEL)

    commands.add_parser("status", help="show local index status")
    commands.add_parser("doctor", help="check SQLite FTS5 and Ollama")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "ingest":
            return _ingest(args)
        if args.command == "search":
            return _search(args)
        if args.command == "cite":
            return _cite(args)
        if args.command == "audit":
            return _audit(args)
        if args.command == "ask":
            return _ask(args)
        if args.command == "status":
            return _status(args)
        if args.command == "doctor":
            return _doctor(args)
        raise RagMvpError(f"unsupported command: {args.command}")
    except RagMvpError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


def _ingest(args: argparse.Namespace) -> int:
    pdfs = discover_pdfs(tuple(args.paths))
    if not pdfs:
        raise RagMvpError("no PDF files were discovered")
    bibtex_keys = load_bibtex_keys(args.bibtex) if args.bibtex else {}
    documents = []
    for index, path in enumerate(pdfs, start=1):
        print(
            f"[{index}/{len(pdfs)}] extracting {path.name}",
            file=sys.stderr,
        )
        matched_key = bibtex_keys.get(path.stem.casefold())
        documents.append(
            extract_pdf(
                path,
                citation_key=matched_key or path.stem,
                bibtex_entry_present=matched_key is not None,
                corpus_role=args.role,
                chunk_words=args.chunk_words,
                overlap_words=args.overlap_words,
                max_pdf_bytes=args.max_pdf_bytes,
            )
        )
    indexed = index_documents(args.db, documents)
    document_count, passage_count = database_counts(args.db)
    print(
        json.dumps(
            {
                "database": str(args.db.expanduser()),
                "indexed_documents": indexed,
                "total_documents": document_count,
                "total_passages": passage_count,
                "bibtex_matches": sum(
                    item.bibtex_entry_present for item in documents
                ),
                "corpus_role": args.role,
                "warnings": sum(len(item.warnings) for item in documents),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _search(args: argparse.Namespace) -> int:
    hits = search(args.db, args.query, limit=args.limit, corpus_role=args.role)
    for hit in hits:
        passage = hit.passage
        printed = display_page_label(passage.printed_page_label)
        citation = (
            "none" if hit.citation_key is None else f"@{hit.citation_key}"
        )
        print(
            f"[S{hit.rank}] score={hit.score:.6f} citekey={citation} "
            f"file={Path(passage.locator).name} "
            f"physical_page={passage.page_index + 1} "
            f"printed_page={printed}"
        )
        print(
            f"passage={passage.passage_id} blocks={','.join(passage.block_ids)}"
        )
        print(passage.text)
        print()
    if not hits:
        print("INSUFFICIENT_EVIDENCE")
    return 0


def _cite(args: argparse.Namespace) -> int:
    proposal = citation_proposal(
        args.db,
        args.claim,
        query=args.query,
        classify=args.classify,
        model=args.model,
        limit=args.limit,
    )
    candidates = []
    for candidate in proposal.candidates:
        passage = candidate.passage
        candidates.append(
            {
                "rank": candidate.rank,
                "citation_key": candidate.citation_key,
                "bibtex_entry_present": candidate.bibtex_entry_present,
                "score": candidate.score,
                "support_status": candidate.support_status,
                "rationale": candidate.rationale,
                "file": Path(passage.locator).name,
                "physical_page": passage.page_index + 1,
                "printed_page": display_page_label(passage.printed_page_label),
                "passage_id": passage.passage_id,
                "block_ids": passage.block_ids,
                "passage": passage.text,
            }
        )
    print(
        json.dumps(
            {
                "claim": proposal.claim,
                "assessment": proposal.assessment,
                "model": proposal.model,
                "candidates": candidates,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def _audit(args: argparse.Namespace) -> int:
    claims = load_citation_claims(args.claims)
    audit = audit_citations(args.db, claims, limit=args.limit)
    rows = []
    for row in audit.rows:
        rows.append(
            {
                "claim_id": row.claim.claim_id,
                "manuscript_sha256": row.claim.manuscript_sha256,
                "lines": row.claim.lines,
                "claim": row.claim.claim,
                "query": row.claim.query,
                "expected_keys": row.claim.expected_keys,
                "expected_keys_available": row.expected_keys_available,
                "expected_outcome": row.claim.expected_outcome,
                "evaluation_status": row.evaluation_status,
                "first_expected_rank": row.first_expected_rank,
                "candidates": [
                    {
                        "rank": hit.rank,
                        "citation_key": hit.citation_key,
                        "bibtex_entry_present": hit.bibtex_entry_present,
                        "score": hit.score,
                        "file": Path(hit.passage.locator).name,
                        "physical_page": hit.passage.page_index + 1,
                        "printed_page": display_page_label(
                            hit.passage.printed_page_label
                        ),
                        "passage_id": hit.passage.passage_id,
                        "passage": hit.passage.text,
                    }
                    for hit in row.hits
                ],
            }
        )
    payload = {
        "assessment": "DETERMINISTIC_RETRIEVAL_EVALUATION",
        "claim_count": len(audit.rows),
        "evaluated_claims": audit.evaluated_claims,
        "corpus_gap_claims": audit.corpus_gap_claims,
        "excluded_claims": audit.excluded_claims,
        "limit": args.limit,
        "hit_at_1": audit.hit_at_1,
        "hit_at_k": audit.hit_at_k,
        "mean_reciprocal_rank": audit.mean_reciprocal_rank,
        "rows": rows,
    }
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output is None:
        print(serialized)
    else:
        output = args.output.expanduser()
        if output.is_symlink():
            raise RagMvpError(f"symlinked output is not accepted: {output}")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized + "\n", encoding="utf-8")
        os.chmod(output, 0o600)
        print(
            json.dumps(
                {
                    "output": str(output),
                    "claim_count": len(audit.rows),
                    "evaluated_claims": audit.evaluated_claims,
                    "corpus_gap_claims": audit.corpus_gap_claims,
                    "hit_at_1": audit.hit_at_1,
                    "hit_at_k": audit.hit_at_k,
                    "mean_reciprocal_rank": audit.mean_reciprocal_rank,
                },
                indent=2,
            )
        )
    return 0


def _ask(args: argparse.Namespace) -> int:
    result = answer(
        args.db,
        args.question,
        model=args.model,
        limit=args.limit,
    )
    print(result.text)
    if result.hits:
        print("\nSources:")
        cited = set(result.citations)
        for hit in result.hits:
            if cited and hit.rank not in cited:
                continue
            passage = hit.passage
            printed = display_page_label(passage.printed_page_label)
            print(
                f"[S{hit.rank}] {Path(passage.locator).name}; "
                f"physical page {passage.page_index + 1}; "
                f"printed page {printed}; {passage.passage_id}"
            )
    return 0


def _status(args: argparse.Namespace) -> int:
    documents, passages = database_counts(args.db)
    print(
        json.dumps(
            {
                "database": str(args.db.expanduser()),
                "documents": documents,
                "passages": passages,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _doctor(args: argparse.Namespace) -> int:
    initialize_database(args.db)
    documents, passages = database_counts(args.db)
    print(f"SQLite FTS5: ready ({documents} documents, {passages} passages)")
    print(f"Ollama: {ollama_version()}")
    print(f"Model configured: {DEFAULT_MODEL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
