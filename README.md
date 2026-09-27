# Project Koios

Project Koios is a local-first knowledge, modeling, and agentic workflow platform for scientific teaching and research.

It organizes notes, references, code, computational workflows, and generated artifacts using explicit schemas, provenance records, and reproducible transformations.

## Components

| Repository | Role |
|---|---|
| `projectkoios` | Product architecture and cross-repository decisions |
| `projectkoios-bootstrap` | Multi-repository operational coordination and Project Koios-specific Pi harness incubation |
| `projectkoios-agent` | Deferred reusable agent-domain components |
| `projectkoios-api` | HTTP API and runtime boundary |
| `projectkoios-applications` | Workflow/CPN-enabled cross-capability application composition |
| `projectkoios-courses` | Course modeling and authoring |
| `projectkoios-ingestion` | Source ingestion and document processing |
| `projectkoios-obsidian` | Obsidian integration and vault management |
| `projectkoios-references` | Reference and citation management |
| `projectkoios-research` | Research-portfolio identity and external-project relationships |
| `projectkoios-search` | Search and indexing |
| `projectkoios-simulations` | Neutral simulation abstractions and provider integrations |
| `projectkoios-web` | Browser interface |
| `projectkoios-workflow` | Generic workflow runtime, state, engine, and CPN contracts |

The operational repository map is maintained in
`projectkoios-bootstrap/maps/repositories.md`. The
[application architecture](docs/architecture.applications.md) defines the
shared `projectkoios.applications` owner and its reusable-component boundary.
`projectkoios.applications.pw_dft_scf` is a capability package under that owner,
not a standalone repository. The [adapter architecture](docs/architecture.adapters.md)
defines the documentation taxonomy, and the
[Frankenstein architecture](docs/architecture.frankenstein.md) records the
current bounded incubation and provenance disposition. Independently governed
scientific and pedagogical projects such as `physkit`, `msekit`,
`ksdft2effmass`, and `dacp2transport` retain their own ownership and authority.

## Product use cases

Cross-repository product outcomes are defined in the
[use-case catalog](docs/use-cases/README.md). Use cases state what users need to
accomplish without replacing architecture decisions, component contracts, or
project-specific research records.

The current independent use cases cover:

1. evidence-grounded textbook ingestion and RAG;
2. evidence-grounded manuscript development; and
3. evidence-grounded prospective research.

Bounded cross-repository demonstrations are defined separately in the
[pilot catalog](docs/pilots/README.md). Pilot definitions do not authorize
execution or replace component contracts and private run evidence.

## Schema registry

Published and cross-repository JSON Schemas are discoverable through the
[mothership schema registry](schemas/README.md). The registry records canonical
URL-shaped identities and exact local content identities. Those URLs are not
claimed to resolve over HTTP until separately published, and validators resolve
schemas locally without implicit network access.

## Design commitments

- Local-first workflows
- Explicit provenance
- Scientific artifact semantics
- Obsidian-compatible Markdown
- Reproducible transformations
- Model-agnostic LLM harnesses
- Separation between pedagogy code and research code
