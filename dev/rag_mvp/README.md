# Local article RAG MVP

This is a deliberately small exploratory vertical slice. It extracts native PDF
text with `projectkoios-ingestion`, proposes page-local reading order, creates
page-bounded passages, indexes them with SQLite FTS5/BM25, and optionally asks a
local Ollama model to answer from retrieved passages.

It is not claim-grade extraction, OCR, proofreading, scientific validation,
citation verification, or a publication system. Generated output remains local
and automated. PDF text is untrusted data. The answer prompt treats retrieved
text as evidence rather than instructions and rejects model output without valid
source labels.

## Environment

Use the Python 3.14 ingestion environment, which supplies PyMuPDF and the
editable ingestion package:

```bash
cd ~/repos/projectkoios
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli doctor
```

The default private database is outside Git at:

```text
~/.local/share/projectkoios/rag-mvp.sqlite3
```

Override it with `--db PATH` or `KOIOS_RAG_DB`.

## Ingest real PDFs

An argument may be a PDF or a directory scanned recursively. Symlinked inputs
are rejected and symlinked directory entries are skipped.

```bash
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli \
  ingest --role reference --bibtex /path/to/references.bib \
  /private/path/to/articles
```

The role is required and must be `reference` or `manuscript`. Citation discovery
always filters to `reference`; this prevents an indexed manuscript from being
returned as evidence for itself. Separate databases remain preferable. BibTeX
matching is conservative: a key is marked present only when the PDF filename
stem exactly matches a key, ignoring case.

The default source-size ceiling is 100 MB per PDF. Native PDF parsing occurs in
the CLI process and is not a security sandbox. Do not ingest untrusted PDFs
without an operating-system isolation boundary. Malformed legacy PDF page
labels or block geometry trigger an explicitly warned direct-PyMuPDF fallback;
the original PDF bytes are not rewritten.

## Retrieve passages

```bash
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli \
  search "Wannier interpolation effective mass"
```

Results identify the local file, physical page, printed page when available,
passage identity, and retained extraction block identities.

## Find citation candidates

The exact manuscript claim is query data, not evidence. An optional shorter
query can improve lexical retrieval. Citation candidates are diversified so one
reference cannot occupy every result position.

```bash
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli \
  cite --query "Wannier overlap matrices trial projections" \
  "Wannier localization requires overlaps and trial projections."
```

Add `--classify` to ask local Ollama for one of `DIRECT_SUPPORT`,
`PARTIAL_SUPPORT`, `BACKGROUND_ONLY`, `CONTRADICTORY`, or `NO_MATCH`. Every such
classification is labeled `AUTOMATED_UNREVIEWED`; a human must inspect the
page-linked passage before inserting a citation.

A private JSONL claim set can measure deterministic source retrieval:

```bash
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli \
  audit /private/claims.jsonl --limit 6 --output /private/audit.json
```

The audit reports Hit@1, Hit@K, mean reciprocal rank, missing-source corpus gaps,
and page-linked candidate passages. Expected keys are evaluation labels, not
accepted citations.

## Ask local Qwen

Ollama must be running with `qwen3.5:9b` installed:

```bash
../projectkoios-ingestion/.venv/bin/python -m dev.rag_mvp.cli \
  ask "How is effective mass computed from band curvature?"
```

Only retrieved passages are sent to the loopback Ollama API. No external model
API is used. The answer must cite labels such as `[S1]`; otherwise the command
returns `INSUFFICIENT_EVIDENCE`.

## Deliberate omissions

The MVP does not yet provide OCR, embeddings, equation interpretation, semantic
reranking, human citation verification, an HTTP API, or multi-user access.
These should be added only after real-query evaluation shows which limitation is
material.
