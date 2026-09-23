# Software Review Notes

## Purpose

Software reviews must turn observations into explicit, evidence-backed actions.
A review finding is not a severity score, work authorization, or human
acceptance. It records the problem, its current disposition, the evidence and
consequence, and the next action or revisit condition.

## Finding Record

Use this shape for every retained finding:

```text
Finding: <stable identifier and concise problem statement>
Disposition: <one DispositionTypes value>
DispositionTypes:
  - MUST_FIX
  - HUMAN_DECISION_REQUIRED
  - SAFE_TO_DEFER
  - NO_ACTION_REQUIRED
Evidence: <file and line, command result, reproduction, or contract conflict>
Consequence: <what can happen if the finding remains unresolved>
NextAction: <specific correction, decision, or objective revisit condition>
```

`DispositionTypes` defines the closed set of allowed values. A finding selects
exactly one of them in `Disposition`:

- `MUST_FIX` — a demonstrated defect prevents the current scope from meeting
  its definition of done;
- `HUMAN_DECISION_REQUIRED` — materially different defensible choices remain
  at a human-owned boundary;
- `SAFE_TO_DEFER` — a concrete issue exists but does not block the current
  bounded scope; and
- `NO_ACTION_REQUIRED` — the concern is resolved, invalid, stale, speculative,
  or outside the applicable scope.

A `SAFE_TO_DEFER` finding must name a concrete revisit condition. “Later” by
itself is not sufficient. Reviewers must update the finding when its revisit
condition becomes true rather than silently carrying the old disposition
forward.

## Review Summary

A review summary records a technical outcome separately from operator input:

- `CHANGES_REQUIRED` — at least one `MUST_FIX` remains;
- `REVIEW_INCONCLUSIVE` — missing or conflicting evidence prevents a bounded
  conclusion; or
- `NO_BLOCKING_FINDINGS` — the review found no blocker in its stated scope.

Operator clarification, decision, authorization, and observable-outcome
confirmation remain separate from technical review. A passing test suite is
evidence; it is not release, publication, or acceptance authority.

## Current Application: v0 Ingestor Pilot

The current bounded scope is a single-document pilot that parses one BibTeX
reference, processes a PDF page by page, produces page-linked chunks, and
selects one lexical chunk. The following findings are intentionally deferred;
they become active when their stated revisit conditions occur.

### INGESTION-PILOT-001

Finding: `BaseDocument` requires a BibTeX reference.
Disposition: `SAFE_TO_DEFER`
DispositionTypes: `MUST_FIX`, `HUMAN_DECISION_REQUIRED`, `SAFE_TO_DEFER`,
`NO_ACTION_REQUIRED`
Evidence: `projectkoios-ingestion:src/python/projectkoios/ingestion/base.py`
uses `BibTexRecord` as `BaseDocument.source_id`.
Consequence: A future non-bibliographic source cannot use the facade without a
reference record.
NextAction: Preserve the citation-first facade for the pilot. Raise
`BibtexReferenceError` when a document has no BibTeX reference. Revisit when the
first supported source cannot supply a citation record; then introduce the
smallest compatible non-bibliographic source identity without breaking the
facade.

### INGESTION-PILOT-002

Finding: PDF processing projects extracted evidence to page text and does not
retain the complete extraction result on `PdfProcessedDocument`.
Disposition: `SAFE_TO_DEFER`
DispositionTypes: `MUST_FIX`, `HUMAN_DECISION_REQUIRED`, `SAFE_TO_DEFER`,
`NO_ACTION_REQUIRED`
Evidence:
`projectkoios-ingestion:src/python/projectkoios/ingestion/documents/pdf.py`
constructs page records from text blocks only.
Consequence: Chunks cannot recover exact block geometry, extraction warnings,
or the complete cold-extraction evidence graph.
NextAction: Revisit before the pilot claims evidence-grounded citation,
independent replay, or provenance-complete retrieval. Retain the extraction
result and exact source references at that boundary.

### INGESTION-PILOT-003

Finding: `BibtexParser` retains ordinary entry fields but not the exact source
entry or Pybtex person records.
Disposition: `SAFE_TO_DEFER`
DispositionTypes: `MUST_FIX`, `HUMAN_DECISION_REQUIRED`, `SAFE_TO_DEFER`,
`NO_ACTION_REQUIRED`
Evidence: `projectkoios-ingestion:src/python/projectkoios/ingestion/bibtex.py`
projects `entry.fields`; Pybtex stores authors and similar people separately.
Consequence: The pilot record is insufficient for exact bibliography replay or
complete author metadata.
NextAction: Revisit before bibliography data becomes authoritative,
user-visible, exportable, or part of a stable identity. Retain the exact entry
and required person data then.

### INGESTION-PILOT-004

Finding: `PilotIngestionPipeline.chunks` is assigned only after `ingest()` and
is overwritten by another ingestion.
Disposition: `SAFE_TO_DEFER`
DispositionTypes: `MUST_FIX`, `HUMAN_DECISION_REQUIRED`, `SAFE_TO_DEFER`,
`NO_ACTION_REQUIRED`
Evidence:
`projectkoios-ingestion:src/python/projectkoios/ingestion/pilot/pipeline.py`
declares mutable per-run chunk state.
Consequence: Access before ingestion fails, and concurrent or multi-document
reuse can expose the wrong chunk set.
NextAction: Revisit before concurrent, asynchronous, or multi-document use.
Replace shared run state with an explicit immutable run result.

### INGESTION-PILOT-005

Finding: `PilotRAG` performs lexical retrieval and returns a source chunk; it
does not perform generation.
Disposition: `SAFE_TO_DEFER`
DispositionTypes: `MUST_FIX`, `HUMAN_DECISION_REQUIRED`, `SAFE_TO_DEFER`,
`NO_ACTION_REQUIRED`
Evidence: `projectkoios-ingestion:src/python/projectkoios/ingestion/pilot/rag.py`
selects the chunk with the largest token overlap and returns its text.
Consequence: Calling this behavior RAG can overstate the pilot and confuse
retrieval with generation.
NextAction: Revisit before exposing a user-facing RAG claim. Either rename the
component to a retriever or add an explicit generation boundary and grounded
answer contract.
