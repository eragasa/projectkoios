# Project Koios web architecture

## Purpose

The Project Koios web layer is a reusable browser interface over stable HTTP
and WebSocket contracts. Its implementation is owned by the dedicated
`projectkoios-web` repository.

```text
projectkoios-web
    -> projectkoios-api
    -> application services
    -> domain packages and storage adapters
```

The web layer does not import Python packages or read vaults, databases, search
indices, or extraction caches directly.

## Repository boundary

`projectkoios-web` owns browser routes, interaction design, API clients,
reusable components, accessibility, responsive presentation, and browser tests.

It does not own backend domain semantics, persistence, filesystem access,
user-specific deployment policy, or canonical API schemas.

## Contract boundary

`projectkoios-api` publishes OpenAPI as the canonical browser contract. The web
repository generates TypeScript boundary types from that schema and wraps them
in a framework-independent API client.

The initial vertical slice uses:

```text
GET /health
POST /search
```

Planned interfaces include source inspection, provenance, ingestion status,
workflow review, and vault-layout review. Backend contracts should exist before
a UI gains write behavior.

## Local-first rule

The default deployment is loopback or same-origin. The browser application does
not include third-party analytics, externally hosted fonts, or direct upload of
user content to external services.

Private deployment preferences remain outside the reusable web repository.
Absolute vault paths remain backend configuration and must not be embedded in a
browser bundle.

## Human-control rule

Read-only inspection precedes write functionality. Future destructive or
content-changing operations require server-side validation, a visible target,
and explicit confirmation. The browser does not bypass workflow approval or
vault-migration safety contracts.

## Implementation

Repository-local implementation details and user instructions live in:

- `projectkoios-web/docs/architecture.md`
- `projectkoios-web/docs/user-guide.md`
