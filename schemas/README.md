# Project Koios schema registry

This directory is the canonical discovery registry for published or cross-repository Project Koios JSON Schemas. A schema's semantic owner remains the named domain; physical storage in this repository does not transfer implementation or acceptance authority.

`catalog.json` records each canonical `$id`, semantic owner, source path, exact SHA-256 identity, byte count, and publication state.

## Semantic-owner namespaces

Current allocations are:

| Code | Domain | Current owner repository |
|---|---|---|
| `ARCH` | Product architecture and accepted policy | `projectkoios` |
| `DEV` | Development coordination | `projectkoios-bootstrap` |
| `API` | HTTP API boundary | `projectkoios-api` |

A code identifies a stable semantic domain, not permanent repository placement. Additional codes are allocated only when a schema is registered; this registry does not pre-assign identities to independent projects.

## Resolution policy

Schema validation is offline and fail-closed:

1. resolve the exact `$id` through `catalog.json`;
2. read the repository-local `source_path` as a regular non-symlinked file;
3. verify its byte count and SHA-256 before use; and
4. reject unknown, mismatched, unpublished, or remotely redirected schemas.

A URL-shaped `$id` is an identity. It is not permission to perform network access. No Project Koios validator may fetch `$id` or `$ref` targets implicitly.

`publication_status: UNPUBLISHED` means the `$id` is reserved locally but is not claimed to resolve over HTTP. Publishing schemas at `projectkoios.com` requires a separate authorized publication mapping and deployment.

## Scope

The registry contains schemas with stable external identities or cross-repository consumers. Purely owner-internal schemas remain in their owner repositories until a concrete external consumer or publication requirement justifies registration.

Versioned schema identities are immutable after publication. A normative schema change receives a new versioned `$id`; existing published bytes are not replaced.

JSON Schema establishes document shape only. Cross-record properties such as reference resolution, graph acyclicity, and derived-leaf completeness remain explicit semantic-validator responsibilities named by the owning contract.
