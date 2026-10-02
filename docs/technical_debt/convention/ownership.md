# Technical debt ownership

The [owner-repository convention](index.md) assigns technical-debt evidence to
the repository that owns or enforces the affected behavior.

## Owner-local placement

Component repositories keep their records under an owner-local area:

```text
docs/technical_debt/
├── index.md
└── <area>/
    ├── index.md
    └── <observation>.md
```

A repository or area index defines only its immediate scope, ownership, and
direct child responsibilities. It may identify directly relevant child records
or subareas, but it must not recursively inventory descendants, aggregate
status, or mirror an issue backlog.

Use descriptive area and observation names. Do not create numbered migrations,
historical tombstones, decision records, or repository-specific alternatives
to the common architecture-documentation convention.

## Cross-repository concerns

When a concern crosses repositories, each owner records only the evidence,
impact, and must-preserve behavior within its boundary. Coordination records
may link the owner-local documents, but `projectkoios` does not copy them into a
central debt catalog or acquire approval authority over component debt.

Naming an affected repository or human authority does not assign work, transfer
ownership, or authorize a change.

## Public-record safety

Technical-debt documents contain public, repository-relative evidence. Private
paths, credentials, protected excerpts, unpublished material, and machine-bound
operational details do not belong in public records. An owner may cite an opaque
artifact identity when doing so does not disclose protected information.
