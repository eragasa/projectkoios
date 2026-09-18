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
| `projectkoios-courses` | Course modeling and authoring |
| `projectkoios-ingestion` | Source ingestion and document processing |
| `projectkoios-obsidian` | Obsidian integration and vault management |
| `projectkoios-references` | Reference and citation management |
| `projectkoios-research` | Research-portfolio identity and external-project relationships |
| `projectkoios-search` | Search and indexing |
| `projectkoios-web` | Browser interface |
| `projectkoios-workflow` | Reusable workflow execution |

The operational repository map is maintained in `projectkoios-bootstrap/maps/repositories.md`. Scientific and pedagogical applications such as `physkit`, `msekit`, `ksdft2effmass`, and `dacp2transport` retain their independent ownership and authority.

## Design commitments

- Local-first workflows
- Explicit provenance
- Scientific artifact semantics
- Obsidian-compatible Markdown
- Reproducible transformations
- Model-agnostic LLM harnesses
- Separation between pedagogy code and research code
