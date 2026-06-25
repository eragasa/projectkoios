# Project Koios Architecture

## Vision

Project Koios is a local-first technical knowledge system for research, teaching, software development, technical writing, and generated artifacts.

It organizes technical work as connected objects: source materials, knowledge objects, workflow records, computations, generated outputs, and provenance records. The system exists so that work developed in one context can be found, checked, extended, revised, published, or reused in another context without reconstructing the path from memory.

Project Koios exposes this system through multiple interfaces. FastAPI provides an HTTP interface. Command-line tools support direct local operations. Notebooks support scientific and exploratory workflows. A web interface can support browsing, search, review, and artifact inspection. Future local services can expose the same underlying object model through additional protocols.

LLMs operate inside this architecture as assistive components. They support retrieval, synthesis, drafting, coding, and review. Their outputs remain tied to source objects, retrieval context, and provenance records.

The current practical target is a RAG-supported LLM coding workflow for local Python repositories. Later targets include scientific notes, references, teaching materials, workflows, generated artifacts, and public outputs.

Project Koios keeps the human in control by making source material, intermediate objects, generated outputs, and provenance inspectable.

## Architecture Status

Project Koios distinguishes between the current repository architecture and the planned system architecture.

The current architecture is intentionally small enough to run, test, and understand immediately.

The planned architecture describes the expansion path after the Python package, API boundary, and search model stabilize.

## Current Architecture

The current repository is a Python package repository.

```text
projectkoios/
├── pyproject.toml
├── README.md
├── docs/
│   └── architecture.md
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

The current implementation uses Python as the primary implementation language.

| Layer               | Current status                                  |
| ------------------- | ----------------------------------------------- |
| Python package      | Primary implementation layer.                   |
| FastAPI API         | Initial interface for health checks and search. |
| SQLite / FTS        | Planned next step for local search storage.     |
| TypeScript web UI   | Not yet implemented.                            |
| Rust infrastructure | Not yet implemented.                            |

The current design rule is:

```text
Project Koios is a Python package first.
FastAPI is an adapter, not the system.
```

## Current Namespace Layout

`projectkoios` is the top-level namespace for the knowledge management system.

| Namespace                 | Purpose                                                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `projectkoios.core`       | Generic infrastructure used across the system: configuration, paths, IDs, serialization, validation, and shared utilities.                   |
| `projectkoios.vault`      | Local Obsidian / Markdown knowledge-base management: vault scanning, front matter parsing, Markdown parsing, links, tags, and note metadata. |
| `projectkoios.search`     | Indexing, full-text search, vector search, ranking, chunking, and retrieval.                                                                 |
| `projectkoios.references` | Reference management: BibTeX records, PDFs, citation keys, source metadata, and reference ingestion.                                         |
| `projectkoios.workflow`   | Tasks, states, process objects, workflow graphs, provenance, and generated artifacts.                                                        |
| `projectkoios.api`        | FastAPI interface over the Project Koios system.                                                                                             |

The Python package avoids a flat structure such as:

```text
projectkoios/
├── main.py
├── models.py
└── search.py
```

That layout makes the web API appear to be the system. The API lives inside `projectkoios.api`, while stable application logic lives in the domain packages.

## Current Python Package Layout

```text
src/python/projectkoios/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── ids.py
│   └── paths.py
├── vault/
│   ├── __init__.py
│   ├── scanner.py
│   ├── markdown.py
│   └── frontmatter.py
├── search/
│   ├── __init__.py
│   ├── commands.py
│   ├── documents.py
│   ├── engine.py
│   └── results.py
├── references/
│   ├── __init__.py
│   ├── bibtex.py
│   └── schemas.py
├── workflow/
│   ├── __init__.py
│   ├── tasks.py
│   ├── states.py
│   └── provenance.py
└── api/
    ├── __init__.py
    ├── main.py
    ├── models.py
    └── routes/
        ├── __init__.py
        ├── health.py
        └── search.py
```

## Current API Boundary

FastAPI is a thin adapter over the Project Koios application services.

The API layer performs the following sequence:

```text
HTTP JSON request
    ↓
