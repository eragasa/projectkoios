# Project Koios

Project Koios is a local-first knowledge, modeling, and agentic workflow platform for scientific teaching and research.

It organizes notes, references, code, computational workflows, and generated artifacts using explicit schemas, provenance records, and reproducible transformations.

## Components

| Repository | Role |
|---|---|
| `projectkoios-agent` | Local-first LLM harness and agent runtime |
| `projectkoios-vault` | Obsidian vault indexing, validation, and transformations |
| `projectkoios-ingest` | PDF, BibTeX, Markdown, and reference ingestion |
| `projectkoios-schemas` | Shared artifact, provenance, note, and workflow schemas |
| `projectkoios-cli` | Top-level `projectkoios` command |
| `physkit` | Pedagogical physics code |
| `msekit` | Research materials-science code |

## Design commitments

- Local-first workflows
- Explicit provenance
- Scientific artifact semantics
- Obsidian-compatible Markdown
- Reproducible transformations
- Model-agnostic LLM harnesses
- Separation between pedagogy code and research code
