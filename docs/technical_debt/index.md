# Technical debt documentation

## Purpose

This directory defines the Project Koios boundary for durable,
evidence-linked documentation of observed technical debt. A technical-debt
record describes a current implementation or documentation condition whose
cost, risk, or constraint is concrete enough to preserve for bounded
investigation.

A technical-debt record is not an architecture decision, replacement design,
work authorization, priority, approval, task state, or acceptance result.

## Project boundary

Each repository owns technical-debt evidence for the implementation,
contracts, and documentation it owns. Component repositories keep that
evidence under `docs/technical_debt/<area>/...`.

`projectkoios` owns this project-wide convention and records only debt in the
product architecture or other material that this repository itself owns. It
must not become a central debt catalog, replicated backlog, status database,
work queue, or approval authority. When one concern affects several
repositories, each owner records only its own evidence and boundary.

Technical-debt documents contain public, repository-relative evidence. Private
paths, protected content, credentials, and mutable operational state remain in
their owning private or operational systems.

## Immediate responsibility

This index defines immediate responsibility and does not inventory descendant
records or component repositories.

| Direct child | Immediate responsibility |
|---|---|
| [Owner-repository convention](convention/index.md) | Defines ownership, record guidance, architecture and execution boundaries, and an illustrative example. |

Execution remains in owner issues, pull requests, and Git history. Current
architecture remains in its owning architecture documents.
