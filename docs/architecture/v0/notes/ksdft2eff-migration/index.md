# `ksdft2effmass` migration notes

Status: **Exploratory inventory**

This note supports the [Project Koios architecture v0 plan](../../index.md). It
is not an accepted migration plan, implementation authorization, or scientific
disposition.

## Intent

Project Koios is expected to absorb reusable research-platform capabilities
that were first developed inside `ksdft2effmass`. The source project should
retain its scientific claims, claim-specific interpretation, scientific
acceptance criteria, and other content whose meaning depends on its research
program.

The desired result is not a copy of the entire source repository. It is a set of
bounded extractions into explicit Project Koios owners.

## Classification vocabulary

Each candidate asset should receive exactly one preliminary disposition:

| Disposition | Meaning |
|---|---|
| `EXTRACT` | Move a reusable capability to its accepted Project Koios owner while preserving compatibility as needed. |
| `REPACKAGE` | Adapt a reusable implementation or design, removing source-project semantics and assigning a new Project Koios contract. |
| `RETAIN_CLAIM_SPECIFIC` | Keep the asset in `ksdft2effmass` because its correctness or meaning depends on that scientific project. |
| `DEFER` | Evidence or destination ownership is insufficient for a safe decision. |

A disposition is an architectural recommendation, not mutation authority.

## Boundary test

For each asset, ask:

> Could another scientific project use this asset unchanged in meaning without
> adopting an effective-mass or Kohn--Sham scientific claim?

A positive answer makes it an extraction candidate. It does not determine the
destination repository by itself.

## Initial candidate inventory

| Source capability | Preliminary disposition | Likely destination or next question |
|---|---|---|
| Strict JSON loading and duplicate-member rejection | `REPACKAGE` | Project Koios architecture-document tooling |
| Draft 2020-12 schema validation and deterministic diagnostics | `REPACKAGE` | Project Koios architecture-document tooling |
| Deterministic JSON-to-Markdown projection profiles | `REPACKAGE` | Project Koios architecture-document tooling |
| Exact-byte Markdown identities and drift comparison | `REPACKAGE` | Project Koios architecture-document tooling |
| Valid/invalid fixture and expected-byte oracle pattern | `REPACKAGE` | Project Koios architecture-document tooling |
| DataObject, ActionObject, request, and operation-result separation | `REPACKAGE` | Adopt the Project Koios DataObject plus DataObjectActionRequest → DataObjectActionizer → DataObjectActionResult roles |
| Resource manifests with content identities | `REPACKAGE` | Assess against Project Koios artifact and provenance ownership |
| Generic artifact and provenance concepts | `EXTRACT` | Route through accepted cross-repository architecture and the eventual component owner |
| Generic workflow, Task, attempt, result, and effect concepts | `DEFER` | Continue through the existing workflow-kernel transfer decisions |
| Generic human-decision and review presentation concepts | `DEFER` | Reconcile with API, Web, workflow, and durable-decision ownership |
| Generic calculator and simulation ports | `DEFER` | Separate reusable execution capability from scientific interpretation |
| QE and Wannier90 mechanical adapters | `DEFER` | Determine whether they are reusable integrations or source-project adapters |
| Effective-mass claims and interpretations | `RETAIN_CLAIM_SPECIFIC` | `ksdft2effmass` |
| Kohn--Sham model-adequacy conclusions | `RETAIN_CLAIM_SPECIFIC` | `ksdft2effmass` |
| Claim-specific equations, assumptions, and acceptance criteria | `RETAIN_CLAIM_SPECIFIC` | `ksdft2effmass` |
| Scientific manuscript and publication prose | `RETAIN_CLAIM_SPECIFIC` | `ksdft2effmass` unless separately authored as a Project Koios product record |

## Documentation-projection predecessor

The first extraction candidate is supported by a concrete predecessor in
`ksdft2effmass`.

Current committed source includes:

```text
python/src/ksdft2effmass/harness/pi/local/
  documentation_projection_validation.py

harness/local/projections/
  task-control-reference-v1.json

harness/local/fixtures/task-control-reference/
harness/local/resource-manifest.json
```

Historical commit `a577ebb1` contains a fuller exact-byte Task documentation
renderer in:

```text
python/src/ksdft2effmass/harness/pi/local/task_model.py
```

Reusable mechanics observed there include:

- immutable frozen records;
- strict deserialization and unknown-field rejection;
- canonical UTF-8 JSON;
- explicit template and projection identities;
- deterministic rendering from explicit inputs;
- exact final-line-feed policy;
- SHA-256 output identity;
- byte-level source/projection comparison; and
- explicit limitations that mechanical agreement is not human acceptance.

The architecture extraction should reuse these mechanics without carrying over
`HarnessTask`, Task-chain authority, activation, `PIHL.*` diagnostics,
source-project profiles, or scientific-domain semantics.

## JSON serialization extraction findings

The JSON audit used committed tree
`7bd913151f7e61ed2bdba593df920be36573b502`; unrelated working-tree changes
were excluded. There is no single serializer that should be copied whole. The
best Project Koios boundary combines several bounded predecessors.

| Predecessor | Strongest reusable property | Disposition |
|---|---|---|
| `harness/pi/wire/canonical_json.py` | Minimal UTF-8 canonical encoder, duplicate-member rejection, nonfinite-constant rejection | Repackage as low-level strict JSON mechanics |
| `provenance/serialization.py` | Best complete explicit record mapping and negative-test partition: discriminators, exact fields, BOM, duplicate, surrogate, numeric-type, and unsupported-version rejection | Reuse its explicit mapping and fixture approach |
| `harness/configuration.py` | Human-readable two-space JSON, strict byte input, exact member vocabulary, and decode/re-encode canonicality check | Reuse selectively for authored configuration and policy files |
| `harness/pi/validation.py` | Immutable serialization/deserialization results, deterministic diagnostics, and no partial value on failure | Repackage the result pattern without its harness-wide union or issue registry |
| `harness/pi/local/documentation_projection_validation.py` | Strict loader followed by Draft 2020-12 JSON Schema validation and deterministic schema diagnostics | Repackage for architecture and policy document validation |
| `harness/_compiler_serialization.py` | Closed JSON algebra, NFC enforcement, UTF-8 key ordering, and domain-separated length-framed identities | Reuse the identity framing and closed-representation concepts |
| `operators/serialization.py` | Strong numeric and container negative fixtures, including Boolean-versus-integer and huge-integer handling | Reuse fixture cases; do not import scientific or NumPy dependencies |
| `workflows/persistence/serialization/run.py` | Exact re-encoding, structured incompatible/corrupt/error outcomes, representation-limit handling, and no partial reconstruction | Retain as an advanced reference, not the initial generic implementation |
| `serialization/contracts.py` | Demonstrated nominal serializer/deserializer/codec ABC across many scientific codecs | Defer; Project Koios has not yet demonstrated need for a universal nominal base |

### Recommended Project Koios composition

The first Project Koios implementation should provide domain-neutral mechanics,
not a reflective object serializer:

1. `StrictJsonObjectDecoder` consumes bounded bytes, rejects BOMs, invalid
   UTF-8, duplicate members, non-RFC constants, prohibited Unicode, excess
   depth/count/size, and a non-object root.
2. The owning document deserializer checks exact versioned fields and converts
   the closed JSON value into its immutable DataObject without coercion.
3. Draft 2020-12 JSON Schema validation supplies deterministic structural
   diagnostics where a published schema exists; it does not replace strict
   parsing or DataObject construction.
4. `CanonicalJsonEncoder` accepts only a closed JSON representation and emits
   deterministic UTF-8 bytes with an explicit whitespace/final-LF profile.
5. The owning serializer maps each supported DataObject explicitly into that
   representation; arbitrary dataclass reflection is excluded.
