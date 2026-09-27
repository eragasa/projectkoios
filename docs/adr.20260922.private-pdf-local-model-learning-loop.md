# ADR20260922: Private PDF corpus processing and local-model learning loop

## Status

Proposed design only.

The Project Koios operator authorized preparation of this recommendation on
2026-09-22. This record does not accept the architecture, authorize component
implementation, authorize a private corpus run, grant database credentials,
commit or push changes, promote a model, or authorize publication.

## Context

Project Koios has PDFs in more than one private source system. Some are files in
registered repositories, including explicitly private or Git-ignored archive
areas. Others may be stored as database blobs or referenced by database records.
The operator wants local language models to process every available PDF and to
improve over time as their output is reviewed.

"Every available PDF" must not mean that a model can crawl the machine, execute
arbitrary SQL, follow arbitrary URLs, or widen its own access. Discovery must be
performed by deterministic, read-only adapters over explicitly registered
sources. Source access, local processability, rights, student visibility, and
publication permission remain separate concerns.

The existing ingestion architecture already provides content-addressed PDF
extraction, page provenance, bounded rendering, optional OCR, structure
proposals, clean transcripts, immutable derived evidence, and batch planning.
The accepted private-instance layout separates source bytes, immutable records,
derived artifacts, disposable projections, mutable state, and staging. The
proposed evidence-grounded retrieval architecture prohibits generated summaries
and assessments from silently becoming source evidence.

The current `UC-01` use case explicitly excludes bulk ingestion of every private
PDF. This proposal therefore defines a separate private corpus-processing
capability. It does not silently expand or amend `UC-01`.

## Proposed decision

Project Koios should implement an explicit, local-only PDF corpus loop with five
separate stages:

```text
registered repository and database sources
    -> deterministic discovery and exact-byte snapshot
    -> immutable extraction, transcript, and audit evidence
    -> two independent local-model assessment candidates
    -> human review and correction records
    -> evaluation-gated prompt, retrieval, adapter, or model promotion
```

All eligible PDFs receive a terminal processing disposition. A disposition may
be `completed`, `partial`, `failed`, `duplicate`, `deferred_by_policy`, or
`deferred_by_resource_limit`. "Process all" does not mean silently ignoring
failures, OCRing every page regardless of need, or accepting every model output.

The first implementation should be an explicit batch CLI. It should plan by
default and require `--apply` for source snapshots, extraction, model execution,
or artifact publication. A daemon, scheduler, lease system, remote worker, or
autonomous retry service is deferred.

## Goals

1. Discover every PDF exposed by an authorized repository or database adapter.
2. Snapshot and identify exact source bytes without modifying the source.
3. Deduplicate identical bytes while retaining every observed origin.
4. Produce evidence-linked local-model assessments for every eligible document.
5. Route disagreements, uncertainty, and policy-sensitive material to review.
6. Convert human corrections into versioned evaluation and learning evidence.
7. Improve prompts, retrieval examples, rules, adapters, and optionally local
   model weights without an uncontrolled feedback loop.
8. Keep source evidence, generated interpretation, human decisions, execution
   authority, and publication authority separate.

## Non-goals

This proposal does not provide:

- unrestricted filesystem crawling;
- model-generated SQL, shell commands, paths, URLs, or access expansion;
- cloud inference or remote-provider fallback;
- automatic authorship, rights, scientific, mathematical, or pedagogical
  acceptance;
- automatic student access, publication, repository mutation, commit, or push;
- generated prose reintroduced as primary source evidence;
- silent correction of extracted source text;
- online weight updates after each document;
- a production scheduler or shared multi-operator execution authority; or
- migration or deletion of existing source or derived artifacts.

## Architectural invariants

1. Source PDFs are opened read-only and never modified.
2. Every processed byte sequence has an exact SHA-256 identity.
3. A locator identifies an observation origin, not a document's canonical
   identity.
4. Identical bytes from multiple origins share processing artifacts while
   retaining all origin observations.
5. Raw extraction remains separate from OCR, reconciliation, model output, and
   human correction.
6. Model output is always `automated_unreviewed` until an authorized human
   decision record says otherwise.