validate request
    ↓
convert to application command
    ↓
call application service
    ↓
convert result to response model
    ↓
HTTP JSON response
```

The API layer does not own search logic, vault parsing, workflow semantics, reference ingestion, or provenance rules.

A route has this shape:

```python
@router.post("/search")
def search(request: SearchRequest) -> list[SearchResult]:
    command = request_to_command(request)
    hits = search_service.search(command)
    return [hit_to_response(hit) for hit in hits]
```

The search engine is usable from:

```text
CLI
notebooks
tests
local scripts
future desktop app
future service in another language
```

The portability test is:

```text
Can search run without importing FastAPI?
```

If yes, the boundary is healthy.

## Pydantic Boundary

Pydantic is used at system boundaries, especially API request and response models.

Pydantic is used for:

```text
API input models
API output models
configuration models
validation-heavy schemas
OpenAPI schema generation
```

Dataclasses and ordinary classes are used for internal domain objects.

| Object type          | Preferred implementation  |
| -------------------- | ------------------------- |
| API request/response | Pydantic model            |
| Configuration schema | Pydantic model            |
| Parsed note          | Dataclass                 |
| Search command       | Dataclass                 |
| Search hit           | Dataclass                 |
| Workflow state       | Dataclass or domain class |
| Search engine        | Ordinary class            |
| Vault scanner        | Ordinary class            |
| Indexer              | Ordinary class            |

Example internal search command:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class SearchCommand:
    query: str
    limit: int = 20
    object_types: tuple[str, ...] = ()
```

Example internal search hit:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class SearchHit:
    document_id: str
    chunk_id: str | None
    title: str
    path: str
    object_type: str
    snippet: str
    score: float
    metadata: dict
```

Example API model:

```python
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    limit: int = Field(default=20, ge=1, le=100)
    object_types: list[str] | None = None
```

The conversion layer is explicit.

```python
def request_to_command(request: SearchRequest) -> SearchCommand:
    return SearchCommand(
        query=request.query,
        limit=request.limit,
        object_types=tuple(request.object_types or ()),
    )
```

## Current Search Target

The first useful search implementation is local, explicit, and inspectable.

```text
vault path
    ↓
scan Markdown files
    ↓
extract document records
    ↓
insert into SQLite
    ↓
query SQLite FTS5
    ↓
return search hits
```

The initial search stack is:

```text
local files
SQLite
SQLite FTS5
Markdown scanner
section-aware chunks
```

The first API target is:

```text
GET /health
POST /search
```

## Planned Architecture

The planned architecture is a local-first multi-layer system.

```text
projectkoios/
├── README.md
├── docs/
│   └── architecture.md
├── python/
│   ├── pyproject.toml
│   ├── README.md
│   ├── dev/
│   ├── tests/
│   └── src/
│       └── python/
│           └── projectkoios/
├── web/
│   ├── package.json
│   ├── index.html
│   └── src/
└── rust/
    ├── Cargo.toml
    └── crates/
```

The planned architecture is implemented incrementally as concrete needs appear.

The planned system layers are:

| Layer            | Primary language | Responsibility                                                                                               |
| ---------------- | ---------------: | ------------------------------------------------------------------------------------------------------------ |
| Python layer     |           Python | Scientific workflows, LLM orchestration, API adapters, notebooks, content generation, search prototypes.     |
| TypeScript layer |       TypeScript | Human interface: search UI, note browser, workflow dashboard, review tools, artifact preview.                |
| Rust layer       |             Rust | Fast local infrastructure: file scanning, indexing, chunking, hashing, search daemon, portable CLI binaries. |

The intended evolution is:

```text
Python first
    ↓
TypeScript interface
    ↓
Rust infrastructure where needed
```

## Planned Search Architecture

Search is layered.

```text
keyword search
    ↓
metadata filtering
    ↓
semantic search
    ↓
ranking
    ↓
