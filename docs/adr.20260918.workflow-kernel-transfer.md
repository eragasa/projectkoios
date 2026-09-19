# ADR20260918: Staged workflow-kernel ownership transfer

## Status

Proposed

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
2. Define and accept `WORKFLOW-CORE-01`, a Petri-independent core contract.
3. Implement `WORKFLOW-CPN-ADAPTER-01` as a separate adapter from the core to
   the colored-Petri-net kernel.
4. Define at least one complete managed-project adapter without moving
   research-domain authority into `projectkoios-workflow`.
5. Decide identity, schema, and wire-version compatibility in
   `WORKFLOW-IDENTITY-WIRE-01`.
6. Run consumer shadow replay before proposing migration.
7. Require separate human acceptance for production ownership transfer,
   consumer migration, source deprecation, and source removal.

The dependency order is:

```text
WORKFLOW-CPN-SHADOW-01
        ↓
WORKFLOW-CORE-01
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

This ordering is a transfer gate, not authorization to implement every stage.
Only ready tasks receive detailed owner-repository issues. Downstream tasks
remain proposed until their dependencies are accepted.

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

## Transfer gates

Production ownership transfer remains blocked until all of the following are
satisfied:

- the Petri-independent core contract is accepted;
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
- `WORKFLOW-CORE-01` is the only immediately ready implementation-planning
  task; later tasks are created when their dependencies are accepted.
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
