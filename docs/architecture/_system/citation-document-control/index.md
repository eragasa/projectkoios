# Citation-document control

## Status and authority

This page is the current cross-repository product architecture for the private
citation-document control surface. It supports the `ksdft2effmass` manuscript
phase of [UC-02](../../../use-cases/uc-02.evidence-grounded-manuscript-development.md)
without changing scientific, editorial, rights, Search, or publication
authority.

The first slice is authorized as a local control-plane implementation. It uses
one current canonical prototype shape. It does not create a numbered format,
compatibility promise, migration, contract acceptance, source-use permission,
or permission to process any particular PDF.

## Goal and bounded slice

The control surface lets an operator:

1. inspect a complete immutable snapshot of every rendered manuscript citation;
2. distinguish bibliography identity, document availability, neutral linkage,
   private processing, transcript availability, Search admission, and human
   acceptance;
3. upload a PDF into private immutable receipt custody;
4. separately authorize and request bounded private technical processing;
5. receive one synchronous terminal success, failure, or indeterminate
   outcome; and
6. inspect a resulting automated, unreviewed transcript through the existing
   transcript reader.

Upload never starts processing. Technical processing never admits material to
Search or authoring evidence. The first slice has no durable queue, scheduler,
worker, polling protocol, progress record, or retry claim.

## Current manuscript snapshot evidence

The initial acceptance fixture is an owner observation of the monograph at
repository revision
`7bd913151f7e61ed2bdba593df920be36573b502`. Its 34 TeX files and one
bibliography file have aggregate snapshot SHA-256
`2778bb8907d0364fc6be0b23e4d65ccb80f04c0ccf228bea4ff5e770bc17d2b2`.
The observation reports:

- 122 distinct rendered citation keys;
- 221 rendered citation calls;
- 277 key occurrences;
- 45 `\citationtodo` markers whose generated citations remain represented; and
- two non-key source gaps.

These values are acceptance evidence for that exact snapshot, not constants,
limits, or expected values for another revision. They do not become API or
References literals. A changed source revision must produce a newly identified
snapshot and newly derived counts.

The existing generic citation-closure observation is incomplete because it
fails closed at an unsupported `\def`. It cannot substitute for the complete
owner snapshot. Historical prose audits, ignored TeX products, and independent
regular-expression scans are not inventory authority.

## Target-owned citation snapshot

`ksdft2effmass` owns deterministic manuscript parsing and emits the complete
snapshot. References, Applications, API, and Web never rescan TeX.

The immutable snapshot binds:

- exact repository revision, normalized composition root, and bibliography;
- every graph-reachable source file by root-relative POSIX path, byte size, and
  SHA-256;
- ordered include instances, retaining an instance ordinal even when one file
  is currently included only once;
- rendered citation calls and key occurrences, including direct citations,
  `\eqincite` expansion, and `\citationtodo` expansion;
- literal case-sensitive keys, key ordinals, command kinds, and origin kinds;
- owner-ordered key groups that retain every occurrence without deduplication;
- exact bibliography-entry order and content lineage; and
- separately identified non-key source gaps.

An occurrence identity binds the snapshot, include instance, source file,
UTF-8 key byte span, command kind, key ordinal, and origin. A display locator is
the root-relative path plus one-based line and column. Immutable validation uses
the source-file digest and UTF-8 byte span. Neither representation contains an
absolute path or manuscript excerpt.

Each target bibliography entry has a target-owned opaque identity and binds the
bibliography path, digest, size, zero-based entry index, literal key, exact byte
span, and entry-content digest. The target does not fabricate a References
observation identity. References owns a separate exact binding from that entry
and lineage to a replay-validated source-bibliography observation.

The parser supports only citation semantics it can prove. Exact harmless
command definitions may be parsed or allowlisted. Unknown citation-capable
macro expansion, an unbounded graph, malformed UTF-8, changed bytes, duplicate
identities, or inconsistent derived counts makes the snapshot incomplete and
blocks the catalog.

A cross-process handoff uses one explicitly operator-supplied, target-owned
artifact containing the complete snapshot Result. The target owns its canonical
unversioned JSON codec, complete encode/decode shape, bounds, and replay rules.
The codec adds no runtime timestamp, machine-local root, protected excerpt,
downstream identity, or numbered prototype format. No consumer parses TeX,
BibLaTeX, or an ad hoc test fixture in place of that codec.

