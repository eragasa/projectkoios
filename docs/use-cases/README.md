# Project Koios use cases

Use cases describe user-visible outcomes that cross repository boundaries.
They constrain product behavior without accepting component contracts,
authorizing implementation, or granting authority for private-data effects.

| ID | Use case | Definition status |
|---|---|---|
| `UC-01` | [Evidence-grounded textbook ingestion and RAG](uc-01.evidence-grounded-textbook-ingestion-and-rag.md) | Draft |
| `UC-02` | [Evidence-grounded manuscript and course-note development](uc-02.evidence-grounded-manuscript-development.md) | Draft |
| `UC-03` | [Evidence-grounded prospective research](uc-03.evidence-grounded-prospective-research.md) | Draft |

UC-01 applies the living [ingestion](../architecture.ingestion.md) and
[search](../architecture.search.md) boundaries. UC-02 applies the
[evidence-grounded long-form authoring](../architecture/v0/index.md#evidence-grounded-long-form-authoring)
design. UC-03 applies [search](../architecture.search.md),
[application](../architecture.applications.md), and the
[planned workflow boundary](../architecture.md#planned-architecture) for
bounded planning, execution, and reconciliation.

The use cases are independent product outcomes. They may reuse ingestion,
evidence, retrieval, provenance, workflow, and review contracts, but none is a
prerequisite for another.

Bounded demonstrations are indexed separately in the
[pilot catalog](../pilots/README.md). A pilot definition does not change a use
case's status or authorize execution.
