# Architecture proposals and roadmaps

This index points to active cross-repository architecture proposals and their
mutable coordination records. The linked ADR is authoritative for stable
architecture content. The linked parent issue is authoritative only for the
mutable cross-repository task graph.

A proposed ADR is not accepted architecture, implementation authorization, a
release decision, or scientific approval.

| Program | Architecture record | ADR status | Parent roadmap |
|---|---|---|---|
| Evidence-grounded scientific retrieval | [`ADR20260918`](adr.20260918.evidence-grounded-scientific-rag.md) | Proposed | [`RAG-ROADMAP-01`](https://github.com/eragasa/projectkoios/issues/2) |
| Workflow-kernel ownership transfer | [`ADR20260918`](adr.20260918.workflow-kernel-transfer.md) | Proposed | [`WORKFLOW-TRANSFER-01`](https://github.com/eragasa/projectkoios/issues/1) |
| Workflow and CPN development tracks | [`ADR20260920`](adr.20260920.workflow-and-cpn-development-tracks.md) | Accepted | [`WORKFLOW-TRANSFER-01`](https://github.com/eragasa/projectkoios/issues/1) |

## Accepted cross-repository decisions used by active programs

| Decision | Architecture record | Coordination record |
|---|---|---|
| Reference authority, identity, and projection direction | [Reference authority and projection architecture](adr.20260918.reference-authority-and-projections.md) | [`REFERENCES-ARCHITECTURE-01`](https://github.com/eragasa/projectkoios/issues/3) |

Owner-repository contracts are discoverable through the
[`Project Koios contract catalog`](contracts/README.md). Task and fresh-session
recovery rules are defined in
[`policies/task-and-recovery-records.md`](policies/task-and-recovery-records.md).
Repository routing remains in
`projectkoios-bootstrap/maps/repositories.md`.

## Accepted cross-repository baselines relevant to these proposals

- [`ADR20260917: Apache License 2.0`](adr.20260917.apache-2.0-license.md)
- [`ADR20260917: Python 3.14 baseline`](adr.20260917.python-3.14-baseline.md)

Acceptance or rejection of an active proposal is recorded by changing the ADR
status through a separately authorized commit. Issue activity alone does not
change architecture status.
