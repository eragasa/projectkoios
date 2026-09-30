# PILOT-UC-01-01: Textbook ingestion and RAG

## Record status

- **Pilot ID:** `PILOT-UC-01-01`
- **Definition status:** Draft
- **Execution status:** Not authorized
- **Use case:**
  [UC-01](../use-cases/uc-01.evidence-grounded-textbook-ingestion-and-rag.md)
- **Architecture:** [ingestion](../architecture.ingestion.md) and
  [search](../architecture.search.md)
- **Parent roadmap:** `RAG-ROADMAP-01`

This definition does not authorize ingestion, model execution, private artifact
publication, contract acceptance, or release.

## Objective

Demonstrate that Project Koios can ingest a bounded, equation-heavy textbook
selection and answer reviewed questions using inspectable source evidence while
keeping curated notes separate from primary evidence.

## Bounded scope

The pilot uses:

- one authorized immutable textbook source;
- two adjacent, technically related chapters;
- reviewed explanatory notes for those chapters;
- source-derived figure aids;
- a private reviewed retrieval benchmark; and
- a deterministic lexical baseline before optional retrieval lanes.

The selected material must exercise sections, equations, figures, tables,
physical and printed page identities, source-specific notation, and known
source discrepancies.

Worked examples embedded in prose, end-of-chapter exercises, questions, and
solutions remain distinct content classes. They are excluded from ordinary
retrieval unless the frozen pilot revision explicitly admits a separate,
bounded corpus role. An unreviewed generated example note cannot satisfy the
requirement for reviewed explanatory notes.

## Exclusions

The pilot does not include:

- bulk ingestion of the complete private library;
- source rewriting or correction;
- automatic equation acceptance;
- a production migration;
- manuscript editing;
- citation insertion;
- vector-only retrieval;
- public release of source material;
- ordinary RAG indexing of worked-example or problem-solution notes;
- treating generated notes as reviewed or source evidence; or
- scientific acceptance of the textbook's claims.

## Participating owners

| Owner | Pilot responsibility |
|---|---|
| `projectkoios` | Pilot definition and cross-repository architecture |
| `projectkoios-ingestion` | Source, transcript, structure, equation, figure, note, and derivation processing |
| `projectkoios-search` | Evidence units, indexes, ranking, bundles, and retrieval evaluation |
| `projectkoios-references` | Source identity, acquisition evidence, and rights evidence |
| `projectkoios-agent` | Optional evidence-grounded answer proposal |
| `projectkoios-api` / `projectkoios-web` | Local inspection and review representation |
| Deployment owner | Private storage, executable composition, authorization, and reconciliation |

Component implementation and conformance fixtures remain in their owning
repositories. This document does not copy their contracts.

## Input classes

### Private inputs

- authorized source bytes and source manifest;
- reviewed chapter and section map;
- reviewed notes and figure aids;
- private benchmark questions and expected evidence locators; and
- local run configuration.

### Public inputs

- use-case and architecture records;
- component contract identifiers;
- synthetic parser, chunking, ranking, and failure fixtures; and
- public conformance commands.

Private inputs are referenced by immutable identity, not copied into this
record.

## Required readiness evidence

Before an executable run is requested, the pilot owner records:

1. the actual lifecycle state of every required contract;
2. configuration and data-root capability evidence;
3. source access and action-specific rights evidence;
4. regular-file and no-symlink checks;
5. source-byte identity;
6. the deployment adapter and effect owner;
7. exact operation identities and bounds;
8. private benchmark location and access policy;
9. a versioned content-class and default-exclusion policy;
10. collision and replacement-authority behavior for derived-note targets; and
11. reviewed stop and reconciliation behavior.

A missing accepted baseline may permit a clearly labeled exploratory run but
must not be represented as claim-grade conformance.

## Procedure

### Phase 0: Freeze the pilot revision

1. Record the source identity and bounded chapter selection.
2. Record the participating contract revisions and component baselines.
3. Freeze the private benchmark schema, metrics, and thresholds before running
   retrieval evaluation.
4. Record corpus roles and exclusions.
5. Freeze any admitted worked-example inventory by source-scoped identity,
   structural kind, and physical page span without copying source prose.

### Phase 1: Register and verify the source

1. Resolve the configured private data root.
2. Fail closed if the root is absent, invalid, or symlinked.
3. Verify the source-byte digest without modifying the source.
4. Create or resolve an immutable source manifest.
5. Record physical-page count and available printed page labels separately.

### Phase 2: Produce ingestion generations

1. Emit an immutable literal transcript with page, block, geometry, and warning
   evidence.
2. Emit a structure generation for chapters, sections, equations, figures,
   captions, and tables.
3. Preserve native text, reconstructed equations, rendered aids, and
   interpretations as distinct representations.
4. Emit figure records linked to source page and bounding box.
5. Parse reviewed notes into a separate generation preserving exact Markdown,
   LaTeX, links, embeds, and warnings.
6. Audit every generation against its source and predecessor identities.
7. Preserve unreviewed generated notes, if present, as a separate derived
   candidate class. They do not enter the reviewed-note generation.

### Phase 3: Produce retrieval units

