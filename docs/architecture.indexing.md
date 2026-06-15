# Indexing Package Architecture

## Purpose

The `projectkoios.indexing` package stores `TextChunk` objects and provides a query interface for retrieving matching chunks.

Indexing is the layer between ingestion and retrieval. It receives chunks produced by ingestion and makes them searchable.

The first implementation is an in-memory chunk index. It is intended to make the repository-to-search pipeline testable before adding embeddings, vector databases, or external storage.

## Package Boundary

The package is responsible for:

* accepting `TextChunk` objects
* storing chunks in an index
* searching stored chunks by query text
* returning matching chunks or search results
* preserving chunk provenance

The package is not responsible for:

* loading repositories
* chunking text
* coordinating ingestion
* embedding text
* calling vector databases
* building RAG prompts
* calling an LLM
* exposing HTTP endpoints
* exposing MCP tools
* modifying source repositories

## Package Layout

```text
src/python/projectkoios/indexing/
├── __init__.py
├── models.py
├── protocols.py
└── memory_index.py
```

## Core Objects

| Object              | Meaning                                                | Status  |
| ------------------- | ------------------------------------------------------ | ------- |
| `ChunkSearchResult` | Search result containing a matched chunk and a score.  | planned |
| `ChunkIndex`        | Protocol for objects that can store and search chunks. | planned |
| `MemoryChunkIndex`  | In-memory implementation of `ChunkIndex`.              | planned |

## `ChunkSearchResult`

`ChunkSearchResult` represents one indexed search hit.

```python
@dataclass(frozen=True)
class ChunkSearchResult:
    chunk: TextChunk
    score: float
```

| Field   | Type        | Meaning                                            |
| ------- | ----------- | -------------------------------------------------- |
| `chunk` | `TextChunk` | The matched text chunk.                            |
| `score` | `float`     | Search score assigned by the index implementation. |

For the first in-memory implementation, the score can be a simple keyword match count.

## `ChunkIndex`

`ChunkIndex` defines the minimal index interface.

```python
class ChunkIndex(Protocol):
    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        ...

    def search(self, query: str, *, limit: int = 10) -> list[ChunkSearchResult]:
        ...
```

The protocol allows later index implementations to replace the in-memory index without changing ingestion or RAG code.

Possible later implementations include:

| Implementation     | Role                                                   |
| ------------------ | ------------------------------------------------------ |
| `MemoryChunkIndex` | In-memory keyword index for tests and early local use. |
| `ChromaChunkIndex` | Vector-backed index using ChromaDB.                    |
| `HybridChunkIndex` | Combined lexical and vector retrieval.                 |

Only `MemoryChunkIndex` should be implemented first.

## `MemoryChunkIndex`

`MemoryChunkIndex` stores chunks in memory and performs simple keyword search over chunk text.

It should:

* store chunks added through `add_chunks`
* search chunk text case-insensitively
* return `ChunkSearchResult` objects
* preserve the original `TextChunk`
* respect the `limit` argument
* return an empty list when no chunks match

The first scoring rule may be simple:

```text
score = number of query terms found in the chunk text
```

This scoring rule is not intended to be final. It exists to make the full pipeline executable and testable.

## Responsibility Split

| Layer     | Object                   | Responsibility                                 |
| --------- | ------------------------ | ---------------------------------------------- |
| Ingestion | `CodeRepositoryIngester` | Produces `TextChunk` objects.                  |
| Indexing  | `MemoryChunkIndex`       | Stores chunks and returns matching chunks.     |
| RAG       | later                    | Builds grounded prompts from retrieved chunks. |

The index receives chunks. It does not know how those chunks were produced.

## Dependency Direction

The indexing package may import from:

```text
projectkoios.chunking
```

The indexing package must not import from:

```text
projectkoios.repositories
projectkoios.ingestion
projectkoios.rag
projectkoios.llm
projectkoios.api
projectkoios.mcp
```

Dependency direction:

```text
ingestion produces chunks
indexing stores and searches chunks
rag consumes search results later
```

## Public API

The current public API should be exported from:

```text
projectkoios.indexing
```

Planned public objects:

```python
ChunkIndex
ChunkSearchResult
MemoryChunkIndex
```

Example use:

```python
from projectkoios.indexing import MemoryChunkIndex


index = MemoryChunkIndex()
index.add_chunks(chunks)

results = index.search("FastAPI app", limit=5)
```

## Tests

Tests belong under:

```text
tests/projectkoios/indexing/
```

Initial test file:

```text
tests/projectkoios/indexing/test__MemoryChunkIndex.py
```

Initial test behaviors:

| Test                                             | Behavior                                           |
| ------------------------------------------------ | -------------------------------------------------- |
| `test__add_chunks__stores_chunks`                | Adds chunks to the index.                          |
| `test__search__returns_matching_chunks`          | Finds chunks containing query terms.               |
| `test__search__is_case_insensitive`              | Matches regardless of case.                        |
| `test__search__returns_empty_list_when_no_match` | Returns no results when nothing matches.           |
| `test__search__respects_limit`                   | Returns at most `limit` results.                   |
| `test__search__preserves_chunk_provenance`       | Returned results contain the original `TextChunk`. |

## Package Invariant

The `projectkoios.indexing` package is valid when it can store `TextChunk` objects, search them through a stable interface, and return results without knowing how the chunks were produced.

It must not load files, chunk text, coordinate ingestion, call an LLM, build RAG prompts, expose API endpoints, expose MCP tools, or modify source repositories.
