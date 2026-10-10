# Search Package Architecture

## Purpose

The `projectkoios.search` package owns deterministic, versioned chunk
derivation, indexing, and retrieval. For citation-aligned page content, chunk
derivation consumes the exact
`projectkoios.ingestion.page.projection.result.PageProjectionResult` contract
and produces Search-owned chunks for downstream Search modules.

This boundary supersedes this page's earlier prototype rule that Search only
receives `TextChunk` objects, does not chunk, and must not import Ingestion.
The first prototype used an in-memory keyword index over `TextChunk`; that
prototype does not define the current cross-repository chunking boundary.

## Package Boundary

The package is responsible for:

* deriving chunks deterministically under an explicit contract version from
  exact `PageProjectionResult` values
* owning the resulting chunk contracts and identities
* storing Search-owned chunks in searchable indexes
* searching chunks by query text
* scoring matching chunks
* returning Search-owned results
* preserving page-projection provenance

The package is not responsible for:

* discovering repositories
* loading files
* coordinating or implementing ingestion
* extracting or projecting text from PDFs
* having chunk derivation index or retrieve
* having chunk derivation publish chunks or source material
* having chunk derivation select or invoke models
* having chunk derivation orchestrate workflows
* composing applications
* building RAG prompts
* calling an LLM
* exposing HTTP endpoints
* exposing MCP tools
* modifying source repositories

## Package Layout

```text
src/python/projectkoios/search/
├── __init__.py
├── models.py
├── protocols.py
├── memory_search_index.py
└── service.py
```

## Core Objects

| Object              | Meaning                                                   | Status  |
| ------------------- | --------------------------------------------------------- | ------- |
| `ChunkSearchResult` | Search result containing a matched `TextChunk` and score. | current |
| `SearchIndex`       | Protocol for searchable chunk indexes.                    | current |
| `MemorySearchIndex` | In-memory keyword search implementation.                  | current |
| `SearchService`     | Application service over a `SearchIndex`.                 | current |

## `ChunkSearchResult`

`ChunkSearchResult` represents one search hit.

```python
@dataclass(frozen=True)
class ChunkSearchResult:
    chunk: TextChunk
    score: float
```

| Field   | Type        | Meaning                                      |
| ------- | ----------- | -------------------------------------------- |
| `chunk` | `TextChunk` | The matched chunk.                           |
| `score` | `float`     | Score assigned by the search implementation. |

The search result preserves the original `TextChunk`, including source path, source kind, language, chunk index, line range, and text.

## `SearchIndex`

`SearchIndex` defines the minimal interface for searchable chunk indexes.

```python
class SearchIndex(Protocol):
    def add_chunks(self, chunks: Iterable[TextChunk]) -> None: ...

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]: ...
```

The protocol allows later search implementations to replace the in-memory implementation without changing the API router, RAG layer, or application service.

## `MemorySearchIndex`

`MemorySearchIndex` stores chunks in memory and performs simple keyword search over chunk text.

It should:

* store chunks added through `add_chunks`
* search chunk text case-insensitively
* return `ChunkSearchResult` objects
* preserve the original `TextChunk`
* sort results by score
* respect the `limit` argument
* return an empty list when no chunks match
* return an empty list for an empty query
* return an empty list for a non-positive limit

The first scoring rule is simple:

```text
score = number of query terms found in the chunk text
```

This scoring rule is not final. It exists to make the search layer executable and testable.

## `SearchService`

`SearchService` is the application service for search operations.

It wraps a `SearchIndex`.

```python
class SearchService:
    def __init__(
        self,
        search_index: SearchIndex | None = None,
    ) -> None: ...

    def add_chunks(self, chunks: Iterable[TextChunk]) -> None: ...

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]: ...
```

If no index is provided, `SearchService` may create a `MemorySearchIndex`.

This keeps the default local application usable while still allowing dependency injection in tests or later application composition.

## Responsibility Split

| Layer | Responsibility |
| --- | --- |
| Ingestion page projection | Produces the exact `PageProjectionResult`. |
| Search chunk derivation | Deterministically derives Search-owned chunks under an explicit version. |
| Search indexing | Stores Search-owned chunks without importing Ingestion. |
| Search retrieval | Ranks and returns Search-owned evidence without importing Ingestion. |
| Applications | Composes cross-capability application calls without translating this leaf contract. |
| Workflow | Owns generic orchestration, state, retries, and authoritative replay. |