7. Model agreement is evidence, not truth or acceptance.
8. Generated summaries and assessments never enter the source-evidence corpus.
9. Every processor, prompt, model, resource, configuration, and output is
   identity-bound.
10. Finalized records and artifact generations are append-only; corrections and
    promotions create new records.
11. Database and browser views are disposable projections, not historical
    authority.
12. Publication and student-facing projection require separate decisions and
    separate operations.

## Source discovery boundary

### Registered source configuration

A private deployment configuration identifies named source adapters and their
read boundaries. No default adapter scans the user's home directory.

```toml
[[pdf_sources]]
id = "course-archives"
kind = "repository"
root = "/configured/private/root"
include_tracked = true
include_private_roots = ["legacy/private-sources"]

[[pdf_sources]]
id = "document-catalog"
kind = "database"
connection = "configured-read-only-connection"
query_id = "registered-pdf-assets-v1"
```

Machine-specific paths, connection details, credentials, and private locators
remain outside Git and public logs.

### Repository adapter

A repository adapter may discover:

- PDFs tracked at an exact Git commit;
- PDFs in the current working tree when that mode is explicitly selected; and
- PDFs below explicitly registered private roots, including ignored roots.

The adapter must:

- reject symlinked roots and source files;
- reject traversal outside the configured root;
- classify tracked, untracked, ignored-private, and historical sources
  separately;
- record Git commit and blob identity where applicable;
- record a bounded private origin observation for non-Git files;
- recheck file identity after opening and before snapshot publication; and
- never infer that Git visibility grants student or publication access.

### Database adapter

A database adapter uses read-only credentials and one registered query or
repository method. It may discover:

- PDF bytes stored in a bounded blob field;
- immutable artifact records resolving to PDF bytes; or
- registered local or object-store references resolved by a separate bounded
  byte loader.

The adapter must not accept model-generated SQL, table names, row filters, URLs,
or credentials. It records the database instance identity, registered query
identity, row identity, row version or transaction snapshot, media type, stated
byte size, and exact observed byte hash. A mutable database row is an origin
observation, not immutable source authority.

Network retrieval is disabled by default. Enabling a registered object-store
loader requires a separate deployment decision and exact endpoint, credential,
size, redirect, and content-type policy.

### Discovery observation

A source discovery produces a compact private observation equivalent to:

```json
{
  "schema": "projectkoios.pdf-source-observation:proposed-0.1.0",
  "source_adapter_id": "configured-adapter",
  "origin_kind": "git_blob | working_tree | private_file | database_blob | database_reference",
  "origin_identity": "private-content-addressed-observation",
  "origin_version": "adapter-specific-version-token",
  "declared_media_type": "application/pdf",
  "observed_byte_size": 12345,
  "observed_sha256": "...",
  "access_scope": "private_local",
  "locator_disclosure": "private_only"
}
```

The final contract must avoid placing private paths, database keys, credentials,
or source excerpts in public projections.

## Corpus snapshot and batch planning

Discovery creates an immutable corpus snapshot containing the complete ordered
set of source-observation identities. Large collections are partitioned into
bounded plans; the top-level snapshot binds the ordered partition identities.

Planning is read-only and reports:

- unique exact PDF blobs;
- duplicate origin groups;
- unsupported or malformed sources;
- encrypted sources;
- admission-policy failures;
- expected extraction and model work;
- cache hits;
- projected storage; and
- every terminal preflight disposition.

Explicit apply performs one bounded partition at a time. A partial batch remains
truthful: completed items remain immutable, and unprocessed items retain their
planned identities and explicit status. Retry uses a new plan over unfinished
or retryable items rather than relabeling the original run.

## Exact-byte snapshot and deduplication

Before durable processing, admitted source bytes are copied into the configured
private content-addressed store. The snapshot operation rechecks size, SHA-256,
PDF header, and source-version evidence on the bytes actually read.

```text
blobs/sha256/<prefix>/<sha256>
records/sources/<sha256>/manifest.json
records/source-origins/<observation-id>.json
```

One exact blob is extracted once for a compatible configuration. Every origin
continues to resolve to that blob. Duplicate origins are not discarded and do
not inflate training or evaluation samples.