After decoding and replay, a target-side one-way Project Koios binding maps the
complete owner Result to the References-neutral target records. It preserves the
owner snapshot, occurrence, group, bibliography-entry, source-gap, content, and
locator identities while omitting only owner-internal detail that the neutral
boundary does not consume. The target binding may call reusable References
contracts; References, Applications, API, and Web do not import target parsing
or rescan target sources. Artifact selection is explicit: there is no default,
repository search, newest-file selection, or committed generated runtime
snapshot requirement.

## References projection and neutral linkage

References consumes the target snapshot, exact bibliography-entry bindings, a
replayed identity projection, bounded availability observations, and neutral
source-document links. It does not interpret TeX, private-processing policy,
ingestion state, Search state, or human acceptance.

The projection groups once by literal citekey in deterministic owner order and
retains every owner occurrence ID. Accepted active canonical names and active
aliases resolve before candidates. Otherwise one exact-entry candidate resolves
as a noncanonical candidate, multiple candidates remain ambiguous, and no
candidate remains unresolved. No filename, title, DOI similarity, or first
match establishes identity.

A neutral source-document link binds one exact projection item and identity
item to one content-identified PDF plus availability evidence and an opaque
pre-effect intent ID. The intent ID is lineage only: References neither imports
Applications nor infers processing authorization from it. Exact replay is
idempotent. Competing content identities remain ambiguous rather than using
last-write-wins behavior.

`available-linked` means only that exact neutral attachment exists. It does not
mean canonical identity, verified rights, processing admission, ingestion,
Search admission, authoring fitness, scientific support, or human review.

Availability remains evidence, not an absence inferred from missing input. If
References has no complete bounded availability observation for a key, the
projection reports `not-evaluated`; it must not report `not-observed`, label the
document missing, or enable PDF upload. A private receipt contributes positive,
explicitly incomplete availability evidence and cannot retroactively prove a
complete pre-receipt observation. Production bibliography bindings, identity
projection, availability evidence, and final projection remain
References-owned dependent inputs.

## Orthogonal control projection

The catalog preserves these dimensions independently:

| Dimension | Values or authority |
|---|---|
| Snapshot | complete owner snapshot, otherwise catalog unavailable |
| Bibliography membership | `defined`, `undefined`, `not-evaluated` |
| Citation identity | exact References projection status and every matching item |
| Document | `not-evaluated`, `not-observed`, `available-unverified-linkage`, `available-linked`, `ambiguous`, `inaccessible` |
| Private receipt | not received or privately received |
| Private-processing admission | not authorized or explicitly authorized for the bounded local intent |
| Technical ingestion | `NOT_REQUESTED`, `SUCCEEDED`, `FAILED`, or `INDETERMINATE` |
| Transcript | `NOT_AVAILABLE` or `AUTOMATED_UNREVIEWED` |
| Search indexing | `NOT_EVALUATED` in this slice |
| Human/scientific acceptance | `NOT_EVALUATED` until a human decision exists |

Only `not-observed`, based on a complete bounded observation, may be presented
as “Document missing.” `not-evaluated` means that no owner evaluation was
supplied. A successful ingestion does not alter document linkage, Search, or
human status. Search does not persist `NOT_EVALUATED` and the interface does not
claim `NOT_INDEXED`; Search has not evaluated these documents.

The two current non-key source gaps are separate catalog entities. They are not
undefined bibliography keys and are not assigned invented citekeys.

## Receipt and explicit private processing

Applications owns private receipt custody, pre-effect intent composition,
processing-admission evidence, synchronous ingestion composition, deterministic
package publication, and the bounded document registry.

Receipt accepts one bounded PDF as untrusted bytes, computes exact content
identity and byte size, and publishes immutable private custody atomically. A
receipt proves only what bytes were received. It does not link a work, authorize
processing, verify rights, ingest content, admit evidence, or record review.

A separate operator action, displayed as **Process privately**, creates an
explicit bounded local-processing admission and pre-effect intent. The intent
binds the exact snapshot and projection item, receipt, resolved candidate or
accepted identity, effective local policy, configured local-operator authority
assertion or decision identity, and idempotency semantics. The first local slice
does not claim authenticated remote-user identity or independent proof of the
assertion. It grants only the requested private technical effect. Unknown or
unaccepted redistribution and authoring rights remain unchanged.

The identity graph is acyclic:

```text
private receipt
    -> Applications pre-effect intent and processing admission
    -> References neutral source-document link
    -> Applications final ingestion request
    -> Ingestion extraction result
    -> Applications document package and registry entry
    -> transcript projection
```

The final ingestion request consumes both the intent and link. A References link
must never bind a final workflow or request identity that itself depends on the
link.

## Synchronous execution and transcript registry

The first slice executes one bounded request synchronously:

```text
verify immutable receipt bytes
    -> extract with the Ingestion owner
    -> build and publish one deterministic Applications document package
    -> register the completed package explicitly
    -> project its transcript
    -> return terminal success, failure, or indeterminate outcome
```

Applications uses the deterministic document-package path, not the legacy
corpus runner. The registry is bounded, explicit, and replay-validated; it never
scans for package roots. It maps opaque document identities to authorized
package roots inside the trusted runtime boundary without returning a path.

The catalog may retain the latest terminal result. `INDETERMINATE` means that a
partial or unknown publication effect requires reconciliation; it makes no
transcript-ready claim and permits no automatic retry, overwrite, repair, or
promotion to `FAILED`. While an HTTP request is open, the browser may display
local pending text, but that is not a durable `QUEUED` or `RUNNING` state.
Reload does not promise recovery. A later durable
asynchronous slice requires separately accepted Workflow planning, dispatch,
claim, lease, execution, retry, and recovery behavior before API or Web exposes
such status.

Completed documents reuse the existing canonical reader:

```text
GET /transcripts/{document_id}
```

A catalog item carries only a nullable opaque `transcript_document_id`. There is
no citation-nested transcript, API-supplied navigation URL, filesystem path, or
client-derived page identity. Owner page order, zero-based page index, one-based
physical page, nullable printed label, exact escaped text, and
`AUTOMATED_UNREVIEWED` status remain intact.

## Cross-process runtime composition

The direct in-process provider injection remains the narrow executable seam.
Standard cross-process startup depends first on the target artifact and binding
above and then on a replay-valid References projection with explicit complete
availability evidence where missing-document behavior is required.

Applications owns the later closed, unversioned runtime manifest and typed
runtime bundle. Its loader receives one explicit operator-selected
configuration path, binds only deployment-provisioned private roots, and
composes the existing custody, registry, and synchronous service. It neither
creates deployment roots nor scans for artifacts, repositories, packages, or
newest state. Deployment keeps the manifest and roots outside Git worktrees and
supplies them explicitly.

API owns only optional control-profile activation, one explicit Applications
configuration path, a statically named owner-composition call, provider
adaptation, and injection. An unconfigured control profile retains the fixed
sanitized unavailable response. Configured but missing, malformed, unsafe, or
incompatible owner state fails startup with a fixed non-sensitive error instead
of falling back to fixtures or partial service. A public profile never loads the
private capability. Browser behavior and ownership do not change.

The Applications manifest/bundle, References production projection artifact,
and API startup bridge are dependent milestones, not implementation authority
created by this page. They require their own owner validation and separate
implementation authorization.

## Control API and Web

The API surface is control-only and remains local/private until a separately
accepted operator authentication and authorization boundary exists. Its first
slice is:

```text
GET  /citation-documents
POST /citation-documents/{item_id}/source
POST /citation-documents/{item_id}/process-private
GET  /transcripts/{document_id}
```

The catalog returns a typed unavailable result when snapshot closure is
incomplete; it never returns a partial inventory as complete. Upload streams or
spools one bounded raw `application/pdf` body with no filename or multipart
semantics into Applications custody and returns receipt-only language. Exact
content-derived receipt replay and exact owner request replay provide current
idempotency; the first slice has no caller-supplied idempotency key. The separate
`process-private` action returns a synchronous terminal result. An indeterminate
result requires reconciliation and supplies no transcript link or retry action.
The API does not return `202`, a workflow ID, queue position, percentage,
polling URL, or retry promise.

API maps owner DTOs without renaming their meanings. It owns no TeX parsing,
PDF storage, attachment decision, ingestion runtime, task database, package
search, or Search state. Errors expose stable codes and safe retry semantics,
never private paths, raw exception text, uploaded bytes, or provider details.

Web adds the dedicated control route `/control/citation-documents` only after
the reviewed API contract exists. It:

- preserves owner ordering and shows one escaped row per literal key;
- expands every occurrence without deduplication or source excerpts;
- presents non-key source gaps separately;
- labels every status in text rather than relying on color;
- shows **Provide PDF** and **Process privately** only when owner-projected
  allowed actions permit them;