1. Emit page-bounded source-evidence units.
2. Emit equation-context units without unsupported cross-boundary joins.
3. Emit figure-caption and table units where admitted by policy.
4. Emit curated-note units under a discovery-only corpus role.
5. Exclude worked-example, exercise, question, and solution notes by default.
   If the frozen pilot revision admits one of these classes, use a separate
   corpus role and require resolution back to source evidence.
6. Verify that every unit resolves to an immutable generation and exact source
   locator.

### Phase 4: Build deterministic indexes

1. Build and identify the source lexical index.
2. Build a separate discovery index for curated notes.
3. Record normalization, tokenization, document-frequency state, scoring, tie
   breaking, and index identity.
4. Add optional equation or semantic lanes only after recording their quality
   policy and model identity.

### Phase 5: Execute the private benchmark

The reviewed benchmark includes:

- exact-source and paraphrased queries;
- section and page questions;
- equation-oriented questions;
- figure and table questions;
- source-specific notation;
- cross-section synthesis;
- known source discrepancies; and
- deliberately insufficient-evidence requests.

For each query, record candidate evidence, ranks, final bundle, warnings,
latency, and replay identity.

### Phase 6: Generate and inspect bounded answers

1. Supply only the bounded evidence bundle to an optional generation client.
2. Require citations to evidence-bundle entries.
3. Validate evidence identity, locator resolution, and quotations.
4. Present original source evidence, derived representations, warnings, and the
   generated answer together.
5. Record a human pilot disposition without changing source authority.

### Phase 7: Replay

1. Rebuild each immutable generation from the same admitted inputs.
2. Rebuild the deterministic lexical index.
3. Replay benchmark retrieval.
4. Compare artifact identities, rankings, evidence bundles, and warnings.
5. Explain every permitted nondeterministic field explicitly.

## Metrics

Metric definitions and thresholds are frozen before Phase 5. The pilot records
at least:

- section Recall@k;
- exact-page Recall@k;
- mean reciprocal rank;
- equation-evidence retrieval accuracy;
- figure and table association accuracy;
- citation-locator resolution rate;
- quotation-validation rate;
- corpus-role violation count;
- problem-material default-exclusion violation count;
- unsupported-answer count;
- insufficient-evidence accuracy; and
- deterministic replay differences.

A metric result describes the bounded benchmark only.

## Acceptance evidence

The pilot is technically demonstrated when reviewed evidence shows:

1. source bytes are unchanged;
2. transcript, structure, note, chunk, and index generations have immutable
   identities and complete derivation links;
3. physical PDF pages and printed labels remain distinguishable;
4. every evaluated source citation resolves to the expected page or span;
5. note-assisted retrieval resolves final support to source evidence;
6. equation candidates retain their representation and review status;
7. source-specific notation and known discrepancies remain retrievable;
8. all admitted figure and table records resolve to source evidence;
9. ranking and evidence-bundle replay is deterministic within the frozen
   policy;
10. deliberately unsupported requests return `INSUFFICIENT_EVIDENCE`;
11. no manuscript, note, or generated answer enters the source-evidence role;
12. problem material remains excluded unless the frozen pilot explicitly
    admits a separate corpus role;
13. generated-note validation or publication success does not promote it to
    reviewed-note or source-evidence status;
14. private inputs and payloads remain outside Git and public logs; and
15. failures, collisions, rejected candidates, and exclusions are preserved
    rather than silently omitted.

Completion does not accept component contracts, establish scientific
correctness, authorize bulk ingestion, or approve production deployment.

## Stop conditions

Stop the run and preserve evidence if:

- source identity changes;
- a required input or destination is symlinked;
- configured private storage cannot be resolved safely;
- an operation exceeds its declared bounds;
- source and curated corpus roles cannot be enforced;
- provenance or exact locators would be lost;
- a private payload would enter a public artifact;
- a generated-note target collides without exact replacement authority;
- an excluded problem-material class would enter ordinary retrieval;
- an effect has ambiguous completion; or
- required review or authority evidence is absent.

Ambiguous effects enter query-only reconciliation and are not automatically
retried.

## Artifact routing

| Artifact | Location |
|---|---|
| Pilot definition | This file |
| Component contracts and synthetic fixtures | Owning repositories |
| Private source and reviewed notes | Authorized private source locations |
| Immutable generations and indexes | Configuration-resolved private store |
| Run manifest, metrics, logs, and decisions | `state/runs/<run-id>/` |
| Mutable coordination | Parent and owner issues |
| Public completion summary | Sanitized owner record without private payloads |

## Required synthetic fixture coverage

Component owners should provide small public fixtures that exercise the
observable boundary without reproducing private textbook material. At minimum,
the fixture set should include:

- adjacent standard and conceptual example headings;
- a conceptual example after the last standard example in a chapter;
- two source locators with identical bytes but different origin names;
- physical page spans that differ from printed labels;
- a generated-note candidate with malformed JSON or LaTeX escaping;
- an incomplete final-answer section;
- a collision with an existing target and no replacement authority;
- an excluded problem-material record presented to ordinary retrieval; and
- a successful atomic publication followed by a failing hash-verification
  example.

Exact fixtures and conformance commands remain in their owning component
repositories. Real private documents supplement these fixtures but never
replace them.