## Admission and containment

PDF parsers, OCR engines, and model runtimes process attacker-controlled bytes
and text even in a private corpus. Each stage therefore has independent limits
for:

- source byte size;
- page count and page dimensions;
- decompression and retained object counts;
- extraction time and memory;
- rendered pixels and image bytes;
- OCR processes, duration, and captured output;
- transcript characters and model context;
- generated tokens;
- batch concurrency; and
- retained artifact size.

Cold PDF parsing and OCR should run in an operating-system isolation boundary
when processing untrusted documents. Model workers receive bounded transcript or
rendered selections, not arbitrary filesystem handles. A source failure cannot
change another source's result.

## Deterministic document processing

The reusable evidence path remains owned by `projectkoios-ingestion`:

```text
exact source blob
    -> cold extraction
    -> layout and structure proposals
    -> selective OCR and deterministic reconciliation
    -> structured and clean transcript
    -> derivation audit
    -> compact reference-evidence projection
```

Native text is preferred when usable. OCR is selected by explicit quality and
policy rules, such as image-only or low-text pages. Every OCR page remains a
separate stream until deterministic reconciliation. Model output cannot repair
or overwrite either stream.

All PDFs receive extraction or an explicit extraction disposition. Expensive
page rendering, OCR, equation recognition, table reconstruction, and figure
analysis remain bounded derived stages and need not run on pages where their
admission rule does not select work.

## Local-model assessment

### Runtime boundary

Model-provider implementations remain outside the ingestion package. The first
runtime should use a local process or loopback-only endpoint with:

- no remote-provider fallback;
- no network tools;
- no shell, filesystem, database, Git, or publication tools;
- exact executable and model-resource hashes;
- explicit runtime, quantization, context, prompt, sampler, and seed settings;
- bounded input and output;
- strict JSON output validation; and
- private logs that omit full source text by default.

Model stochasticity must be represented honestly. A stored first result can be
immutable and replayable as an observation without claiming that a future model
invocation will reproduce identical text.

### Two independent roles

The two initial local processors have intentionally different tasks.

**Scout**

- proposes document kind and topic labels;
- drafts a concise private summary;
- identifies assignment, solution, syllabus, article, textbook, and other
  content candidates;
- proposes sensitivity, rights-review, and student-visibility flags;
- emits evidence-linked claim candidates; and
- abstains when extraction is inadequate.

**Verifier**

- receives the same bounded evidence independently;
- checks whether proposed fields can be supported by page or span evidence;
- looks for omitted sensitivity, rights, and solution-material risks;
- challenges unsupported summaries and classifications; and
- emits its own assessment before seeing the Scout output.

Only after both immutable outputs exist does a deterministic comparator produce
agreements, disagreements, missing fields, evidence conflicts, and review
priority. If both roles use the same model and prompt family, the record states
that their independence is limited.

### Prompt-injection boundary

Extracted PDF text is untrusted data. Prompts must frame it as quoted source
material that cannot issue instructions. The model has no tools with which to
act on embedded instructions. Output fields are schema-constrained, length
bounded, and rejected if they contain unknown fields, invalid locators, or
references to evidence not supplied in the request.

### Assessment candidate

A model assessment candidate should bind:

- exact source, extraction, transcript, and audit identities;
- exact bounded page, span, or object evidence made available;
- assessment task and schema version;
- processor role;
- model, runtime, prompt, configuration, and resource identities;
- proposed document class, topics, summary, and flags;
- evidence references for every factual field;
- explicit abstentions, warnings, and truncation;
- completion, partial, or failed status; and
- canonical serialized output identity.

It must not contain an accepted authorship, rights, student-access, scientific,
pedagogical, retention, or publication decision.

## Human review and corrections

A local review interface presents exact page evidence beside both model outputs
and their deterministic comparison. The reviewer can:

- accept, reject, or correct individual proposed fields;
- mark a model claim unsupported;
- identify missing sensitivity or rights flags;
- distinguish extraction error from model error;
- request re-extraction or OCR for a bounded page;
- record a purpose-scoped document disposition; and
- decline to make a decision.

