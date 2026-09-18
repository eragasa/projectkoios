# Contract governance

## Purpose

This policy defines identity, ownership, lifecycle, pre-release versioning,
change classification, and conformance requirements for Project Koios
cross-repository contracts.

A contract records an independently versioned boundary between producers and
consumers. It is not an implementation plan, task status, release artifact,
architecture decision, or authorization by itself.

## Scope

This policy applies to contracts consumed across Project Koios repository
boundaries. Owner-internal records may use the same convention but are not
required to appear in the cross-repository catalog unless another repository
depends on them.

Cross-repository product architecture remains in `projectkoios` ADRs. Contract
content remains in the repository that owns and enforces the boundary.

## Identity allocation

A contract has one globally unique, stable, namespaced ID:

```text
projectkoios.<owner-domain>.<contract-name>
```

The owner repository proposes the ID. Registration in
[`docs/contracts/README.md`](../contracts/README.md) reserves its uniqueness
across Project Koios. The catalog owns only namespace uniqueness and discovery;
it does not own component semantics or acceptance.

A contract ID is never a task ID, Python class name, file path, or version.
Renaming an ID creates a new contract and requires an explicit predecessor or
replacement relationship.

## Contract suites and granularity

One document may contain a suite of related contracts, but every independently
changing or independently consumed boundary has its own:

- contract ID;
- target version;
- lifecycle status;
- dependency and predecessor relationships;
- conformance subject; and
- acceptance evidence.

A suite title and file path have no lifecycle or version of their own. A suite
must state which sections are normative for each contained contract.

Separate contracts are required when boundaries can change, be accepted,
implemented, or consumed independently. Internal algorithms that no external
consumer observes belong in design documentation rather than being promoted to
cross-repository contracts.

## Pre-release versioning

Project Koios has no formal stable contract release. Cross-repository contracts
therefore use semantic versions below `1.0.0`:

```text
0.MINOR.PATCH
```

Rules before `1.0.0`:

- `0.1.0` is the initial target version for a newly registered contract.
- Increment `MINOR` for any normative behavioral, structural, compatibility, or
  meaning change, including a breaking change.
- Increment `PATCH` only for a clarification that does not change required
  producer or consumer behavior.
- Lifecycle status is not encoded in the version. A contract may be
  `Proposed` with target version `0.1.0`.
- The Git commit containing the document identifies the exact specification
  revision under review.
- `1.0.0` requires a separate human decision establishing the first formal
  stable contract release and its compatibility commitment.

An owner-internal schema, processor, artifact, or cache version may use a
different numbering system. Its relationship to the cross-repository contract
version must be explicit. Existing implementation identifiers are not silently
renumbered.

## Lifecycle

| Status | Meaning |
|---|---|
| `Draft` | The owner is developing the boundary; cross-repository review is not requested. |
| `Proposed` | A target version and complete review boundary are published for review. |
| `Accepted` | The designated human authority accepted the normative contract and recorded its immutable specification baseline. |
| `Deprecated` | The contract remains usable for a stated interval, but new adoption is discouraged. |
| `Superseded` | A named accepted successor replaces the contract subject to its migration policy. |
| `Retired` | The contract is no longer supported under a separately authorized decision. |

Lifecycle status is distinct from implementation status, task status, test
outcome, package release, architecture acceptance, scientific acceptance, and
publication authority.

### Transition requirements

`Draft → Proposed` requires:

- complete metadata;
- a target `0.x` version;
- identified owner, consumers, dependencies, and acceptance authority;
- normative scope and conformance subjects; and
- an owner task and governing architecture record.

`Proposed → Accepted` requires:

- separately recorded human acceptance;
- resolved normative ambiguity;
- review by materially affected producer and consumer owners;
- conformance criteria mapped to evidence or explicitly marked as required
  before implementation conformance may be claimed;
- compatibility and migration consequences;
- an immutable acceptance commit; and
- no unresolved `MUST_FIX` findings.

Acceptance of a contract does not authorize implementation, migration, release,
promotion, scientific use, or publication.