context assembly
```

The search system indexes workflow objects, not only text files.

Searchable objects include:

```text
notes
sections
references
PDF metadata
source files
code blocks
equations
tasks
workflow states
generated artifacts
figures
provenance records
```

The search implementation evolves through the following stages:

| Stage | Capability                                                           |
| ----: | -------------------------------------------------------------------- |
|     1 | Markdown file scanner and document table.                            |
|     2 | SQLite FTS5 keyword search.                                          |
|     3 | Section-aware chunking.                                              |
|     4 | Metadata filters using front matter, paths, tags, and object types.  |
|     5 | Vector embeddings and semantic retrieval.                            |
|     6 | Hybrid ranking.                                                      |
|     7 | Graph-aware ranking using links, references, courses, and workflows. |
|     8 | RAG context assembly with provenance.                                |

## TypeScript Layer

The TypeScript layer owns the human interface.

It includes:

```text
search UI
note browser
workflow dashboard
artifact preview
source/result inspection
manual curation tools
settings UI
review tools
```

It does not own canonical knowledge-management logic.

TypeScript is not the source of truth for:

```text
vault parsing rules
citation logic
search ranking
workflow state semantics
scientific computation
LLM prompt assembly
provenance semantics
```

A practical frontend layout is:

```text
web/
├── package.json
├── index.html
└── src/
    ├── main.tsx
    ├── api/
    ├── components/
    ├── pages/
    ├── types/
    └── state/
```

The frontend interacts through stable API contracts.

Example TypeScript DTOs:

```ts
export type SearchRequest = {
  query: string;
  limit?: number;
  object_types?: string[] | null;
};

export type SearchResult = {
  document_id: string;
  chunk_id: string | null;
  title: string;
  path: string;
  object_type: string;
  snippet: string;
  score: number;
  metadata: Record<string, unknown>;
};
```

The browser UI calls the Python API through HTTP or WebSocket initially.

```text
TypeScript UI
    ↓ HTTP / WebSocket
Python FastAPI adapter
    ↓ application services
Project Koios domain layer
    ↓ storage / index
SQLite / files / vector index
```

## Rust Layer

Rust is introduced when the Python implementation proves the model and a performance-critical subsystem becomes clear.

Rust targets include:

```text
fast vault scanner
file watcher
Markdown chunker
content hashing
deduplication
SQLite/FTS indexer
local search daemon
portable CLI binaries
parallel ingestion
```

The useful boundary is:

```text
Python asks:
    search("Bloch boundary conditions")

Rust handles:
    scan files
    parse chunks
    search index
    rank candidates
    return structured hits
```

Python remains responsible for:

```text
LLM orchestration
prompt assembly
citation formatting
artifact generation
notebooks
scientific computation
FastAPI response conversion
```

## Storage Layer

Initial storage is simple and local.

```text
local files
SQLite
SQLite FTS5
```

Later storage additions include:

```text
vector index
content hashes
artifact registry
provenance graph
reference database
```

Storage responsibilities:

| Storage object                     | Purpose                                        |
| ---------------------------------- | ---------------------------------------------- |
| Markdown files                     | Human-readable source notes.                   |
| SQLite documents table             | Indexed document metadata and body text.       |
| SQLite FTS5 table                  | Keyword search.                                |
| Chunk table                        | Section-aware retrieval.                       |
| Embedding table or vector database | Semantic search.                               |
| Link table                         | Backlinks, graph traversal, and ranking.       |
| Provenance table                   | Artifact generation and workflow traceability. |

## Development Flow

Code moves through stages.

```text
dev/ experiment
    ↓
tests/ specify expected behavior
    ↓
