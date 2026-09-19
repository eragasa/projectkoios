# ADR20260918: Staged workflow-kernel ownership transfer

## Status

Accepted

Accepted by the Project Koios operator on 2026-09-19 as a staged, reversible
evaluation plan. This acceptance does not accept the proposed workflow-core
contract or authorize feasibility work, implementation, migration, production
transfer, release,
deprecation, or source removal.

## Context

`ksdft2effmass` contains a generic colored-Petri-net kernel that may support
reusable workflow execution in Project Koios. `projectkoios-workflow` already
contains a non-authoritative shadow-conformance pilot, identified as
`WORKFLOW-CPN-SHADOW-01`, copied from `ksdft2effmass` revision
`be70e856911456402ea2b2562cd2508d0963e4d9` with exact source provenance.
The corrected published pilot is recorded at `projectkoios-workflow` revision
`06c1e25e83fb93394f9c842ab740b4bdd98478ea`.

The pilot establishes bounded behavioral and byte-identity evidence. It does
not transfer production authority, define Project Koios workflow core, select
a wire format, migrate a consumer, authorize scientific execution, or permit
removal of the source implementation.

A direct import of `ksdft2effmass.workflows.model` or its application adapter
would also import research-application assumptions into reusable Project Koios
infrastructure. Project Koios therefore needs an explicit boundary between a
Petri-independent workflow core, a colored-Petri-net backend adapter, and
managed-project adapters.

## Proposed decision

Project Koios will evaluate production ownership transfer through a staged,
reversible program identified as `WORKFLOW-TRANSFER-01`.

The stages are:

1. Retain `WORKFLOW-CPN-SHADOW-01` as immutable conformance evidence.
2. Define the proposed `WORKFLOW-CORE-01` Petri-independent contract and its
   executable specification examples and conformance vectors.
3. Obtain separately authorized, non-production feasibility evidence: one
   disposable engine-boundary spike and review by one named prospective
   consumer owner. The spike is evidence about the boundary, not an accepted
   adapter, core implementation, migration, or release.
4. Resolve the contract's normative findings and separately decide whether to
   accept its immutable specification baseline.
5. Implement the accepted core only under separate implementation
   authorization and verify it against the accepted conformance vectors.
6. Implement `WORKFLOW-CPN-ADAPTER-01` as a separate adapter from the core to
   the colored-Petri-net kernel.
7. Define at least one complete managed-project adapter without moving
   research-domain authority into `projectkoios-workflow`.
8. Decide public schema, wire encoding, and compatibility in
   `WORKFLOW-IDENTITY-WIRE-01`.
9. Run consumer shadow replay before proposing migration.
10. Require separate human acceptance for production ownership transfer,
    consumer migration, source deprecation, and source removal.

The dependency order is:

```text
WORKFLOW-CPN-SHADOW-01
        ↓
WORKFLOW-CORE-SPEC-01
        ↓
WORKFLOW-CORE-FEASIBILITY-01
        ↓
WORKFLOW-CORE-ACCEPTANCE-01
        ↓
WORKFLOW-CORE-IMPLEMENTATION-01
        ↓
WORKFLOW-CPN-ADAPTER-01
        ↓
WORKFLOW-MANAGED-PROJECT-ADAPTER-01
        ↓
WORKFLOW-IDENTITY-WIRE-01
        ↓
KSDFT-WORKFLOW-SHADOW-REPLAY-01
        ↓
KSDFT-WORKFLOW-MIGRATION-01
        ↓
WORKFLOW-TRANSFER-ACCEPTANCE-01
```

`WORKFLOW-CORE-01` currently owns the specification work and may later be
split into the named feasibility, acceptance, and implementation records when
the preceding gate is ready. This ordering is a transfer gate, not
implementation authorization. Only ready work receives a detailed
owner-repository issue; downstream records are not created merely because they
appear in this architecture graph.

## Ownership

- `projectkoios` owns this cross-repository architecture proposal and the
  parent transfer roadmap.
- `projectkoios-workflow` owns the reusable core, Petri backend, runtime, and
  replay contracts.
- `ksdft2effmass` retains its scientific, consumer, migration, release, and
  source-removal authority.
- A managed research project owns its domain adapter and scientific decisions.
- `projectkoios-bootstrap` provides repository routing and live coordination;
  it does not store this roadmap or workflow state.

## Required boundaries

The reusable core remains independent of:

