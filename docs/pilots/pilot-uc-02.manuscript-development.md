# PILOT-UC-02-01: Manuscript development

## Record status

- **Pilot ID:** `PILOT-UC-02-01`
- **Definition status:** Draft
- **Execution status:** Not authorized
- **Use case:**
  [UC-02](../use-cases/uc-02.evidence-grounded-manuscript-development.md)
- **Architecture:**
  [evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md)
- **Parent roadmap:** `RAG-ROADMAP-01`

This definition does not authorize manuscript or bibliography modification,
citation acceptance, source acquisition, contract acceptance, publication, or
release.

## Objective

Demonstrate that Project Koios can use a read-only scientific manuscript as
query material, retrieve source-diverse reference evidence, produce
source-linked citation or drafting proposals, and support append-only human
review without modifying the manuscript.

## Bounded scope

The pilot uses:

- one immutable manuscript revision;
- one bounded manuscript section or appendix;
- its current bibliography identity;
- an authorized local reference corpus;
- a reviewed private claim and citation benchmark;
- equation-aware review for applicable claims; and
- a laptop-local review interface.

The manuscript is query material. Only admitted reference sources may provide
literature evidence.

## Exclusions

The pilot does not include:

- manuscript or bibliography writes;
- automatic citation acceptance;
- automatic acquisition of absent sources;
- scientific-validity approval;
- publication or submission;
- use of manuscript text as evidence for itself;
- feedback of generated prose into the reference corpus; or
- replacement of calculation provenance with literature citations.

## Participating owners

| Owner | Pilot responsibility |
|---|---|
| `projectkoios` | Pilot definition and cross-repository architecture |
| `projectkoios-ingestion` | Exact manuscript parsing and admitted source processing |
| `projectkoios-search` | Corpus-role filtering, retrieval, ranking, and evidence bundles |
| `projectkoios-references` | Bibliographic identity, key presence, acquisition, and rights evidence |
| `projectkoios-agent` | Claim-query, alignment, citation, and drafting proposals |
| `projectkoios-api` / `projectkoios-web` | Local citation and drafting review interface |
| `projectkoios-research` | Purpose-specific scientific judgments |
| Deployment owner | Private composition, storage, authorization, and reconciliation |

The manuscript's owning repository retains manuscript authority.

## Input classes

### Private inputs

- exact read-only manuscript bytes;
- bibliography and citation-key inventory;
- claim spans and original TeX;
- reference evidence and source locators;
- private benchmark judgments;
- prior review decisions; and
- local runtime configuration.

### Public inputs

- use-case and architecture records;
- component contract identifiers;
- synthetic claim, citation, equation, and revision fixtures; and
- public conformance commands.

No private manuscript or source excerpt is copied into this definition.

## Required readiness evidence

Before an executable run is requested, the pilot owner records:

1. manuscript identity and read-only guard;
2. bibliography identity;
3. reference-corpus and index identities;
4. exact corpus-role enforcement behavior;
5. decision-store identity and revision semantics;
6. API-only browser access to private data;
7. equation rendering and original-TeX preservation behavior;
8. private benchmark schema, metrics, and frozen thresholds;
9. privacy review; and
10. deployment ownership for every external effect.

## Procedure

### Phase 0: Freeze the pilot revision

1. Identify the bounded manuscript revision and selected section.
2. Record participating contract and component revisions.
3. Freeze the private benchmark schema, metrics, and thresholds.
4. Record the reference corpus and exclusions.
5. Confirm that the manuscript will remain read-only.

### Phase 1: Parse the manuscript exactly

1. Read the manuscript through an authorized adapter.
2. Verify and record its content identity.
3. Preserve original text, TeX, equations, labels, citation commands, and
   source spans.
4. Emit bounded section, paragraph, equation, claim, and citation candidates.
5. Mark automated claim identification and classification
   `AUTOMATED_UNREVIEWED`.
6. Assign every manuscript unit the `query_material` role.

### Phase 2: Establish bibliography state

1. Record every existing citation key without modifying the bibliography.
2. Resolve available keys to bibliographic and source identities.
3. Distinguish present keys, absent keys, unresolved entries, and unavailable
   sources.
4. Preserve duplicate or conflicting bibliographic findings.

### Phase 3: Build reviewed information needs

The private benchmark includes:

- uncited literature claims;
- correctly cited claims;
- partially supported claims;
- equation-oriented claims;
- source-specific conventions;
- manuscript-derived calculations;
- missing bibliography keys;
- intended sources absent from the corpus;
- conflicting sources; and
- deliberately unsupported claims.

