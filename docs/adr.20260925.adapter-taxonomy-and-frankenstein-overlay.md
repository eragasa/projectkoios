# ADR20260925: Adapter taxonomy and Frankenstein incubation overlay

## Status

Accepted

## Context

Project Koios uses adapter terminology for multiple boundaries. Reconstructed
scientific software exposed a distinction that needs durable names:
PyFlamestk, PyPosPack, PyGithub, and similar packages are imported or
selectively vendored code dependencies, while LAMMPS, VASP, GitHub, and similar
calculators or services are external systems with separate effect authority.

The `projectkoios-frankenstein` repository also incubates modules intended for
selective transfer into the distributed `projectkoios` namespace. Repository
names must remain useful when one provider capability owns both dependency and
external-system concerns.

## Decision

Adapter is the nominal containing architectural set. Binding and integration
are distinct nominal adapter roles:

- a binding adapts an imported or deliberately vendored code dependency;
- an integration adapts an external application or service; and
- an integration may contain a binding through composition.

No generic `adapt()` method follows from adapter membership. Shared nominal
"is-a" relationships use base classes. Independent "has-a" relationships use
composition. A proposed additional shared base class freezes implementation
until an explicit architecture discussion accepts its invariant and owner.

Provider repositories use capability names such as `projectkoios-github` and
`projectkoios-lammps`. Python namespaces express adapter roles, for example
`projectkoios.adapters.bindings.pygithub` and
`projectkoios.adapters.integrations.github`.

`projectkoios.frankensteins` is a mirrored incubation overlay. Accepted modules
move by removing the `frankensteins` namespace segment, without renaming domain
classes or redesigning inheritance. Shared namespace levels remain compatible
with the implicit namespace-package decision in ADR20260629 and do not provide
broad implementation re-exports.

## Consequences

- A provider repository may publish both binding and integration leaves.
- A GitHub integration may compose a PyGithub binding while retaining external
  effect authority.
- PyFlamestk and PyPosPack reconstruction belongs under binding namespaces.
- LAMMPS and VASP behavior belongs under integration namespaces.
- Repository names do not encode binding, integration, or external prefixes.
- "External" remains a governance or contribution qualifier rather than an
  integration synonym.
- Existing API, deployment, workflow, persistence, and projection adapters are
  not automatically reclassified by this decision.
- Frankenstein source, test, and documentation paths mirror their intended
  final Project Koios paths.

## Alternatives considered

### Encode the role in every repository name

Rejected. Names such as `projectkoios-integration-github` become inaccurate
when the same capability also owns a dependency binding.

### Use an `external` repository family

Rejected. The term is ambiguous between technical effects, third-party
ownership, and contribution governance.

### Combine bindings and integrations

Rejected. Dependency API adaptation and external effect authority require
different contracts, tests, and evidence.

### Create Frankenstein-specific root contracts

Rejected. Repository-branded base classes would require renaming during
transfer and would prevent the namespace from serving as a pick-and-pull
incubation overlay.
