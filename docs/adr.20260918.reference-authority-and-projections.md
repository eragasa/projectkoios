# ADR20260918: Reference authority and projection architecture

## Status

Accepted

Accepted by the Project Koios operator for
[`REFERENCES-ARCHITECTURE-01`](https://github.com/eragasa/projectkoios/issues/3)
on 2026-09-18. This decision does not accept a component contract, authorize
implementation or migration, or promote any reference.

## Context

The reference prototype carries overlapping identity, access, rights, review,
collection, and processing state in BibLaTeX, CSV, JSON, SQLite, asset and
acquisition manifests, collection-reconciliation outputs, and ingestion
workspace files. Without an authority model, an import or projection can appear
to accept a candidate, overwrite historical evidence, or claim another
repository's decision authority.

The architecture must preserve historical observations and human decisions,
allow local query and export, and keep component boundaries explicit. In
particular, references must consume ingestion-owned evidence without treating
an ingestion workspace layout as an API.

## Decision

Project Koios uses immutable, content-addressed records as historical authority
for reference observations, evidence, and human decisions. SQLite is a
rebuildable working projection of those records. CSV, JSON, BibLaTeX, and
Markdown are deterministic import or export projections; a file format is not
authority merely because it is human-readable or tracked in Git.

Authority is federated by domain. A content hash establishes record integrity
and identity, not truth, actor authenticity, scientific support, rights
clearance, or publication permission. Those meanings come from the record
type, its evidence, and the authority of its producer or human actor.

### Authoritative record rules

An authoritative record must:

- have a stable type and content-derived identity;
- identify its schema or contract version and producing implementation;
- identify exact upstream records or source bytes;
- preserve source-verbatim evidence separately from normalized proposals;
- represent unknown, not observed, unresolved, and not applicable distinctly;
- be append-only once published; and
- use an explicit supersession or correction record rather than mutation.

A human decision record must additionally identify the actor, the actor's
authority and scope, the evidence considered, the decision, rationale, and any
record it supersedes. A timestamp may be retained as evidence, but identity and
replay must not depend on a newly generated replay time.

The actor provenance must be verified by the repository process that admits the
decision. Content addressing alone does not authenticate an actor.

### Identity model

The reference domain has distinct identities and types for:

1. **source observations** — verbatim bibliography entries, provider responses,
   citation occurrences, file observations, and other bounded observations;
2. **reference candidates** — normalized proposals assembled from identified
   observations and discrepancies; and
3. **canonical references** — identities created only by an actor-provenanced
   human promotion decision.

A candidate identifier is never a canonical reference identifier. A proposed
citekey is candidate metadata and remains visibly noncanonical. Importing
BibLaTeX, matching a filename, locating a PDF, joining a citation graph, adding
a collection row, or passing a technical check cannot create a canonical
reference.

For an accepted reference object, the convention
`BibLaTeX key == Markdown basename == PDF basename` remains a naming
projection. It does not establish identity acceptance. Promotion, merge, split,
alias creation, or citekey migration requires its own actor-provenanced decision
record. The concrete schemas and encodings remain owned by
`projectkoios-references` and require separate contract review.

### Authority and projection matrix

| State category | Authoritative owner and record | Projection and authority limit |
|---|---|---|
| Source bibliography or metadata observation | `projectkoios-references` owns an immutable observation bound to exact source content, locator, revision evidence, and parser or provider identity. The source repository or external provider remains authoritative for its own current content. | Imported BibLaTeX, provider cache rows, and catalog rows are views of what was observed. They do not establish normalized truth or acceptance. |
| Normalized metadata and discrepancies | `projectkoios-references` owns immutable normalization proposals and discrepancy records linked to source observations. A human resolution is a separate actor-provenanced decision. | Last writer, provider preference, or export order cannot resolve a discrepancy. |
| Reference candidate | `projectkoios-references` owns the candidate identity, candidate lifecycle evidence, and proposed noncanonical names. | Candidate manifests, graph CSV, and discovery reports may project candidate state. They cannot emit a canonical identity. |
| Canonical reference identity and naming | `projectkoios-references` owns the canonical identity and naming rules; a designated human reference curator owns promotion and identity-migration decisions. | SQLite rows, accepted-looking filenames, or imported keys cannot stand in for the promotion decision. |
| Citation occurrence and citation graph evidence | `projectkoios-references` owns immutable observations bound to the exact source and supported parser scope. | Citation closure proves only the bounded key-resolution observation. It does not establish relevance, support, or manuscript acceptance. |
| Project Koios review-collection membership | `projectkoios-references` owns immutable membership observations and actor-provenanced curation decisions for its review collections. | Membership is neither canonical promotion nor a claim about the source's scientific value. |
| Source-project bibliography and manuscript use | The repository that owns the source project or manuscript owns its bibliography content and citation-use decisions through its designated human author or maintainer. | References may observe and report exact-revision use. It must not rewrite or accept use on the source repository's behalf. |
| Asset discovery and byte identity | `projectkoios-references` owns bounded discovery, match, hash, format, and version observations for reference assets. | A filename, score, hash, or local possession does not prove work identity, canonical attachment, completeness, or rights. |
| Asset-to-reference attachment | A designated human reference curator owns the attachment or rejection decision, recorded against exact asset and candidate or canonical identities. | Materialization and basename projections follow the decision; they cannot create it. |
| Acquisition and access state | `projectkoios-references` owns immutable acquisition and access observations, including coverage and failures. The source or resource owner retains access-control authority. | Lawful possession, local processability, public access, and absence are separate evidence states. An observation does not grant access or imply redistribution or publication permission. |
| Rights evidence | `projectkoios-references` owns source-attributed rights observations and unresolved discrepancies. | Rights fields are evidence, not a general legal or publication decision. |
| Action-specific rights decision | The repository performing acquisition, quotation, redistribution, manuscript use, or publication owns the action record; its designated human rights authority owns the decision. | No reference, ingestion, search, or automation status grants that permission. |
| Extraction and transcript state | `projectkoios-ingestion` owns source-byte identity, extraction, transcript, audit, and processing evidence and publishes the versioned evidence contract consumed by other repositories. | References stores only the exact producer evidence it consumed and its own linkage observation. It must not inspect or encode ingestion's private workspace layout. |
| Reference-side ingestion linkage | `projectkoios-references` owns the immutable observation that a specific ingestion evidence record was linked to a specific asset identity. | A recorded passing audit is not independent revalidation, proofreading, scientific acceptance, or publication suitability. |
| Reading and reference-curation decisions | `projectkoios-references` owns actor-provenanced reading and reference-curation records. Automated processors own only their technical outcomes. | One replaceable `review_status` scalar must not combine processing, reading, claim support, canonical acceptance, or manuscript use. |
| Claim support and scientific relevance | The owning research repository, such as `projectkoios-research` or an independent scientific application, owns evidence records; its designated human scientific authority owns acceptance. | References and search may propose locators or retrieval evidence but cannot accept scientific support. |
| Manuscript use | The manuscript-owning repository owns the use record; its designated human author owns the decision to cite, quote, or rely on a reference in that manuscript. | Canonical identity, local access, technical validation, and claim locators do not authorize manuscript use. |
| Publication | The publication artifact owner owns the publication record; its designated human publication authority owns release or submission decisions. | Manuscript use, canonical identity, and rights evidence do not by themselves authorize publication. |
| Architecture acceptance | `projectkoios` owns cross-repository architecture records; the Project Koios operator owns acceptance. | A literature citation or passing component test is evidence, not architecture acceptance. |
| SQLite working catalog | `projectkoios-references` owns its schema and deterministic reducer, but not historical authority in the database itself. | The database is disposable and rebuildable from identified authoritative records. Backup and migration may preserve convenience, not create authority. |
| CSV, JSON, BibLaTeX, and Markdown outputs | The producing repository owns deterministic projection semantics. | Each output identifies exact authoritative inputs, schema or contract, generator, configuration, ordering, and replay behavior. Editing an output does not mutate its inputs. |

### Projection and replay direction

The allowed direction is:

```text
bounded external source or owner-produced evidence
    -> immutable source observation
    -> immutable candidate, linkage, or human decision record
    -> deterministic reducer
    -> SQLite working projection and CSV/JSON/BibLaTeX/Markdown views
```

Imports parse a bounded external file into a new immutable observation. They do
not overwrite prior records or silently convert the imported format into
historical authority. Reimport of identical content is idempotent. Different
content creates a new observation or an explicit conflict.

Every projection must identify:

- the complete ordered set of authoritative input identities;
- reducer, schema or contract, generator, and configuration versions;
- deterministic ordering and normalization rules;
- exclusions, unsupported values, and unresolved discrepancies; and
- whether exact replay is expected to be byte-identical.

Identical replay is byte-identical where the projection contract makes that
claim. A different existing immutable destination fails closed. A projection
may be deleted and rebuilt without historical loss. An edited projection can be
reimported only as a new source observation or explicit decision proposal; it
never updates authoritative history in place.

SQLite may contain indexes, joins, resolved current-state views, and cached
provider data. Every authority-bearing value in it must retain or resolve to the
exact authoritative record identity. Database schema migration must not
silently relabel, discard, or upgrade the authority of those records.

### Candidate manifests and collection reconciliation

The Proposed
[`projectkoios.references.candidate-manifest`](https://github.com/eragasa/projectkoios-references/blob/master/docs/contracts/reference-evidence.md#contract-metadata-candidate-manifest)
contract is the intended cross-repository projection of one reference
candidate's bibliographic observations, normalized proposals, discrepancies,
access evidence, and rights evidence. This ADR establishes the authority rules
that such a contract must respect. It does not accept version `0.1.0`, assert
implementation conformance, or grant promotion authority.

The current collection-reconciliation record is a provisional,
owner-internal, collection-scoped evidence projection. It combines exact-scope
bibliography observations, collection rows, citation closure, asset and
coverage observations, and recorded ingestion status to report the state of a
bounded collection. Its seed citekeys remain source observations or proposed
names unless a separate canonical decision is linked.

Neither record subsumes the other:

- a candidate manifest describes one candidate and can be an identified input
  to future collection reconciliation;
- a reconciliation package describes a bounded collection and may report a
  candidate's presence or unresolved state; and
- neither converts collection membership, asset presence, citation use, or
  processing status into canonical acceptance.

A future authoritative reconciliation package must bind every input and output,
including citation closure and producer evidence, under one complete immutable
package identity. That requirement selects direction and provenance, not a
component schema. The component owner must still propose, review, and accept
its contracts separately.

### Ingestion dependency direction

`projectkoios-ingestion` is the producer of extraction and transcript evidence.
It must publish a versioned, content-addressed producer contract or projection
that binds at least source-byte identity, extraction identity, transcript
generation and status, audit identity and status, and producer versions.

`projectkoios-references` is a consumer through an adapter owned by the
references repository. It may retain the exact producer record and publish its
own source-asset linkage observation. It must not construct ingestion paths,
read fixed private filenames, or infer status from private workspace layout.

```text
projectkoios-ingestion evidence contract
    -> projectkoios-references consumer adapter
    -> immutable asset-to-processing linkage observation
    -> collection/catalog projections
```

Existing Draft or Proposed ingestion contracts remain Draft or Proposed. This
decision mandates the owner-contract boundary but does not select or accept a
particular producer contract. Materially affected producer and consumer owners
must review any proposed boundary before contract acceptance under the shared
contract-governance policy.

## Consequences

- Historical observations and decisions survive catalog rebuilds and projection
  changes.
- Candidate and canonical reference identities cannot share an ambiguous API.
- Canonical promotion and identity migration require inspectable human
  provenance.
- SQLite remains useful for local joins, query, and current-state views without
  becoming irreplaceable history.
- Every public or private projection can disclose exactly which evidence it
  represents and how to replay it.
- References and ingestion can evolve their private layouts independently.
- Rights, access, scientific support, manuscript use, architecture acceptance,
  and publication remain separate authorities.
- Component repositories must define schemas, reducers, migrations, fixtures,
  and conformance evidence consistent with this decision before claiming a
  reusable architecture.

## Alternatives considered

### Make SQLite the source of truth

Rejected. A mutable database can erase provenance, conflate imported and
accepted state, and cannot by itself expose a reviewable historical decision
chain.

### Make tracked BibLaTeX or CSV canonical

Rejected. These formats are valuable projections but cannot represent all
source observations, discrepancies, decision provenance, assets, coverage, and
cross-repository processing evidence without ambiguous overwrite semantics.

### Treat immutable manifests as one undifferentiated authority

Rejected. Content addressing protects identity and replay, but the producer and
record type still determine whether a record is an observation, proposal,
technical outcome, or human decision.

### Let references inspect ingestion workspace files

Rejected. Private storage layout is not a cross-repository API and cannot prove
that observed processing state derives from the currently linked source bytes.

## Non-decisions and authorization boundary

This ADR does not:

- accept the Proposed candidate-manifest, clean-transcript, or another component
  contract;
- choose concrete record schemas, serialization encodings, or SQLite migrations;
- claim conformance for the current reference prototype or reconciliation
  outputs;
- promote, merge, split, rename, acquire, attach, or publish a reference or
  asset;
- establish scientific support, manuscript use, rights clearance, or
  publication permission; or
- authorize component implementation, migration, commit, push, release, or
  `REF-PROVENANCE-01` execution.
