# ADR20260626: Move away from the monorepo structure

## Status

Accepted

## Supersedes

ADR20260611: Use `projectkoios` as the main Python package repository

If the original ADR file is missing, this supersedes the reconstructed version of that decision.

## Context

The original Project Koios architecture treated `projectkoios` as the main Python package repository.

The implementation lived under:

`src/python/projectkoios`

The package was organized into internal namespaces such as:

- `projectkoios.core`
- `projectkoios.vault`
- `projectkoios.search`
- `projectkoios.references`
- `projectkoios.workflow`
- `projectkoios.api`

That structure was useful for the first prototype. It made the project easy to start, run, inspect, and test locally.

However, the structure is starting to feel too monolithic. The components have different purposes and development rhythms. Keeping all of them inside one repo makes the project harder to reason about and harder to evolve.

## Decision

Move away from the monorepo structure.

Keep `projectkoios` as the mothership repository.

Use the mothership for:

- architecture notes
- roadmap
- ADRs
- examples
- configuration templates
- incubation code

Extract major components into separate repositories as their boundaries become clear.

The first extracted implementation repository will be:

- `projectkoios-agent`

The initial agent package will use:

`src/projectkoios/agent`

Do not create `projectkoios-core` yet.

A core package should only be created after shared abstractions become stable across multiple components.

## Rationale

The original structure was good for a prototype.

It allowed the first package layout, API boundary, search model, and workflow ideas to develop together.

The next stage needs looser coupling.

The agent harness is the clearest first extraction because it has a distinct purpose: model backends, tool execution, workflow control, provenance tracking, and artifact generation.

Creating `projectkoios-core` now would freeze abstractions too early. It is better to let the extracted components reveal what actually needs to be shared.

## Consequences

The existing `docs/architecture.md` remains useful as historical and conceptual architecture, but it no longer defines the target repository structure.

The old internal namespaces become extraction candidates:

- `projectkoios.vault`
- `projectkoios.search`
- `projectkoios.references`
- `projectkoios.workflow`
- `projectkoios.api`
- `projectkoios.agent`

Some small abstractions may be duplicated temporarily.

Shared abstractions should move to core only after repeated use proves that they are actually shared.

A practical rule:

- used by one component: keep local
- used by two components: consider extraction
- used by three or more components: promote to core

## Alternatives considered

### Keep everything in `projectkoios`

Rejected.

This keeps early development simple, but it makes the project too monolithic as the components grow.

### Create `projectkoios-core` immediately

Rejected.

The shared abstractions are not stable enough yet.

### Extract all components at once

Rejected.

That would create too much packaging overhead before the component boundaries are proven.

## Current next step

Create `projectkoios-agent` as the first extracted implementation repository.

The first MVP should be a small local harness workflow, not a full general agent system.