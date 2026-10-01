# PILOT-UC-02-01: Manuscript development

## Record status

- **Pilot ID:** `PILOT-UC-02-01`
- **Definition status:** Draft
- **Execution status:** Not authorized
- **Use case:**
  [UC-02](../use-cases/uc-02.evidence-grounded-manuscript-development.md)
- **Architecture:**
  [evidence-grounded long-form authoring](../architecture/v0/index.md#evidence-grounded-long-form-authoring)
- **Supporting control slice:**
  [citation-document control](../architecture/_system/citation-document-control/index.md)
- **Parent roadmap:** `RAG-ROADMAP-01`

This definition does not authorize source access, ingestion, model execution,
manuscript or bibliography modification, citation acceptance, publication, or
release.

## Objective

Demonstrate one lean, local, text-only authoring slice for a bounded
`ksdft2effmass` manuscript subsection. The author receives a short proposal
whose citation markers resolve to immutable evidence items from admitted
reference works, while missing, partial, conflicting, and deferred-modality
cases remain visible.

## Bounded scope

The pilot uses:

- one exact read-only manuscript revision and subsection;
- one author-supplied writing question;
- a small explicitly authorized reference set;
- canonical transcript blocks admitted through exact lineage and warning review;
- deterministic lexical retrieval with fixed bounds and per-work diversity;
- local inference without model tools;
- one paragraph or short-subsection proposal; and
- one small benchmark fixed before evaluation.

The manuscript context remains with the `ksdft2effmass` composition root. Search
receives only an evidence retrieval request containing a bounded query
representation, opaque target identity, optional work filters, and fixed bounds.

## Supporting citation-document control

A separately bounded control slice may prepare the private transcript evidence
used by readiness review. It does not expand the authoring pilot into a control
plane and it does not admit its output to Search.

For the initial monograph revision, the manuscript owner emits a complete
immutable snapshot whose acceptance evidence derives 122 distinct key groups,
221 rendered calls, 277 occurrences, 45 `\citationtodo` markers, and two
non-key source gaps. These values describe that snapshot only; they are not
format constants.

The control sequence is:

1. project the complete snapshot and exact References identity/availability
   evidence without rescanning TeX;
2. receive a PDF into private immutable Applications custody;
3. require a separate explicit **Process privately** intent/admission;
4. record a References-owned neutral source-document link;
5. synchronously extract and publish one deterministic document package;
6. register and expose the automated, unreviewed transcript by opaque document
   ID; and
7. stop without Search or authoring admission.

The control API returns only terminal success, failure, or an indeterminate
outcome requiring reconciliation. It has no workflow, queue, running, polling,
percentage, background-worker, automatic-retry, repair, or recovery claim. An
indeterminate outcome exposes no transcript-ready state. The dedicated browser
page presents owner state but creates none of it.

## Exclusions

The pilot does not include:

- direct manuscript or bibliography writes;
- a claim ledger, patch applier, or persistent review database;
- semantic, typed-equation, figure, or table retrieval;
- workflow orchestration or API/browser authoring review beyond the separately
  bounded citation-document control surface;
- remote model providers or model tools;
- extraction of shared generation behavior to `projectkoios-agent`;
- scientific, editorial, or citation acceptance by automation; or
- publication, submission, or deployment.

## Participating owners

| Owner | Pilot responsibility |
|---|---|
| `projectkoios` | Pilot definition and cross-repository architecture |
| `projectkoios-references` | Bibliographic authority status, observed assets and linkage, and access/rights evidence |
| `projectkoios-ingestion` | Extraction, canonical transcript, page/block lineage, transformations, warnings, and derivation audit |
| `projectkoios-applications` | Supporting private receipt, processing intent/admission, synchronous composition, package, and registry |
| `projectkoios-api` | Supporting control-only catalog, upload, process, and transcript transport |
| `projectkoios-web` | Supporting dedicated private citation-document control page |
| `projectkoios-search` | Immutable evidence items and deterministic lexical retrieval request/result behavior |
| `ksdft2effmass` | Citation snapshot, temporary composition root, target context, local generation, repository checks, and manuscript authority |
| Author or principal investigator | Purpose-specific source-use authorization and scientific/editorial acceptance |

Reusable owners never import `ksdft2effmass`. Passing technical checks does not
transfer author or principal-investigator authority.

## Required readiness evidence

Before an executable run is separately authorized, the pilot owner identifies:

1. the complete owner citation snapshot, exact manuscript revision, and selected
   span;
2. each bibliographic work's candidate or accepted authority status;
3. each observed asset and References-owned neutral work/document linkage;
4. any private-processing result separately from rights observations and
   explicit purpose-specific authoring-use authorization;
5. admitted transcript blocks with matching source identity, page/block
   lineage, retained extraction or transformation mapping, and warning details;
6. deterministic evidence-item, corpus, index, and ranking identities;
7. fixed query, filter, item, per-work, warning, and aggregate-text bounds;
8. the local model and prompt identities; and
9. benchmark questions and expected evidence dispositions.

Source admission reports `REFERENCE_IDENTITY_UNRESOLVED`,
`DISCOVERY_INCOMPLETE`, `ASSET_INACCESSIBLE`, `RIGHTS_UNKNOWN`,
`USE_NOT_AUTHORIZED`, or `INGESTION_MISSING` distinctly. None is a Search
insufficiency outcome.

## Procedure

1. Verify that manuscript and source inputs are unchanged and read-only. Treat
   any control-slice receipt, link, ingestion result, and transcript as separate
   evidence that grants no authoring admission by itself.
2. Admit selected works, assets, and transcript blocks through the source and
   transcript gates.
3. Build the deterministic lexical index over admitted reference evidence only.
4. Retain bounded manuscript context locally and construct one evidence
   retrieval request with opaque target identity.
5. Search orders eligible evidence by lexical score then stable evidence-item
   identity, retaining the strongest item and filling remaining slots under a
   per-work cap.
6. Return one evidence retrieval result with ordered ranked items, applied
   bounds, omissions, warnings, and exactly one outcome:
   `EVIDENCE_AVAILABLE`, `INSUFFICIENT_EVIDENCE`, `INVALID_REQUEST`, or
   `INFRASTRUCTURE_FAILURE`.
7. Give the local model the bounded target context and retrieval result
   separately.
8. Generate one proposal whose markers map to stable evidence-item identities
   and whose unsupported, partial, conflicting, or deferred claims remain
   explicit.
9. Emit an accepted canonical citekey only when References supplied one;
   otherwise report the bibliographic gap and candidate/prospective status.
10. Resolve quotations to retained extraction or an explicit transformation
    mapping, retaining page evidence and warnings.
11. Optionally run only repository-local structural checks implemented at pilot
    time against a staged copy.
12. Present the proposal and evidence to the author, then stop without writing
    the manuscript or bibliography.

## Small benchmark

Freeze these cases before evaluation:

- directly supported and paraphrased needs;
- a partially supported claim;
- conflicting works;
- a missing intended work;
- an equation-oriented question answerable from retained text;
- an equation request requiring deferred modality; and
- a deliberately zero-hit lexical request.

Inspect evidence recall within the fixed bound, locator and retained-quotation
resolution, deterministic ordering, citation-to-item mapping, per-work
diversity, visible unsupported material, closed outcome classification, and the
author's usefulness and revision assessment.

## Acceptance evidence

The pilot is technically demonstrated only when reviewed evidence shows:

1. source, manuscript, and bibliography bytes remain unchanged;
2. source/use admission and transcript gates fail closed;
3. manuscript and generated text cannot become reference evidence;
4. every selected item resolves to one work/asset linkage and exact retained
   extraction with page/block lineage and warnings;
5. ordering and multiple-work selection replay deterministically;
6. every proposal marker maps only to supplied evidence items;
7. candidate citekeys are never emitted as accepted citations;
8. missing, partial, conflicting, zero-hit, invalid, infrastructure, and
   deferred-modality cases remain distinct;
9. the model receives no tools and no content leaves the local boundary;
10. optional structural checks are described only as software checks;
11. no private path or protected excerpt enters public output; and
12. the author can assess the proposal without hidden session context.

Completion does not accept a citation, approve manuscript prose, establish
scientific validity, authorize a write, or justify shared-agent extraction.

## Stop conditions

Stop when source or use authority is unclear, evidence cannot resolve to
retained extraction, selected warnings require unresolved page inspection,
target text would leave its approved boundary, retrieved content could influence
tools, the target changed, an equation representation is required, or a shared
abstraction still has only one demonstrated consumer.

## Artifact routing

| Artifact | Location |
|---|---|
| Pilot definition | This file |
| Architecture and use case | `projectkoios` living documentation |
| Citation snapshot, manuscript, target context, proposal, and author assessment | `ksdft2effmass` or its authorized private storage |
| Reference observations and neutral linkage | `projectkoios-references` evidence boundary |
| Extraction and transcript evidence | `projectkoios-ingestion` evidence boundary |
| Private receipt, processing intent/result, package, and registry | `projectkoios-applications` control boundary |
| Control transport and browser presentation | `projectkoios-api` and `projectkoios-web` |
| Evidence items, retrieval result, and index | `projectkoios-search` evidence boundary |
| Synthetic fixtures and conformance tests | Applicable owner repository when separately authorized |
