from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

from dev.rag_mvp.literature_review import (
    ArchivedOllamaLiteratureReviewer,
    ClaimAssessment,
    OllamaReviewConfiguration,
    build_claim_evidence_bundle,
    load_literature_claims,
    render_literature_review,
    write_assessment,
    write_evidence_bundle,
)
from dev.rag_mvp.rag import DEFAULT_MODEL, RagMvpError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="koios-literature-review-pilot",
        description=(
            "Build a bounded source-linked literature review with local Ollama."
        ),
    )
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--claims", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--model-digest", required=True)
    parser.add_argument("--minimum-ollama-version", default="0.34.2")
    parser.add_argument("--per-query-limit", type=int, default=6)
    parser.add_argument("--total-limit", type=int, default=10)
    parser.add_argument("--retrieve-only", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return _run(args)
    except RagMvpError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


def _run(args: argparse.Namespace) -> int:
    output = args.output.expanduser()
    archive = args.archive.expanduser()
    _prepare_directory(output)
    _prepare_directory(archive)
    evidence_directory = output / "evidence"
    assessment_directory = output / "assessments"
    _prepare_directory(evidence_directory)
    _prepare_directory(assessment_directory)
    claims = load_literature_claims(args.claims)
    bundles = []
    for claim in claims:
        bundle = build_claim_evidence_bundle(
            args.db,
            claim,
            per_query_limit=args.per_query_limit,
            total_limit=args.total_limit,
        )
        write_evidence_bundle(
            evidence_directory / f"{claim.claim_id}.json",
            bundle,
        )
        bundles.append(bundle)
    if args.retrieve_only:
        _write_manifest(output, claims, bundles, (), runtime_version=None)
        print(
            json.dumps(
                {
                    "claims": len(claims),
                    "evidence_items": sum(
                        len(bundle.evidence) for bundle in bundles
                    ),
                    "assessment": "NOT_RUN",
                },
                indent=2,
            )
        )
        return 0
    reviewer = ArchivedOllamaLiteratureReviewer(
        OllamaReviewConfiguration(
            model=args.model,
            model_digest=args.model_digest,
            minimum_version=args.minimum_ollama_version,
        ),
        archive,
    )
    runtime_version = reviewer.validate_runtime()
    assessments: list[ClaimAssessment] = []
    for index, bundle in enumerate(bundles, start=1):
        assessment = reviewer.assess(bundle)
        write_assessment(
            assessment_directory / f"{bundle.claim.claim_id}.json",
            assessment,
        )
        assessments.append(assessment)
        print(
            f"[{index}/{len(bundles)}] {assessment.claim_id}: "
            f"{assessment.status}",
            file=sys.stderr,
        )
    review = render_literature_review(bundles, assessments)
    _atomic_write(output / "literature-review.md", review.encode("utf-8"))
    _write_manifest(
        output,
        claims,
        bundles,
        tuple(assessments),
        runtime_version=runtime_version,
    )
    print(
        json.dumps(
            {
                "claims": len(claims),
                "evidence_items": sum(
                    len(bundle.evidence) for bundle in bundles
                ),
                "assessment": "AUTOMATED_UNREVIEWED",
                "review": str(output / "literature-review.md"),
                "manifest": str(output / "manifest.json"),
            },
            indent=2,
        )
    )
    return 0


def _write_manifest(
    output: Path,
    claims: tuple[object, ...],
    bundles: list[object],
    assessments: tuple[ClaimAssessment, ...],
    *,
    runtime_version: str | None,
) -> None:
    artifacts = []
    for path in sorted(output.rglob("*")):
        if not path.is_file() or path.name == "manifest.json":
            continue
        artifacts.append(
            {
                "path": str(path.relative_to(output)),
                "byte_length": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    payload = {
        "schema": "koios.literature-review-pilot-manifest.v1",
        "claim_count": len(claims),
        "evidence_item_count": sum(
            len(bundle.evidence)
            for bundle in bundles  # type: ignore[attr-defined]
        ),
        "assessment_count": len(assessments),
        "assessment_status": (
            "AUTOMATED_UNREVIEWED" if assessments else "NOT_RUN"
        ),
        "ollama_runtime_version": runtime_version,
        "artifacts": artifacts,
        "human_disposition": None,
        "classifier_implementation_authorized": False,
        "scientific_calculation_authorized": False,
    }
    _atomic_write(output / "manifest.json", _canonical_bytes(payload))


def _prepare_directory(path: Path) -> None:
    if path.is_symlink():
        raise RagMvpError(f"symlinked directory is not accepted: {path}")
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(path, 0o700)


def _canonical_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def _atomic_write(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        raise RagMvpError(f"output already exists: {path.name}")
    temporary = path.with_name(f".{path.name}.tmp")
    if temporary.exists() or temporary.is_symlink():
        raise RagMvpError(f"temporary output exists: {temporary.name}")
    with temporary.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.chmod(temporary, 0o600)
    os.replace(temporary, path)


if __name__ == "__main__":
    raise SystemExit(main())