- describes successful upload as private receipt, not ingestion;
- uses local pending state only during the synchronous request;
- labels an indeterminate result as requiring reconciliation without offering
  retry or transcript navigation; and
- opens the existing encoded transcript route with “Automated · unreviewed”
  labeling.

The browser never creates an attachment, processing admission, retry, Search
admission, or acceptance decision from local state. It parses no TeX, BibTeX,
Markdown, or filenames and renders all operator-visible values as escaped text.

## Threat and trust boundaries

PDF bytes and manuscript-derived labels are untrusted data. The owner
implementations must bound request size, counts, text, nesting, and aggregate
output; verify PDF media/header/parser expectations; constrain extraction
resources; and fail closed on malformed or hostile input. Filename, title, or
path resemblance supplies no identity evidence.

Private custody and package publication reject symlinks, path traversal,
changed-during-read content, partial output, hash mismatch, and replacement of
different existing artifacts. Descriptor-confined reads, private permissions,
atomic create-once publication, and exact replay protect against path and
TOCTOU attacks.

Opaque IDs are validated and encoded as data, never treated as paths or URLs.
No request body, idempotency key, absolute path, protected excerpt, uploaded
bytes, or raw provider error enters public logs, fixtures, or responses.

The local-processing boundary prevents confused-deputy escalation: upload is
not processing, processing is not neutral linkage, neutral linkage is not
rights approval, and technical success is not Search or authoring admission.
Source and target text do not leave the approved local boundary. Retrieved or
extracted content cannot issue tool or policy instructions.

## Ownership

| Concern | Owner |
|---|---|
| Product and cross-repository architecture | `projectkoios` |
| Citation graph, rendered occurrences, bibliography snapshot, source gaps | `ksdft2effmass` |
| Bibliographic identity, exact entry binding, availability, neutral link, catalog projection | `projectkoios-references` |
| Extraction and transcript artifacts | `projectkoios-ingestion` |
| Receipt, intent/admission, synchronous composition, package, registry | `projectkoios-applications` |
| HTTP DTOs, routing, bounded upload transport, safe errors | `projectkoios-api` |
| Control-page interaction and presentation | `projectkoios-web` |
| Index admission and per-document indexing state | `projectkoios-search`, deferred |
| Durable task execution | `projectkoios-workflow`, deferred |
| Scientific, editorial, rights, and purpose-specific authoring acceptance | Author or designated human authority |

## Acceptance and failure behavior

The slice is conformant only when:

1. the exact snapshot fixture derives 122 groups, 221 rendered calls, 277
   occurrences, 45 todo markers, and two source gaps without hard-coding them;
2. all repeated occurrences and generated citations remain independently
   addressable;
3. an unknown citation-capable macro makes inventory unavailable;
4. the target-owned complete Result artifact decodes and replays exactly before
   the target-side binding supplies neutral records;
5. incomplete inventory never appears as a complete catalog;
6. absent complete availability evidence remains `not-evaluated`, is never
   labeled missing, and enables no upload;
7. upload creates no link, processing request, Search item, or acceptance;
8. processing requires a separate exact intent/admission and neutral link;
9. duplicate receipt/request replay is deterministic and identity conflicts
   fail closed;
10. only terminal ingestion success, failure, or indeterminate outcome is
    persisted or returned, and indeterminate output requires reconciliation;
11. technically processed output remains unavailable to Search and authoring;
12. every transcript opens by opaque document ID with owner page order and
    automated/unreviewed labeling;
13. private paths, protected excerpts, and uploaded bytes do not cross the
    control boundary; and
14. no automated state implies scientific or editorial acceptance.

Snapshot incompleteness, unresolved or ambiguous identity, inaccessible bytes,
missing processing admission, stale projection, link ambiguity, malformed PDF,
extraction failure, publication conflict, malformed package, and unavailable
transcript remain distinct typed failures. None is relabeled as “missing,”
Search insufficiency, or human rejection.

## Deferred

The first slice excludes Search indexing, authoring-evidence admission,
automated citation acceptance, transcript proofreading, async dispatch,
queued/running status, retries, background workers, cross-process recovery,
remote processing, publication, redistribution, and manuscript or bibliography
writes. Applications manifest/runtime implementation, References production
availability/projection publication, and API standard-startup activation remain
ordered dependent milestones. Each requires its own owner validation and
separate implementation authorization.