Each information need remains linked to the exact manuscript revision and
source span.

### Phase 4: Retrieve reference evidence

1. Execute retrieval with `corpus_role = reference` for final support.
2. Permit curated-note discovery only when final candidates resolve back to
   reference evidence.
3. Exclude manuscript text, generated prose, prior model answers, and citation
   proposals from the evidence corpus.
4. Diversify candidate results by source before admitting repeated passages
   from one source.
5. Return bounded evidence bundles with exact pages, spans, ranks, warnings,
   and truncation information.
6. Record absent or inadequate support as `INSUFFICIENT_EVIDENCE`.

### Phase 5: Produce proposals

For each reviewed claim or writing need, emit a proposal containing:

- manuscript revision and exact span;
- claim or writing-need identity;
- candidate reference identities;
- proposed citation keys and key-presence status;
- exact supporting source locators;
- relevant equation, figure, or table references;
- source and extraction warnings;
- supported and unsupported claim portions; and
- an explanation of the proposed relationship.

A drafting proposal may suggest prose or organization, but each
literature-dependent statement remains linked to evidence-bundle entries.

### Phase 6: Review locally

1. Present exact manuscript context and original TeX.
2. Render equations as review aids without replacing original TeX.
3. Present candidate source pages or spans and bibliographic state.
4. Display warnings, corpus roles, proposal status, and prior decisions.
5. Record append-only decisions bound to the manuscript identity.
6. Do not modify the manuscript or bibliography.

### Phase 7: Revision and replay

1. Re-run the same requests against the same manuscript and index identities.
2. Verify deterministic candidate and evidence-bundle behavior.
3. Introduce a new synthetic or authorized manuscript revision.
4. Confirm that prior decisions remain bound to the old revision.
5. Require explicit carry-forward or re-review rather than automatic reuse.

## Metrics

Metric definitions and thresholds are frozen before benchmark execution. The
pilot records at least:

- reference Recall@k and mean reciprocal rank;
- exact-locator accuracy;
- citation-key presence accuracy;
- source-diversity behavior;
- partial-support detection;
- unsupported-claim detection;
- insufficient-evidence accuracy;
- manuscript self-retrieval count;
- invalid or invented locator count;
- stale-decision application count; and
- deterministic replay differences.

A retrieval score is not a citation-acceptance decision.

## Acceptance evidence

The pilot is technically demonstrated when reviewed evidence shows:

1. manuscript and bibliography bytes remain unchanged;
2. every manuscript unit is query material rather than reference evidence;
3. no manuscript passage is returned as support for itself;
4. every citation proposal resolves to reference evidence and an exact locator;
5. note-assisted discovery resolves final support to reference evidence;
6. calculated and literature claims remain distinct;
7. missing keys, missing sources, conflicts, and partial support remain visible;
8. original TeX remains available beside every rendered equation;
9. unsupported requests return `INSUFFICIENT_EVIDENCE`;
10. decisions are append-only and manuscript-revision-bound;
11. generated prose does not enter the reference corpus;
12. private manuscript, source, benchmark, and review payloads remain outside
    public artifacts; and
13. rerunning the frozen inputs reproduces retrieval and proposal identities
    within the documented deterministic boundary.

Completion does not accept a citation, approve manuscript prose, establish
scientific validity, or authorize a manuscript change.

## Stop conditions

Stop the run and preserve evidence if:

- the manuscript changes after the guarded identity check;
- a write to the manuscript or bibliography is attempted;
- corpus roles cannot prevent self-citation;
- exact manuscript or source spans would be lost;
- a proposal invents a source identity or locator;
- private text would enter a public log or fixture;
- decision revision binding fails;
- required source access or rights evidence is absent; or
- an external effect has ambiguous completion.

Ambiguous effects enter query-only reconciliation and are not automatically
retried.

## Artifact routing

| Artifact | Location |
|---|---|
| Pilot definition | This file |
| Synthetic claim and citation fixtures | Owning component repositories |
| Manuscript and bibliography | Authoritative application repository or authorized private location |
| Private claim benchmark and evidence bundles | Configuration-resolved private store |
| Review database, reports, metrics, and logs | `state/runs/<run-id>/` |
| Proposed patch artifact | Private store; never applied without separate authority |
| Research judgment | `projectkoios-research` or application-owned record, as applicable |
| Mutable coordination | Parent and owner issues |
| Public completion summary | Sanitized record without private text or locators |
