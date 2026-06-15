# Search Package Architecture

## Purpose

The `projectkoios.search` package provides search over `TextChunk` objects.

Search is the layer that receives chunks, stores them in a searchable structure, and returns matching chunks as search results.

The first implementation is an in-memory keyword search index. It exists to make the pipeline executable and testable before adding SQLite FTS, vector search, hybrid retrieval, or external databases.

## Package Boundary

The package is responsible for:

* accepting `TextChunk` objects
* storing chunks in a searchable index
* searching chunks by query text
* scoring matching chunks
* returning `ChunkSearchResult` objects
* preserving chunk provenance

The package is not responsible for:

* discovering repositories
* loading files
* chunking text
* coordinating ingestion
* extracting text from PDFs
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
    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        ...

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]:
        ...
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
    ) -> None:
        ...

    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        ...

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]:
        ...
```

If no index is provided, `SearchService` may create a `MemorySearchIndex`.

This keeps the default local application usable while still allowing dependency injection in tests or later application composition.

## Responsibility Split

| Layer          | Object                   | Responsibility                                                         |
| -------------- | ------------------------ | ---------------------------------------------------------------------- |
| Ingestion      | `CodeRepositoryIngester` | Produces `TextChunk` objects.                                          |
| Search         | `MemorySearchIndex`      | Stores chunks and returns matching chunks.                             |
| Search service | `SearchService`          | Provides application-level access to a `SearchIndex`.                  |
| API            | `create_search_router`   | Converts API request/response models to and from search service calls. |
| RAG            | later                    | Builds grounded prompts from search results.                           |

The search package receives chunks. It does not know how those chunks were produced.

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

The search package may import from:

```text
projectkoios.chunking
```

The search package must not import from:

```text
projectkoios.api
projectkoios.repositories
projectkoios.ingestion
projectkoios.rag
projectkoios.llm
projectkoios.mcp
```

Dependency direction:

```text
chunking produces TextChunk
ingestion supplies TextChunk objects to search
search returns ChunkSearchResult
api and rag consume search results
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

The `projectkoios.search` package is valid when it can store `TextChunk` objects, search them through a stable interface, and return `ChunkSearchResult` objects without knowing how the chunks were produced.

It must not load files, chunk text, coordinate ingestion, build RAG prompts, call an LLM, expose API endpoints, expose MCP tools, or modify source repositories.
