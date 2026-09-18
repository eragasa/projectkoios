# Project Koios contract catalog

This catalog provides one discovery point for cross-repository Project Koios
contracts. Each linked contract remains authoritative in its owning repository.
This repository does not copy component contract text or take over component
acceptance authority.

The contract document is authoritative for its lifecycle status, version,
limitations, and acceptance evidence. Task issues remain authoritative only for
mutable coordination. This catalog intentionally does not duplicate mutable
status or implementation progress.

| Contract ID | Owner | Authoritative contract | Architecture | Parent roadmap |
|---|---|---|---|---|
| `projectkoios.ingestion.clean-transcript` | `projectkoios-ingestion` | [`docs/contracts/clean-transcript-v2.md`](https://github.com/eragasa/projectkoios-ingestion/blob/master/docs/contracts/clean-transcript-v2.md) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) |
| `projectkoios.references.reference-evidence` | `projectkoios-references` | [`docs/contracts/reference-evidence.md`](https://github.com/eragasa/projectkoios-references/blob/master/docs/contracts/reference-evidence.md) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) |
| `projectkoios.search.retrieval-evidence` | `projectkoios-search` | [`docs/contracts/retrieval-evidence.md`](https://github.com/eragasa/projectkoios-search/blob/master/docs/contracts/retrieval-evidence.md) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) |
| `projectkoios.workflow.core` | `projectkoios-workflow` | [`docs/contracts/workflow-core.md`](https://github.com/eragasa/projectkoios-workflow/blob/master/docs/contracts/workflow-core.md) | [Staged workflow-kernel ownership transfer](../adr.20260918.workflow-kernel-transfer.md) | [`WORKFLOW-TRANSFER-01`](https://github.com/eragasa/projectkoios/issues/1) |

## Location convention

Component contracts use:

```text
<owning-repository>/docs/contracts/
```

Each owner directory contains a `README.md` index. Proposed documents state
that they are proposals and carry no implementation or compatibility promise.
Accepted contract versions are identified by the owner document and an exact
acceptance commit.

Cross-repository product architecture remains in Project Koios ADRs. Shared
policies remain under `docs/policies/`. Neither is moved into the contract
catalog.

## Contract metadata

Every contract records:

- stable contract ID;
- owner repository;
- lifecycle status;
- contract version, or `Unassigned` while proposed;
- governing architecture record;
- owner task;
- supersession relationship; and
- known consumers.

Contract identity is distinct from task identity. A task number such as
`SEARCH-EVIDENCE-01` is not a contract version.

## Change discipline

- Change the authoritative document in its owner repository.
- Update this catalog only when ownership, identity, path, architecture, or
  parent-roadmap relationships change.
- Do not copy contract bodies into this repository.
- Do not infer acceptance from issue activity, implementation, tests, or use by
  a consumer.
- Preserve historical commit-pinned links when a contract moves.

Task and recovery rules are defined in
[`docs/policies/task-and-recovery-records.md`](../policies/task-and-recovery-records.md).