A correction record identifies the exact model output, evidence considered,
corrected field, prior value, corrected value, rationale, reviewer identity,
reviewer authority and scope, and any superseded review record. A mutable review
database may project current state, but the correction or decision record is
append-only authority.

## Improvement loop

The system improves through controlled candidate releases rather than autonomous
self-modification.

### Improvement order

Use the least risky mechanism that fixes the observed failure:

1. deterministic extraction or normalization correction;
2. source-admission or classification rule correction;
3. prompt or schema revision;
4. retrieval of bounded, reviewed examples;
5. local adapter or LoRA training over explicitly eligible reviewed examples;
6. replacement of the local base model.

A model must not train on its own unreviewed output. Agreement between models is
not a training label. Generated summaries are never source evidence.

### Training-example eligibility

A reviewed correction can become a training example only when a separate
eligibility record confirms:

- exact upstream source and review identities;
- the reviewer and scope of the correction;
- permitted local training use;
- absence or explicit handling of sensitive data;
- bounded included evidence;
- no unresolved extraction defect affecting the label;
- no train/evaluation split conflict; and
- a retraction path if the source or permission is later withdrawn.

Rights to possess or review a PDF do not automatically grant permission to
redistribute a derived dataset or model adapter. Training artifacts remain
private and action-specific rights decisions remain separate.

### Reviewed-example retrieval

Before weight tuning, the runtime may retrieve a small number of similar,
reviewed examples. Examples remain clearly separated from the current source
and include their correction identities. Selection policy, ordering, distance,
and truncation are versioned. Document-level deduplication prevents the same
source or near-duplicate from dominating the examples.

### Evaluation sets

Evaluation splits are made by exact document or duplicate group, never by
random page, so pages from one PDF cannot appear in both training and held-out
evaluation. A permanent hidden regression set contains:

- native-text and scanned PDFs;
- mixed and malformed layouts;
- assignments, solutions, syllabi, articles, and books;
- known personal-information and rights-review cases;
- prompt-injection text;
- duplicate origins;
- insufficient-evidence cases; and
- expected abstentions and failures.

Private evaluation records retain identities and metrics without exposing
source text publicly.

### Metrics

Promotion evidence should include at least:

- document-class precision and recall;
- known sensitive-information recall and false-negative count;
- evidence-locator validity;
- unsupported factual-field rate;
- appropriate abstention rate;
- extraction-error versus model-error routing accuracy;
- inter-model disagreement rate;
- human correction rate by field;
- median human review time;
- failure and resource-limit rates; and
- latency and local resource use.

Self-reported model confidence is not treated as calibrated probability. A
promotion threshold is fixed before an evaluation run and cannot be selected
after seeing candidate results.

### Active review selection

Human review is prioritized for:

- Scout/Verifier disagreements;
- missing or invalid evidence references;
- poor extraction or OCR quality;
- novel layouts or low-neighbor-distance examples;
- policy-sensitive documents;
- changed behavior between model releases; and
- a random sample of apparent agreements.

The random sample detects correlated mistakes. Duplicate PDFs count once for
model evaluation while retaining all origin-level policy decisions.

### Candidate release and promotion

A candidate release binds the exact:

- base model and optional adapter bytes;
- runtime and quantization;
- prompt and schema;
- reviewed-example index;
- deterministic preprocessing;
- evaluation-set generation;
- thresholds; and
- evaluation report.

Promotion is a separate human-authorized record. It identifies the prior
champion, candidate, evaluation evidence, scope, rationale, and rollback target.
A promoted model affects only new derived generations. Prior outputs are not
silently relabeled or overwritten.

## Storage and projection

The accepted private-instance roles should be extended without mixing evidence
and interpretation:

```text
records/pdf-discovery/             # immutable source observations
collections/pdf-corpora/           # immutable corpus snapshots and partitions
artifacts/extractions/             # deterministic source-derived evidence
artifacts/transcripts/             # deterministic source-derived evidence
artifacts/model-assessments/       # generated, automated_unreviewed
records/model-comparisons/         # deterministic assessment comparisons
records/human-corrections/         # append-only human review evidence
artifacts/training-candidates/      # private, eligibility-gated
artifacts/model-evaluations/        # immutable evaluation runs
records/model-promotions/           # human-authorized promotion history
projections/pdf-review/             # disposable local review database
state/pdf-runs/                     # mutable local execution state
staging/                            # incomplete work, never retrieval input
```