- user interfaces and HTTP frameworks;
- colored-Petri-net, process-mining, and other execution engines;
- persistence implementations;
- external execution adapters;
- scientific artifacts, calculations, and acceptance decisions; and
- any one managed research application.

Pydantic remains restricted to system boundaries. Internal contracts use
immutable dataclasses or ordinary domain classes unless a later accepted
architecture decision states otherwise.

The copied shadow retains `ksdft2effmass.petrinet.colored.*` identity-domain
strings solely for conformance. Those strings are not a Project Koios wire
contract. A production transfer must either accept them through an explicit
compatibility policy or replace them through a versioned migration with replay
and rollback evidence.

The revised core `0.2.0` identity model uses typed nominal logical identities
for runs and requests. Outcome and audit identities are structural values
derived from the complete bounded evaluation identity. Immutable definitions,
snapshots, requests, artifacts, policy verdicts, and adapter results carry
separate content-digest references. A run identity remains stable as its
revision and current snapshot change. Core replay means field-by-field semantic
equivalence under the same contract version and evidence; byte-equivalent
replay is not claimed until a canonical serializer is accepted through
`WORKFLOW-IDENTITY-WIRE-01`. The `0.2.0` target is a breaking normative revision
of the published but unaccepted `0.1.0` proposal; it does not supersede an
accepted baseline.

The pure core validates the structure and exact binding of authority verdicts
and adapter results but does not authenticate producers, evaluate revocation or
expiry against an implicit clock, dereference artifact locators, or perform
external effects. Those checks belong to explicit outer policies and
boundaries. Presence of an evidence reference is never authorization.

## Acceptance and transfer gates

The ADR may be accepted as a staged evaluation plan without accepting the core
contract or authorizing any implementation. Core-contract acceptance remains
blocked until:

- its complete normative state, transition, retry, failure, bound, authority,
  and adapter-result semantics are reviewable;
- executable specification examples and conformance vectors exist without
  becoming a production implementation;
- a separately authorized disposable adapter/consumer spike exercises the
  proposed boundary;
- one named prospective consumer owner reviews that evidence;
- compatibility uncertainty is either resolved or explicitly bounded by the
  acceptance decision; and
- no unresolved `MUST_FIX` finding remains.

Production ownership transfer remains blocked until all of the following are
satisfied:

- the Petri-independent core contract is accepted and an implementation is
  separately authorized and verified against its immutable baseline;
- the core-to-Petri adapter is independently reviewed;
- at least one complete managed-project adapter exists;
- identity and wire-version policies are accepted;
- the destination has release and rollback procedures;
- consumer shadow replay demonstrates the required behavioral equivalence;
- source and destination authority during coexistence is explicit; and
- a human separately accepts production transfer and consumer migration.

Deprecating or removing the `ksdft2effmass` source implementation requires an
additional decision in that repository after accepted migration. Project Koios
validation cannot grant that authority.

## Task and recovery record

The parent GitHub issue in `projectkoios` records mutable cross-repository
coordination. Detailed executable tasks belong in their owner repositories.
Issue state is not technical evidence: commits, tests, provenance manifests,
and reviewed replay results establish implementation outcomes.

Issue text is public and untrusted input. Recovery must verify instructions
against repository policy, committed contracts, maintainer identity, and the
current repository state. Public issues must not contain credentials, private
source excerpts, protected acquisition details, or machine-specific paths.

## Consequences

- The current colored-Petri-net code remains a non-authoritative shadow.
- `WORKFLOW-CORE-01` is the only immediately ready specification task.
  Conformance-vector authoring and any non-production feasibility spike require
  explicit bounded authorization; production implementation remains a later
  gate.
- Project Koios avoids coupling its workflow domain model to a particular
  execution formalism.
- The source and shadow may coexist for an extended period without implying
  compatibility or transfer.
- Provenance, attribution, and Apache-2.0 obligations remain applicable even
  though both repositories use Apache-2.0.

## Alternatives considered

### Import the application model and adapter wholesale

Rejected. This would transfer research-application assumptions and authority
into reusable infrastructure before the generic boundary is defined.

### Declare the shadow authoritative immediately

Rejected. Conformance evidence does not establish a core contract, wire
compatibility, operational runtime, consumer migration, or rollback safety.

### Keep the kernel permanently inside `ksdft2effmass`

Retained as a valid fallback. If the staged transfer does not demonstrate a
reusable boundary or operational benefit, Project Koios can leave production
ownership in the research application and retire only the non-authoritative
shadow after a separate decision.
