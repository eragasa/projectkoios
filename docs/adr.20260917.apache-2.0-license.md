# ADR20260917: Apache License 2.0 across Project Koios repositories

## Status

Accepted

## Context

Project Koios is implemented across multiple repositories with independent package metadata and release histories. Most Project Koios repositories were initially licensed under the MIT License, while `ksdft2effmass`, the intended first managed research project and a source of potentially reusable workflow implementation, is licensed under the Apache License 2.0.

Using Apache-2.0 consistently for Project Koios-owned code and documentation provides an explicit patent grant and removes an avoidable destination-license mismatch for reviewed reuse from Apache-2.0 research applications. A repository-wide change does not alter the licenses of third-party dependencies, external research projects, separately licensed reference material, or earlier versions already distributed under the MIT License.

## Decision

The repository-owned code and documentation in the following Project Koios repositories are licensed under the Apache License, Version 2.0:

- `projectkoios`
- `projectkoios-bootstrap`
- `projectkoios-agent`
- `projectkoios-api`
- `projectkoios-courses`
- `projectkoios-ingestion`
- `projectkoios-obsidian`
- `projectkoios-references`
- `projectkoios-research`
- `projectkoios-search`
- `projectkoios-web`
- `projectkoios-workflow`

Each repository carries the canonical Apache License 2.0 text in its root `LICENSE` file. First-party package metadata and first-party fixture-rights declarations use the SPDX identifier `Apache-2.0`.

This decision does not relicense:

- third-party packages or vendored components;
- external research applications merely registered by Project Koios;
- bibliographic records or source materials with their own licenses;
- generated or imported artifacts whose rights are separately recorded; or
- historical Project Koios revisions already made available under the MIT License.

Copying Apache-2.0 source between repositories still requires preserving applicable copyright, attribution, modification, and NOTICE obligations. Common licensing does not erase source provenance or repository ownership boundaries.

## Consequences

- New Project Koios-owned contributions use Apache-2.0 unless a later accepted decision establishes a narrower exception.
- Package manifests use `Apache-2.0` for first-party package licensing.
- Synthetic fixtures authored by Project Koios may identify Apache-2.0 as their rights basis; fixtures or references obtained from other sources retain their actual rights.
- Dependency lock files continue to report each dependency's own license and must not be rewritten to Apache-2.0.
- External projects retain their independent licensing and publication authority.
- Prior MIT grants remain valid for the revisions to which they applied.

## Alternatives considered

### Retain MIT across Project Koios

Rejected. It would preserve a license mismatch with the Apache-2.0 workflow source being evaluated for bounded reuse and would omit Apache-2.0's explicit patent grant.

### Dual-license Project Koios under MIT and Apache-2.0

Rejected for now. No current distribution or integration requirement justifies the additional compatibility and communication burden.

### Change only `projectkoios-workflow`

Rejected. A consistent Project Koios policy is easier to communicate and avoids repeating the same licensing decision as reusable components move between Project Koios repositories.