Artifact directories and private files use the private-instance permission
policy. Staging, model logs, summaries, and review state are not committed to
source repositories by default.

## Workflow and execution authority

`projectkoios-workflow` may own engine-neutral review and model-promotion state,
but compact workflow events contain artifact identities rather than PDF bytes,
transcripts, prompts, or summaries. Decisions, evidence, operation authority,
and effects remain separate.

The initial implementation should not require a scheduler. An operator invokes a
bounded plan explicitly. A future worker/lease/dispatch system requires its own
accepted design and cannot be inferred from this document or the current
workflow runtime.

## Repository ownership

- `projectkoios` owns this cross-repository proposal and any acceptance record.
- `projectkoios-ingestion` owns PDF source-observation and corpus-plan contracts,
  exact-byte ingestion, extraction, OCR, transcript, audit, and assessment-
  candidate boundaries.
- `projectkoios-agent` owns concrete local-model runtime adapters and prompts.
- `projectkoios-workflow` owns review progression and model-promotion workflow
  semantics, not source or generated payloads.
- `projectkoios-references` owns bibliographic identity, acquisition, access,
  and rights evidence for reference assets.
- `projectkoios-search` owns reviewed-example and retrieval indexes when those
  become reusable search capabilities.
- `projectkoios-api` and `projectkoios-web` may expose authenticated private
  projections after local authentication, session, CSRF, CORS, and audit
  boundaries are accepted.
- A deployment adapter owns configured repository/database access, local storage,
  explicit execution, and operating-system isolation.
- The designated human owner retains authorship, rights, student-access,
  scientific, pedagogical, model-promotion, and publication decisions.

These assignments select dependency direction. They do not authorize owner-
repository implementation.

## Threat model and defenses

| Failure or attack | Required defense |
|---|---|
| Malformed PDF exploits native parser | Source admission, versioned parser identity, resource limits, and OS isolation |
| PDF text contains model instructions | Treat text as untrusted quoted data; model has no tools or network |
| Symlink escapes a repository root | Descriptor-relative/no-follow access and post-open identity checks |
| Mutable file changes during discovery | Exact-byte snapshot and version/hash recheck |
| Database query scope widens | Registered read-only query; no model-authored SQL |
| Database pointer redirects externally | Registered resolver and endpoint policy; network disabled by default |
| Duplicate PDF dominates learning | Exact-hash and near-duplicate grouping with document-level splits |
| Both models repeat the same error | Blind passes, heterogeneous resources where practical, and random agreement review |
| Model invents a locator | Schema validation against the exact supplied evidence set |
| Generated summary becomes evidence | Separate artifact role and index exclusion |
| Sensitive text enters logs | Metadata-only public logs and private bounded diagnostics |
| Training data is poisoned | Human-reviewed eligibility, immutable lineage, held-out regression, and promotion gate |
| Adapter improves average accuracy but harms privacy recall | Per-metric no-regression promotion thresholds |
| Source permission is withdrawn | Source-to-example lineage, retraction records, affected-adapter inventory, and retraining decision |
| A failed item disappears from reports | Required terminal disposition for every corpus item |

## Delivery phases

### Phase 0 — Design and fixtures

- review and accept or reject this architecture separately;
- define synthetic and redistributable repository/database fixtures;
- define source observation, corpus snapshot, and assessment candidate proposals;
- fix resource ceilings and private logging policy; and
- define a small pre-registered evaluation matrix.

### Phase 1 — Read-only discovery

- implement repository and fake/database protocol adapters;
- produce a dry-run corpus snapshot;
- verify deduplication, symlink rejection, pagination, and complete dispositions;
- perform no source snapshot or model execution by default.

### Phase 2 — Deterministic processing

