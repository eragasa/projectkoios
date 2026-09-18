# Project Koios cross-repository contract catalog

This catalog provides one discovery point for contracts consumed across Project
Koios repository boundaries. It is intentionally not an inventory of every
owner-internal type, schema, processor configuration, or cache format.

Each linked contract remains authoritative in its owning repository. This
repository owns global contract-ID uniqueness and discovery only; it does not
copy component contract text or take over component semantics or acceptance
authority.

Contract identity, pre-release versioning, lifecycle, compatibility, and
conformance follow the
[`contract governance policy`](../policies/contracts.md). Task and recovery
authority follow the
[`task and recovery policy`](../policies/task-and-recovery-records.md).

| Contract ID | Owner | Current authoritative document | Architecture | Parent roadmap | Accepted baseline |
|---|---|---|---|---|---|
| `projectkoios.ingestion.clean-transcript` | `projectkoios-ingestion` | [`clean-transcript-v2.md`](https://github.com/eragasa/projectkoios-ingestion/blob/master/docs/contracts/clean-transcript-v2.md#contract-metadata-clean-transcript) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.ingestion.transcript-batch-plan` | `projectkoios-ingestion` | [`clean-transcript-v2.md`](https://github.com/eragasa/projectkoios-ingestion/blob/master/docs/contracts/clean-transcript-v2.md#contract-metadata-transcript-batch-plan) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.references.candidate-manifest` | `projectkoios-references` | [`reference-evidence.md`](https://github.com/eragasa/projectkoios-references/blob/master/docs/contracts/reference-evidence.md#contract-metadata-candidate-manifest) | [Reference authority and projections](../adr.20260918.reference-authority-and-projections.md); [evidence-grounded retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.references.claim-locator` | `projectkoios-references` | [`reference-evidence.md`](https://github.com/eragasa/projectkoios-references/blob/master/docs/contracts/reference-evidence.md#contract-metadata-claim-locator) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.search.evidence-unit` | `projectkoios-search` | [`retrieval-evidence.md`](https://github.com/eragasa/projectkoios-search/blob/master/docs/contracts/retrieval-evidence.md#contract-metadata-evidence-unit) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.search.evidence-bundle` | `projectkoios-search` | [`retrieval-evidence.md`](https://github.com/eragasa/projectkoios-search/blob/master/docs/contracts/retrieval-evidence.md#contract-metadata-evidence-bundle) | [Evidence-grounded scientific retrieval](../adr.20260918.evidence-grounded-scientific-rag.md) | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) | None |
| `projectkoios.workflow.core` | `projectkoios-workflow` | [`workflow-core.md`](https://github.com/eragasa/projectkoios-workflow/blob/master/docs/contracts/workflow-core.md#contract-metadata) | [Staged workflow-kernel ownership transfer](../adr.20260918.workflow-kernel-transfer.md) | [`WORKFLOW-TRANSFER-01`](https://github.com/eragasa/projectkoios/issues/1) | None |

Default-branch links locate the current proposal. Only an exact commit link in
the `Accepted baseline` column identifies an accepted immutable specification.
No listed contract currently has an accepted baseline.

## Location convention

Component contracts use:

```text
<owning-repository>/docs/contracts/
```

Each owner directory contains a `README.md` index. One document may contain a
suite, but every independently versioned contract has its own metadata,
normative scope, and conformance subjects.

Cross-repository architecture remains in Project Koios ADRs. Shared policies
remain under `docs/policies/`. Neither is moved into the contract catalog.

## Registration and change discipline

- The catalog reserves contract-ID uniqueness when a row is added.
- The owner repository controls contract content and proposes lifecycle
  transitions.
- Proposed contracts use target versions below `1.0.0`; Project Koios has no
  formal stable contract release.
- Change the authoritative document in its owner repository.
- Update this catalog only when identity, ownership, path, architecture,
  roadmap, or accepted baseline changes.
- Do not copy contract bodies into this repository.
- Do not infer acceptance from issue activity, implementation, tests, or use by
  a consumer.
- Preserve historical commit-pinned links when a contract moves.

## Legacy and owner-internal contracts

`projectkoios-ingestion/docs/contracts.md` remains a legacy aggregate of
implemented owner-internal ingestion contracts. It is not silently renumbered
or treated as an accepted release under this cross-repository governance
policy. Relevant boundaries enter this catalog through explicit IDs and
pre-release target versions.
