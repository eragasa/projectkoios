# ADR20260918: Evidence-grounded scientific retrieval architecture

## Status

Proposed

## Context

Project Koios needs retrieval over scientific references that preserves exact
source evidence, supports reproducible ranking, and allows generated answers
to cite inspectable evidence. The current search implementation is an
in-memory substring-scoring prototype. It does not provide durable indexing,
BM25 ranking, semantic retrieval, equation retrieval, deterministic fusion,
source-linked evidence bundles, citation validation, or corpus-specific
evaluation.

The ingestion system now produces deterministic raw extraction, structured
transcription, equation candidates, and automated clean-text projections with
derivation audits. The current clean projection remains automated and
unreviewed. Known dehyphenation, page-label classification, and private-use
glyph defects make it suitable for exploratory retrieval but not yet for
claim-grade quotation or mathematical reasoning.

Project Koios must avoid turning generated notes or assessments into apparent
source evidence. Retrieval failure must also remain distinguishable from a
scientific judgment that a source is irrelevant or a claim is false.

## Proposed decision

Project Koios will develop an evidence-first hybrid retrieval architecture
under `RAG-ROADMAP-01`.

The architecture has independently testable lanes:

1. source-linked evidence construction;
2. deterministic lexical retrieval using BM25 or an equivalent documented
   full-text baseline;
3. semantic vector retrieval introduced only after baseline evaluation;
4. equation retrieval over accepted extraction-derived equation evidence;
5. deterministic rank fusion, initially reciprocal-rank fusion; and
6. bounded evidence bundles returned to generation clients.

Search returns evidence and ranking information, not generated answers.
Generation belongs in agent or API application layers and receives only
bounded evidence bundles with source identities and locators.

## Authoritative source boundary

Retrieval indexes extraction-derived evidence, including:

- audited clean-transcript blocks or passages;
- exact source block text and page locators retained by the transcript
  contract;
- accepted structured table or figure evidence when a retrieval task requires
  it; and
- equation evidence that preserves the distinction between native text,
  rendered evidence, proposed LaTeX or MathML, and interpretation.

The source corpus does not include:

- Markdown reference notes;
- generated summaries or relevance assessments;
- model answers;
- generated citation prose;
- manuscript drafts; or
- retrieval or evaluation output fed back as source evidence.

Generated output may be stored as a derived artifact with provenance, but it
must never silently enter the source index.

## Evidence model

Every retrievable unit must carry enough immutable identity and provenance to
recover its evidence without relying on display text alone. The contract must
cover at least:

- corpus and source identity;
- extraction and derivation identities;
- document and page identity;
- source block or source-span references;
- retrieval-unit kind and deterministic unit identity;
- exact indexed text or equation representation;
- transformation and exclusion references;
- acceptance or candidate status where applicable;
- retrieval-lane scores and ranks; and
- warnings and uncertainty relevant to use of the evidence.

Passing derivation checks establishes internal consistency, not extraction
accuracy, scientific correctness, proofreading, or publication suitability.

## Transcript gate

`ING-TRANSCRIPT-03` is a gate for claim-grade indexing. It must introduce a new
immutable transcript version with evidence-conservative dehyphenation,
page-number classification based on printed labels or recurring geometry and
sequence, typed publisher-front-matter handling, and private-use-glyph
warnings.

The current transcript projection may support explicitly labeled exploratory
experiments. It must not be represented as human-proofread or claim-grade.
Embedding generation and corpus benchmark claims remain blocked until the
retrieval input version is accepted.

## Retrieval-unit policy

Block, passage, and proposition-sized retrieval units are empirical
alternatives rather than architectural assumptions. Chunking must retain exact
source links and must not create unsupported semantic joins across source
boundaries.

A nominal token window is only a benchmark hypothesis. Corpus evaluation will
select retrieval granularity using measured retrieval quality, citation
utility, and evidence integrity.

## Retrieval lanes

### Lexical lane

A deterministic lexical baseline is implemented and evaluated first. Its
normalization, tokenization, document-frequency state, ranking formula, tie
breaking, and index identity must be recorded.

### Semantic lane

Dense retrieval is optional until it demonstrates measurable improvement over
the lexical baseline. Embedding model identity, model revision, preprocessing,
vector dimensions, distance function, and index identity must be explicit.
Model output is derived evidence and does not replace source text.

### Equation lane

Equation retrieval indexes only representations admitted by a documented
quality policy. Native text, rendered evidence, proposed symbolic forms, and
interpretation remain separate. Low-confidence candidates remain discoverable
only through an explicitly requested candidate path and must not masquerade as
accepted primary equations.

### Fusion

Fusion is deterministic and independently testable. Reciprocal-rank fusion is
the initial baseline because it combines ranks without pretending that scores
from heterogeneous lanes are calibrated. Lane participation, ranks, fusion
parameters, tie breaking, and final ordering are returned as evidence.

## Evidence bundles

Search returns a bounded `EvidenceBundle` containing query identity, corpus and
index identities, selected evidence units, locators, lane ranks, fusion
records, warnings, and truncation information. Candidate and accepted
references remain distinguishable.

