# ADR20260611: Use `projectkoios` as the main Python package repository

## Status

Superseded

## Note

This ADR was reconstructed after the original decision record was lost.

The decision is reconstructed from the original Project Koios architecture document, which described the current repository as a Python package repository with the main implementation under `/src/python/projectkoios`.

## Context

The early Project Koios architecture treated the repository as a Python package first.

The package contained the main system namespaces:

- `projectkoios.core`
- `projectkoios.vault`
- `projectkoios.search`
- `projectkoios.references`
- `projectkoios.workflow`
- `projectkoios.api`

The design rule was that Project Koios was a Python package first, and FastAPI was an adapter rather than the system itself.

## Decision

Use `projectkoios` as the main Python package repository.

Keep the initial implementation under:

`src/python/projectkoios`

Use internal namespaces to separate concerns:

- `core` for shared infrastructure
- `vault` for Obsidian and Markdown handling
- `search` for indexing and retrieval
- `references` for BibTeX, PDFs, and citation metadata
- `workflow` for task, state, and provenance objects
- `api` for the FastAPI adapter

## Rationale

This structure made the first prototype easy to run, test, and understand.

Keeping the system inside one Python package reduced early packaging overhead and allowed the initial object model, API boundary, search model, and workflow concepts to evolve together.

## Consequences

The repository became a package-centered prototype.

The structure was coherent for early development, but it also pushed Project Koios toward a monorepo/package-monolith shape.

This decision is now superseded by the later decision to keep `projectkoios` as the mothership repo and extract major components into separate implementation repositories.