- snapshot exact bytes into the private store;
- reuse existing batch extraction and cache behavior;
- produce transcripts, audits, and explicit partial/failure records;
- verify source immutability and replay.

### Phase 3 — Two-model assessment

- implement one Scout and one Verifier local adapter;
- enforce blind execution and strict schemas;
- produce deterministic comparisons and a private review projection;
- prohibit model-based mutation or publication.

### Phase 4 — Reviewed-example learning

- capture field-level corrections;
- create eligibility and split records;
- add reviewed-example retrieval;
- measure against the frozen held-out set.

### Phase 5 — Optional local fine-tuning

- create a private candidate adapter only when reviewed-example retrieval no
  longer provides sufficient improvement;
- evaluate against the champion and hidden regression set;
- require separate promotion authority; and
- preserve rollback and prior generations.

## Acceptance criteria for a first bounded implementation

A first implementation is technically complete only when it demonstrates:

1. one repository fixture and one database fixture under read-only adapters;
2. complete discovery with no arbitrary traversal, SQL, or URL access;
3. exact-byte deduplication with multiple retained origin observations;
4. immutable source snapshots and no source mutation;
5. bounded extraction with explicit completed, partial, and failed outcomes;
6. two blind local-model assessments with complete resource identities;
7. rejection of invented evidence locators and prompt-injection instructions;
8. a deterministic disagreement projection;
9. field-level human corrections without relabeling source evidence;
10. document-group train/evaluation isolation;
11. a pre-registered candidate-versus-champion evaluation;
12. a separate human promotion record and working rollback;
13. no generated assessment in a source-evidence index;
14. no private path, database key, source excerpt, or credential in public logs,
    fixtures, issues, or documentation; and
15. no commit, push, student projection, or publication side effect from corpus
    processing.

Real private PDFs may supplement these fixtures only in an explicitly authorized
local acceptance run. They do not become repository fixtures or public evidence.

## Alternatives considered

### Let models crawl repositories and databases directly

Rejected. It grants unnecessary authority, prevents complete replay, and turns
prompt injection or model error into an access-control problem.

### Use one model and trust confidence scores

Rejected. Self-reported confidence is not calibrated evidence. Independent
roles, deterministic evidence validation, human corrections, and held-out
metrics provide stronger signals.

### Fine-tune continuously after every review

Rejected. Online updates make behavior difficult to reproduce, amplify bad
labels, blur training and evaluation, and provide no safe rollback.

### Treat model agreement as acceptance

Rejected. Correlated models can agree on the same unsupported output. Agreement
only changes review priority.

### Put generated summaries in the source search corpus

Rejected. This creates circular evidence and allows model errors to influence
future source retrieval.

### Make the database the authority for historical processing

Rejected. A mutable database is a useful read source or disposable projection,
but immutable observations, artifacts, decisions, and promotion records retain
historical authority.

### Process only previously curated references

Rejected for this private-corpus capability. The operator requested complete
coverage of PDFs exposed by registered repository and database adapters.
Completeness is reported through terminal dispositions rather than by silently
narrowing discovery.

## Relationship to existing records

- This proposal follows the accepted reference authority and projection
  architecture.
- It extends the proposed private-instance artifact layout with model-assessment,
  correction, evaluation, and promotion roles.
- It preserves the evidence-grounded retrieval prohibition against generated
  material becoming source evidence.
- It uses the existing ingestion batch and bounded-JIT principles. Bulk work is
  explicit through an immutable plan and `--apply`, never an import-time or
  default side effect.
- It defines a separate capability from `UC-01`, whose current scope continues
  to exclude bulk ingestion of every private PDF.

## Open implementation decisions

The architecture does not yet select:

- the concrete read-only database and snapshot mechanism;
- the first two local model resources;
- whether the initial local runtime uses a subprocess, Unix socket, or loopback
  HTTP adapter;
- exact source and assessment schema encodings;
- corpus partition size below existing hard ceilings;
- near-duplicate detection beyond exact byte identity;
- evaluation thresholds;
- local adapter-training framework; or
- authenticated API and browser review surfaces.

Each choice requires owner-repository implementation evidence and separate
review. None blocks review of the architectural boundaries in this document.