Deprecation, supersession, and retirement each require a separately authorized
decision identifying affected versions, consumers, migration or coexistence
period, rollback consequences, and the effective commit or release.

## Required metadata

Each cross-repository contract records:

| Field | Requirement |
|---|---|
| Contract ID | Stable globally registered identity |
| Target version | `0.x` while Project Koios has no formal stable release |
| Status | Contract lifecycle status |
| Specification revision | Git commit containing the exact document |
| Owner | Repository responsible for semantics and maintenance |
| Acceptance authority | Human authority required for lifecycle acceptance |
| Architecture record | Governing cross-repository architecture |
| Task | Mutable owner-task record |
| Predecessor | Prior contract ID/version, or none |
| Supersedes | Accepted contract replaced now; none while merely proposed |
| Dependencies | Exact contract IDs and target/accepted versions |
| Consumers | Materially affected repositories or boundary owners |
| Compatibility | Current compatibility classification and limitations |
| Effective baseline | Immutable acceptance commit, or none before acceptance |

Implementation classes and modules use a separate implementation-binding field
when needed. They are not contract predecessors or superseded contracts.

## Normative language

Contract documents distinguish normative requirements from informative
rationale and examples.

The words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**,
**SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are
normative when capitalized. Lowercase descriptions are informative unless a
section explicitly states otherwise.

Terms such as “conceptually,” “for example,” “equivalent,” and “subject to
implementation review” are non-normative. Unresolved terms may remain in a
proposed document, but they block acceptance when they affect observable
behavior or conformance.

## Conformance

Each contract identifies its conformance subjects, such as:

- artifact producer;
- artifact consumer;
- serializer or parser;
- index builder;
- retrieval service;
- adapter; or
- implementation package.

For each subject, the contract states normative obligations, bounds, failure
semantics, and required evidence. Conformance claims identify the contract ID,
version, exact specification commit, implementation commit, and validation
result.

Passing tests establishes only the bounded software claim represented by those
tests. It does not grant contract acceptance, lifecycle authorization,
scientific validity, or publication suitability.

## Dependencies and compatibility

Dependencies use contract IDs and explicit versions. A dependency on a Python
class, Markdown filename, issue number, or repository branch is not a contract
dependency.

Before `1.0.0`, consumers MUST NOT assume compatibility from version ordering
alone. Each proposed change records one of:

- `editorial` — no normative behavior change;
- `compatible` — existing conforming consumers remain valid under the stated
  bounds;
- `breaking` — a producer or consumer migration is required; or
- `unknown` — compatibility has not yet been demonstrated.

`unknown` is valid while proposed but blocks acceptance unless the acceptance
decision explicitly bounds the unresolved compatibility and affected use.

## Consumer review

The owner repository maintains contract semantics. Materially affected consumer
owners review proposed accepted boundaries and breaking changes. Consumer review
is evidence, not veto authority unless the governing architecture decision
explicitly grants it.

A consumer records supported contract versions in its implementation or
integration evidence. Listing a repository under `Consumers` does not imply
conformance or adoption.

## Catalog behavior

The cross-repository catalog contains:

- contract ID;
- owner;
- current authoritative document;
- governing architecture;
- parent roadmap; and
- immutable accepted baseline when one exists.

The catalog does not duplicate contract bodies, mutable task status,
implementation status, or acceptance evidence. Default-branch links are
current-draft discovery links. Only commit-pinned links identify an immutable
specification baseline.

## Change procedure

1. Change the authoritative owner document.
2. Classify the change and update target version metadata.
3. Review affected dependencies and consumers.
4. Record the exact specification commit in the owner task.
5. Update the catalog only when identity, ownership, path, architecture,
   roadmap, or accepted baseline changes.
6. Require separate authorization for acceptance, implementation, migration,
   release, deprecation, supersession, or retirement.

## Deferred machinery

No dedicated contract repository, schema service, generated mirror, custom
registry daemon, or package is authorized. Machine-readable schemas and
automated catalog checks are introduced only when a concrete serialization or
recurring validation requirement justifies them.
