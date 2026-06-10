# Project Koios

Project Koios is a knowledge management and content generation system for technical and scientific workflows. It is built primarily for my work as a researcher, lecturer, and technical tinkerer.

The system is organized around local knowledge objects: notes, references, source files, tasks, workflows, generated artifacts, and provenance records.

## Installation

From the repository root:

```bash
cd projectkoios

python3 -m venv .venv
source .venv/bin/activate

pip install -e .
```

For development dependencies

```bash
pip install -e ".[dev]"
```

Run the API server

```
uvicorn projectkoios.api.main:app -reload
```

Check the server
```
curl http://127.0.0.1:8000/health
```

## Folder Layout

```text
projectkoios/
├── pyproject.toml
├── README.md
├── dev/
├── tests/
└── src/
    └── python/
        └── projectkoios/
            ├── __init__.py
            ├── core/
            ├── vault/
            ├── search/
            ├── references/
            ├── workflow/
            └── api/
```

## Namespace Layout

`projectkoios` is the top-level namespace for the whole knowledge management system.

| Namespace | Purpose |
|---|---|
| `projectkoios.core` | Generic infrastructure used across the system: configuration, paths, IDs, serialization, validation, and shared utilities. |
| `projectkoios.vault` | Local Obsidian / Markdown knowledge-base management: vault scanning, front matter parsing, Markdown parsing, links, tags, and note metadata. |
| `projectkoios.search` | Indexing, full-text search, vector search, ranking, chunking, and retrieval. |
| `projectkoios.references` | Reference management: BibTeX records, PDFs, citation keys, source metadata, and reference ingestion. |
| `projectkoios.workflow` | Tasks, states, process objects, workflow graphs, provenance, and generated artifacts. |
| `projectkoios.api` | FastAPI interface over the Project Koios system. |

## Development Layout

| Path | Purpose |
|---|---|
| `dev/` | Scratch space for experiments, spikes, temporary scripts, exploratory notebooks, and design notes that are not yet stable enough for `src/`. |
| `tests/` | Python tests for the source package. |

