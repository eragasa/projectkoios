# Project Koios use cases

Use cases describe user-visible outcomes that cross repository boundaries.
They constrain product behavior without accepting component contracts,
authorizing implementation, or granting authority for private-data effects.

| ID | Use case | Definition status |
|---|---|---|
| `UC-01` | [Evidence-grounded textbook ingestion and RAG](uc-01.evidence-grounded-textbook-ingestion-and-rag.md) | Draft |
| `UC-02` | [Evidence-grounded manuscript development](uc-02.evidence-grounded-manuscript-development.md) | Draft |
| `UC-03` | [Evidence-grounded prospective research](uc-03.evidence-grounded-prospective-research.md) | Draft |

All three use cases apply the living [ingestion](../architecture.ingestion.md),
[search](../architecture.search.md), [agent](../architecture.agents.md), and
[application](../architecture.applications.md) boundaries as applicable. UC-03
also applies the [planned workflow boundary](../architecture.md#planned-architecture)
for bounded planning, execution, and reconciliation.

The use cases are independent product outcomes. They may reuse ingestion,
evidence, retrieval, provenance, workflow, and review contracts, but none is a
prerequisite for another.

Bounded demonstrations are indexed separately in the
[pilot catalog](../pilots/README.md). A pilot definition does not change a use
case's status or authorize execution.
