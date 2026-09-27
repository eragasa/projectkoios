# ADR20260927: Application composition ownership

## Status

Accepted

Accepted by the Project Koios operator on 2026-09-27.

## Context

Project Koios needs a durable boundary between reusable capabilities and the
scientific applications that compose them. The initial `pw_dft_scf` work joins
simulation providers, scientific recipes, workflow behavior, colored-Petri-net
(CPN) behavior, execution, replay, and evidence. Treating that composition as
either a neutral simulation capability or a generic workflow concern would
move application policy into reusable infrastructure. Creating a repository for
every application capability would instead fragment one composition owner.

A local `projectkoios-applications` repository now owns the
`projectkoios.applications` namespace. Its first incubated capability is the
Frankenstein overlay for `applications.pw_dft_scf`.

## Decision

A Project Koios application is the workflow/CPN-enabled composition layer that
stitches reusable capabilities into a scientific operation. The
`projectkoios-applications` repository owns:

- cross-capability composition;
- application scientific policy, recipes, and configuration;
- application workflow definitions and facades;
- application CPN composition;
- application runners and replay;
- campaigns; and
- application evidence and outcomes.

These responsibilities are application-scoped. Application evidence may refer
to provider artifacts and generic workflow records without taking ownership of
the reusable implementations that produced or tracked them. Scientific
acceptance remains an explicit human or separately declared domain authority;
a completed application run does not imply acceptance.

Application capabilities are packages under the shared owner, not repositories
by default. In particular, `pw_dft_scf` is the capability package
`projectkoios.applications.pw_dft_scf`; it is not a standalone application or
repository. Additional application capabilities share
`projectkoios-applications` unless a later accepted decision establishes a
materially independent ownership boundary.

The Frankenstein source path mirrors the intended final namespace as
`projectkoios.frankensteins.applications.pw_dft_scf`. Transfer removes only the
`frankensteins` segment, following
[ADR20260925](adr.20260925.adapter-taxonomy-and-frankenstein-overlay.md).

Reusable ownership remains separate:

| Owner | Responsibility |
|---|---|
| `projectkoios-simulations` | Neutral simulation abstractions and provider integrations, without application recipes, campaigns, or scientific outcome policy. |
| `projectkoios-workflow` | Generic workflow runtime, state, engine, replay primitives, and CPN contracts, without application scientific semantics. |
| `projectkoios-applications` | Composition and policy that specialize those reusable capabilities into applications. |

Dependencies point from applications to reusable components. Reusable
components, including simulations, workflow, and provider integrations, must
not import `projectkoios.applications` or an application capability package.
Shared behavior needed by a reusable component must be expressed through a
neutral contract owned outside the application layer.

## Reconciliation with earlier decisions

This decision preserves earlier records as history and narrows or supersedes
their ownership language as follows:

- [ADR20260918](adr.20260918.workflow-kernel-transfer.md) says a managed
  research project owns its domain adapter. An independent research project
  still owns its scientific, migration, release, and source authority. Project
  Koios cross-capability application adapters, facades, and policy now belong
  to `projectkoios-applications` rather than to a reusable component or a
  repository created for each capability.
- [ADR20260920](adr.20260920.workflow-and-cpn-development-tracks.md) places the
  first ingestion workflow adapter in a deployment layer and identifies an
  ingestion-owner task. That placement remains historical sequencing, but
  application workflow definitions and cross-capability composition now belong
  to `projectkoios-applications`. Ingestion retains neutral ingestion behavior;
  workflow retains generic runtime and CPN contracts.
- [ADR20260925](adr.20260925.adapter-taxonomy-and-frankenstein-overlay.md)'s
  adapter taxonomy and mirrored Frankenstein transfer rule remain in force.
  Its capability-repository examples do not require one repository per
  provider or application capability. For neutral simulation providers, this
  decision assigns the integrations to `projectkoios-simulations`; for
  application capabilities, it assigns the packages to
  `projectkoios-applications`.
- The [scientific-platform thesis](architecture.scientific-platform-thesis.md)
  continues to treat independently governed projects such as `ksdft2effmass`
  and `dacp2transport` as independent. That is distinct from a capability
  intentionally owned inside the Project Koios application composition layer.

## Consequences

- Application scientific semantics do not leak into neutral simulation or
  generic workflow packages.
- The generic workflow runtime and CPN contracts can serve multiple
  applications without depending on any of them.
- Neutral simulation providers can be reused by more than one application.
- Application capabilities share one release and architecture owner until a
  later decision establishes a genuine independent boundary.
- Application replay and outcomes remain distinguishable from generic workflow
  replay mechanics and provider-level artifacts.

## Alternatives considered

### Make `pw_dft_scf` a standalone repository

Rejected. It is one application capability under a shared composition owner,
not an independently governed application.

### Put the composition in `projectkoios-simulations`

Rejected. Scientific recipes, workflow definitions, campaigns, and outcomes
are application policy rather than neutral simulation behavior.

### Put the composition in `projectkoios-workflow`

Rejected. Generic workflow runtime, state, engines, and CPN contracts must not
depend on application scientific semantics.