6. `JsonSerializationResult` and `JsonDeserializationResult` contain either one
   complete value or structured findings, never a partial value.
7. Content identity binds exact emitted bytes. Semantic identities, when
   needed, use a versioned domain separator and length framing rather than a
   bare unscoped hash.

Architecture and policy JSON are human-authored inputs. Their decoder may
accept insignificant whitespace and object-member order while still rejecting
ambiguous or malformed input. A serializer owns the preferred two-space source
format. A separate deterministic Markdown renderer consumes the decoded and
validated DataObject. Requiring every author to supply already compact,
key-sorted JSON would optimize for wire transport at the expense of review.

### Required corrections during extraction

The source implementations do not collectively satisfy all Project Koios
requirements without modification:

- Python's standard `json.loads` does not provide application byte, nesting,
  collection, or string bounds; Project Koios must enforce them explicitly.
- Schema validation occurs only after duplicate-member-safe parsing.
- Float admission is contract-specific. Architecture and policy records should
  prohibit floats until a represented use requires an exact numeric contract.
- Boolean values must never satisfy integer fields accidentally.
- The generator-expression trick used by one `parse_constant` callback should
  become a named function consistent with the Python policy.
- Harness-global dispatch unions, runtime import patching, issue registries,
  Task semantics, and broad reflective dataclass conversion must not migrate.
- Catch-all exception handling is reserved for a documented isolation boundary;
  ordinary serializers use specific exceptions.
- Canonical byte comparison establishes representation agreement only, not
  semantic, human, or scientific acceptance.

## Object-model synthesis

The migration should not copy the complete nominal vocabulary of either
project. Project Koios v0 treats DataObject and DataObjectActionizer as the two
BaseObject classifications without introducing a public `BaseObject` class. It
defines the thin `DataObject` ABC for struct-like records, the thin generic
`DataObjectActionizer` ABC for function-like operations, and this exact flow:

```text
DataObjectActionRequest → DataObjectActionizer → DataObjectActionResult
```

An immutable DataObject is a `DataObjectModel`. The request and result ABCs
therefore inherit `DataObjectModel`; a separate domain-model value remains
optional and is introduced only when its identity or reuse matters.

The relationship to the source-project vocabulary is:

| Source concept | Project Koios v0 treatment |
|---|---|
| Struct-like DataObject | Inherit the thin `projectkoios.base.DataObject` ABC and retain intrinsic invariants and valid cheap deterministic methods |
| Immutable DataObject | Inherit `DataObjectModel`, the immutable DataObject ABC specialization |
| Exact operation input | Inherit `DataObjectActionRequest`, identifying all DataObjects, parameters, and any separate domain-model object |
| ActionObject | Repackage as the function-like `DataObjectActionizer` ABC over one exact request and explicit dependencies |
| ResultObject returned by an operation | Inherit `DataObjectActionResult` unless it is specifically a workflow ResultObject |
| Workflow ResultObject | Keep as a distinct workflow-facing role and never infer it from an operation-result name |
| BaseObject | Use as a classification containing DataObject and DataObjectActionizer; do not introduce a public class |
| Registries and reflective discovery | Do not extract as part of this pattern |

Concrete Python operation families share a domain stem. For example,
`ArchitectureDocumentRenderRequest`,
`ArchitectureDocumentRenderActionizer`, and
`ArchitectureDocumentRenderResult` inherit the applicable thin public ABCs
while retaining domain names. `Result` remains the internal domain term; a
transport adapter may separately produce an HTTP response model.

The implementation follows the authoritative Draft
[Project Koios Python policy source](../../../../policies/code/python.json) and
its [Markdown projection](../../../../policies/code/python.md). That policy
selects readability and safety guidance from the Google Python Style Guide
subject to each owner repository's existing Ruff, MyPy, Python 3.14, formatting,
and validation configuration. It does not authorize a repository-wide style
rewrite or replacement of established tooling with Pylint or Pyink.