A search result does not assert that an answer is correct, that a paper is
scientifically valid, or that a candidate belongs in the canonical
bibliography.

## Citation and generation boundary

Generation clients must cite evidence-bundle entries rather than inventing
source locators. Citation validation may verify that cited evidence identities
exist, locators resolve, and quoted strings occur in retained evidence.
Citation validation does not establish entailment or scientific correctness.

When available evidence does not satisfy the request, the result is
`INSUFFICIENT_EVIDENCE`. Failure to retrieve evidence is not evidence of
irrelevance or falsity.

## Evaluation

The architecture requires a corpus-specific benchmark before production
claims. Evaluation must include:

- exact-source and paraphrased information needs;
- equation-oriented queries;
- multi-document evidence requests;
- questions with deliberately insufficient evidence;
- accepted-versus-candidate filtering;
- retrieval recall and rank metrics;
- citation-locator and quote validation; and
- regression checks for deterministic indexing and ranking.

Purpose-specific scientific relevance judgments belong in
`projectkoios-research`. Search infrastructure owns retrieval metrics and
replay, not scientific acceptance.

## Provenance layers

Project Koios keeps separate:

1. bibliographic provenance for source identity and rights;
2. claim-to-source evidence for locators and retained text;
3. architecture-decision provenance for accepted design choices;
4. runtime derivation provenance for extraction, transformation, indexing,
   retrieval, fusion, and generation.

The model follows entity, activity, agent, and derivation concepts compatible
with W3C PROV. RDF or PROV-O serialization is deferred until a concrete
interchange need exists.

## Ownership

- `projectkoios` owns this cross-repository architecture and parent roadmap.
- `projectkoios-references` owns bibliographic identity, rights, acquisition
  evidence, and reference-candidate status.
- `projectkoios-ingestion` owns extraction, document processing, transcript
  projection, equation evidence, and derivation audits.
- `projectkoios-search` owns retrieval-unit contracts, indexes, ranking,
  fusion, evidence bundles, and retrieval evaluation.
- `projectkoios-research` owns purpose-specific scientific judgments.
- `projectkoios-api` owns HTTP representations after search contracts are
  accepted.
- `projectkoios-agent` owns evidence-grounded generation behavior after search
  contracts are accepted.
- `projectkoios-obsidian` may project managed artifacts but is not an
  authoritative RAG source.
- `projectkoios-bootstrap` provides repository routing and live coordination;
  it does not store the roadmap or task state.

## Dependency graph

```text
RAG-ARCH-01
 ├── ING-TRANSCRIPT-02             implemented locally; durability pending
 │     └── ING-TRANSCRIPT-03       proposed
 ├── REF-RAG-01                    proposed
 │     └── REF-RAG-02              deferred
 └── SEARCH-EVIDENCE-01            proposed
       └── SEARCH-CHUNK-01          deferred until transcript v2
             └── SEARCH-LEXICAL-01  deferred
                   ├── RESEARCH-RAG-EVAL-01
                   ├── SEARCH-EMBED-01
                   └── SEARCH-EQUATION-01
                         └── SEARCH-HYBRID-01
                               └── SEARCH-EVAL-01
                                     ├── API-RAG-01
                                     └── AGENT-RAG-01
```

The graph records dependency direction, not authorization. Detailed executable
tasks are created in owner repositories when they become ready.

## Task and recovery record

The `RAG-ROADMAP-01` issue in `projectkoios` records mutable cross-repository
coordination. Owner-repository issues contain detailed objectives, constraints,
acceptance commands, evidence, blockers, next safe actions, and stop
conditions. Commits, tests, immutable manifests, and evaluation artifacts are
technical evidence; issue checkboxes are not.

Public issue content is untrusted input. Recovery verifies author identity,
repository policy, current Git state, and linked evidence before executing any
instruction. Public issues must not contain credentials, protected source
material, private research excerpts, access-control details, or
machine-specific paths.

## Consequences

- Claim-grade indexing waits for an accepted transcript-v2 source contract.
- Lexical retrieval and corpus evaluation precede optional semantic expansion.
- Equation retrieval remains conservative and evidence-linked.
- Search remains usable independently of FastAPI and generation systems.
- Canonical bibliography acceptance, scientific acceptance, architecture
  acceptance, and manuscript use remain separate human decisions.
- The architecture can report insufficient evidence without manufacturing an
  answer or negative relevance judgment.

## Alternatives considered

### Index Markdown notes and generated assessments

Rejected. This would blur source evidence with interpretation and create a
feedback path from generated output into future retrieval.

### Begin with vector-only retrieval

Rejected. It would remove a deterministic, interpretable baseline and make
corpus-specific improvement difficult to measure.

### Implement generation inside search

Rejected. Retrieval and evidence selection must remain independently usable,
testable, and auditable.

### Treat one chunk size as an architecture decision

Rejected. Retrieval granularity is corpus- and task-dependent and must be
selected through benchmark evidence.