Chunk derivation is a narrow Search operation between page projection and the
independent indexing/retrieval modules. It owns only deterministic mapping,
validation, identity, and versioning. It receives no indexing, retrieval,
publication, model-selection or model-execution, application-composition, or
workflow-orchestration authority.

## API Boundary

The search package does not import FastAPI or Pydantic models.

The API layer maps between API models and search models.

API request flow:

```text
SearchRequest
  -> create_search_router
  -> SearchService.search(query, limit)
  -> list[ChunkSearchResult]
  -> list[SearchResult]
```

The API layer owns `SearchRequest` and `SearchResult`.

The search package owns `ChunkSearchResult`.

## Dependency Direction

A narrow production dependency is permitted in one direction only:

```text
projectkoios-search
  -> projectkoios.ingestion.page.projection.result.PageProjectionResult
```

Only the Search chunk-derivation boundary may use that exact leaf contract.
Search indexing and retrieval modules must remain independent of Ingestion, and
`projectkoios-ingestion` must not import `projectkoios-search`. No broader
Ingestion API becomes a Search dependency.

Search consumes the exact owner contract directly. A duplicate DTO and an
Applications-owned translation or mapping layer are rejected for this boundary
unless a later product-architecture review changes the decision. Applications
retains cross-capability composition ownership, and Workflow retains generic
orchestration ownership; neither takes ownership of the leaf value or its
chunk-derivation semantics.

The remaining prohibited directions are:

```text
projectkoios.search -> projectkoios.api
projectkoios.search -> projectkoios.repositories
projectkoios.search -> projectkoios.rag
projectkoios.search -> projectkoios.llm
projectkoios.search -> projectkoios.mcp
projectkoios.ingestion -> projectkoios.search
```

Boundary flow:

```text
Ingestion emits exact PageProjectionResult
  -> Search derives deterministic versioned chunks
  -> independent Search indexing and retrieval consume Search-owned chunks
  -> API and RAG consume Search results
```

## Public API

The current public API is exported from:

```text
projectkoios.search
```

Current public objects:

```python
ChunkSearchResult
SearchIndex
MemorySearchIndex
SearchService
```

Example use:

```python
from projectkoios.search import MemorySearchIndex


index = MemorySearchIndex()
index.add_chunks(chunks)

results = index.search("FastAPI app", limit=5)
```

Example service use:

```python
from projectkoios.search import SearchService


service = SearchService()
service.add_chunks(chunks)

results = service.search("FastAPI app", limit=5)
```

## Tests

Tests belong under:

```text
tests/projectkoios/search/
```

Current test files:

```text
tests/projectkoios/search/test__MemorySearchIndex.py
tests/projectkoios/search/test__SearchService.py
```

Current `MemorySearchIndex` test behaviors:

| Test                                                      | Behavior                                           |
| --------------------------------------------------------- | -------------------------------------------------- |
| `test__add_chunks__stores_chunks`                         | Adds chunks to the index.                          |
| `test__search__returns_matching_chunks`                   | Finds chunks containing query terms.               |
| `test__search__is_case_insensitive`                       | Matches regardless of case.                        |
| `test__search__returns_empty_list_when_no_match`          | Returns no results when nothing matches.           |
| `test__search__respects_limit`                            | Returns at most `limit` results.                   |
| `test__search__preserves_chunk_provenance`                | Returned results contain the original `TextChunk`. |
| `test__search__orders_results_by_score`                   | Higher-scoring chunks are returned first.          |
| `test__search__returns_empty_list_for_empty_query`        | Empty query returns no results.                    |
| `test__search__returns_empty_list_for_non_positive_limit` | Non-positive limit returns no results.             |

Current `SearchService` test behaviors:

| Test                                              | Behavior                                           |
| ------------------------------------------------- | -------------------------------------------------- |
| `test__search__returns_results_from_search_index` | Service returns results from the configured index. |
| `test__search__passes_limit_to_search_index`      | Service passes `limit` to the index.               |

## Package Invariant

The `projectkoios.search` package is valid when it can deterministically
reconstruct equivalent chunks from an exact `PageProjectionResult` under an
explicit version and its independent indexing and retrieval modules can consume
the Search-owned output through stable interfaces.

It must not load files, coordinate Ingestion, broaden the permitted Ingestion
import, publish content, select or invoke models, orchestrate workflows, compose
applications, build RAG prompts, call an LLM, expose API or MCP endpoints, or
modify source repositories.