## Python test-evidence audit predecessor

The same committed tree already contains the reusable test-evidence audit
mechanics. Project Koios must adapt that implementation rather than create an
unrelated validator:

- `PythonConformanceValidator` accepts explicit source and metadata bytes and
  performs no repository discovery or filesystem access;
- the strict adapter owns Test-class ownership, helper ownership, typing, and
  test-resource-placement checks;
- the repository-local adapter resolves repository authority and supplies exact
  inputs to the generic validator;
- the thin CLI emits deterministic `PASS`, `FAIL`, `INVALID_INPUT`, or
  `INTERNAL_ERROR` JSON; and
- the profile matrix distinguishes `routine` and `claim_bearing` evidence and
  owns the required module and per-test fields.

The authoritative Project Koios adaptation is
[`python_test.json`](../../../../policies/code/python_test.json), with generated
[`python_test.md`](../../../../policies/code/python_test.md). Both bind the audit
sources to committed revision
`7bd913151f7e61ed2bdba593df920be36573b502` and exact SHA-256 identities.
Project Koios retains explicit-input validation, stable findings, ownership,
profiles, evidence identifiers, parameter inventories, and claim boundaries. It
adapts repository paths, local `test__...` spelling, private Test-owner helper
placement, and migration timing. Extraction of the implementation remains a
separate owner-repository decision; the mothership policy does not become a
second audit implementation.

## Architecture-document target

The proposed Project Koios source format is one closed JSON object per module:

```text
docs/architecture/v0/<module>.json
```

Its deterministic projection is:

```text
docs/architecture/v0/<module>.md
```

The JSON model must represent classes, attributes, relationships,
cardinalities, responsibilities, exclusions, invariants, flows, failures,
repository boundaries, conformance fixtures, and deferred decisions. The
renderer generates prose tables and Mermaid class diagrams from those records;
it does not accept arbitrary Mermaid as a second architectural authority.

## Provenance and source-worktree safety

The inspected `ksdft2effmass` working tree contains unrelated modifications.
Extraction must therefore read named committed blobs or use an isolated clean
worktree at an explicit revision. It must not copy files from the dirty working
tree and describe them as committed source.

For every adapted file, retain technical provenance containing:

- source repository;
- exact source revision;
- source path;
- extracted concepts or code spans;
- destination path;
- adaptation summary; and
- validation evidence.

The same owner controls both projects and has stated that there are no other
contributors. Technical provenance remains valuable for replay and maintenance
even when third-party attribution is not required.

## Destination principles

“Project Koios owns the reusable platform” refers to the Project Koios
repository ecosystem, not necessarily the mothership package.

- Cross-repository architecture and durable decisions belong in
  `projectkoios`.
- Ingestion, references, search, workflow, agent, API, and Web implementation
  belongs in their respective owner repositories.
- Repository-local architecture-document rendering may begin as documentation
  tooling in `projectkoios`.
- `projectkoios-bootstrap` remains an operational Pi/Herdr coordination cockpit
  and is not the product-architecture owner.
- A new shared tooling package should not be created until repeated use shows
  that repository-local tooling is insufficient.

## Migration gates

No candidate should move until all applicable gates pass:

1. exact committed-source inventory;
2. destination ownership decision;
3. source and destination contract comparison;
4. removal of scientific or harness-specific semantics;
5. valid and invalid conformance fixtures;
6. deterministic replay where applicable;
7. compatibility or retirement plan for source consumers;
8. source-project validation;
9. destination-repository validation; and
10. separate authorization to commit, publish, integrate, or retire the source.

## Explicit non-decisions

This note does not decide:

- whether `ksdft2effmass` becomes a thin package, research repository, or
  publication repository;
- ownership of reusable QE or Wannier90 integrations;
- migration of workflow implementation already covered by separate ADRs;
- scientific acceptance of any result or claim;
- retirement of any existing source-project interface; or
- creation of a new Project Koios repository.