src/python/projectkoios/ implement stable package code
```

The application does not import from `dev/`.

| Path              | Purpose                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `dev/`            | Scratch space for experiments, spikes, temporary scripts, exploratory notebooks, and design notes that are not yet stable enough for `src/`. |
| `dev/api/`        | FastAPI route experiments, request/response sketches, and temporary server tests.                                                            |
| `dev/search/`     | Search experiments: FTS, vector indexing, ranking, chunking, and query prototypes.                                                           |
| `dev/vault/`      | Vault scanner experiments, Markdown parsing tests, front matter extraction, link extraction, and file traversal scripts.                     |
| `dev/references/` | BibTeX, PDF, citation-key, and reference-ingestion experiments.                                                                              |
| `dev/workflow/`   | Task/state/process/provenance experiments before formalizing them into package code.                                                         |
| `tests/`          | Python tests for stable source code under `src/python/projectkoios/`.                                                                        |

## Interface Strategy

Project Koios supports multiple interfaces over the same application services.

| Interface            | Purpose                                                               |
| -------------------- | --------------------------------------------------------------------- |
| FastAPI              | HTTP API for frontend, local tools, and automation.                   |
| CLI                  | Direct local use, indexing, debugging, and scripts.                   |
| Notebooks            | Scientific modeling, teaching workflows, and exploratory computation. |
| Web UI               | Search, review, browsing, and workflow control.                       |
| Future desktop shell | Local-first app interface if needed.                                  |

The same domain services power all interfaces.

```text
CLI
Web API
notebook
desktop UI
    ↓
application services
    ↓
domain objects
    ↓
storage / index
```

## Portability Rule

The system is portable by construction.

The API layer can be ported to another language when the system obeys these rules:

```text
Keep FastAPI thin.
Keep Pydantic at the boundary.
Keep domain objects independent of the web framework.
Keep storage formats explicit.
Keep application services callable without HTTP.
Keep TypeScript as UI, not domain authority.
Introduce Rust only behind stable internal interfaces.
```

The main portability risk is letting framework objects become the domain model.

Avoid this:

```text
FastAPI route
    owns search semantics
    owns workflow semantics
    owns storage details
```

Prefer this:

```text
FastAPI route
    validates request
    calls service
    returns response
```

## Initial Build Target

The first useful Project Koios build is:

```text
Python package
FastAPI health endpoint
FastAPI search endpoint
Markdown scanner
SQLite document table
SQLite FTS5 index
basic search results
```

Minimum working API:

```text
GET /health
POST /search
```

Minimum working internal flow:

```text
vault path
    ↓
scan Markdown files
    ↓
extract document records
    ↓
insert into SQLite
    ↓
query SQLite FTS5
    ↓
return search hits
```

## Architecture Summary

Project Koios evolves as:

```text
Python first
    establish object model, API, search semantics, workflow semantics

TypeScript next
    make search, browsing, review, and workflow interaction usable

Rust later
    accelerate file scanning, indexing, hashing, and local search infrastructure
```

The architectural center is not a framework. The center is the Project Koios namespace and its domain model.

```text
projectkoios.core
projectkoios.vault
projectkoios.search
projectkoios.references
projectkoios.workflow
projectkoios.api
```

The primary design constraint is that the knowledge system remains inspectable, local-first, and portable across interfaces.

## Data Transfer Objects

Project Koios uses explicit data-transfer objects between layers.

Pydantic models are used at external boundaries. Dataclasses are used for internal domain and application objects.

| Layer | Object type | Purpose |
|---|---|---|
| `projectkoios.api.models` | Pydantic models | HTTP request and response schemas, validation, serialization, and OpenAPI documentation. |
| `projectkoios.search.models` | Dataclasses | Internal search queries, hits, ranking inputs, and retrieval results. |
| `projectkoios.repositories.models` | Dataclasses | Repository files and source metadata. |
| `projectkoios.chunking.models` | Dataclasses | Text/code chunks and chunk offsets. |
| `projectkoios.rag.models` | Dataclasses | Retrieved context, prompt inputs, and prompt outputs. |
| `projectkoios.llm.models` | Dataclasses or Pydantic models | Internal LLM requests/responses; Pydantic only when validating provider JSON boundaries. |

The API layer translates between HTTP-facing Pydantic models and internal dataclass models.

```text
HTTP JSON
    ↓
Pydantic API model
    ↓
conversion function
    ↓
dataclass domain model
    ↓
service
    ↓
dataclass result
    ↓
conversion function
    ↓
Pydantic API response
    ↓
HTTP JSON
```


|                                 |     |
| ------------------------------- | --- |
| [[architecture.repositories]]   |     |
| [[architecture.rag]]            |     |
| [[architecture.rag.repository]] |     |
