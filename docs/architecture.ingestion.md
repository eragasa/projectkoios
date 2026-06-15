# Ingestion Package Architecture

## Purpose

The `projectkoios.ingestion` package coordinates source loading and chunking.

Ingestion turns loaded source objects into `TextChunk` objects that can later be indexed, searched, cited, or passed into RAG.

The package does not define repository models or chunk models. It uses existing loaders and chunkers.

The first implemented ingester is `CodeRepositoryIngester`.

## Package Boundary

The package is responsible for:

* receiving a source repository object
* calling the appropriate repository loader
* passing loaded source text to a chunker
* yielding `TextChunk` objects
* preserving source provenance from loaded files into chunks

The package is not responsible for:

* discovering repository roots
* loading files directly
* defining source file models
* defining chunk models
* indexing chunks
* searching chunks
* embedding chunks
* ranking chunks
* building RAG prompts
* calling an LLM
* exposing HTTP endpoints
* exposing MCP tools
* modifying source repositories

## Package Layout

```text
src/python/projectkoios/ingestion/
├── __init__.py
└── code_repository_ingester.py
```

## Core Objects

| Object                   | Meaning                                                                     | Status  |
| ------------------------ | --------------------------------------------------------------------------- | ------- |
| `CodeRepositoryIngester` | Coordinates `CodeRepositoryLoader` and `LineChunker` for code repositories. | current |

## Responsibility Split

| Layer          | Object                   | Responsibility                                                    |
| -------------- | ------------------------ | ----------------------------------------------------------------- |
| Source loading | `CodeRepositoryLoader`   | Loads `CodeFile` objects from a `CodeRepository`.                 |
| Chunking       | `LineChunker`            | Converts text into `TextChunk` objects.                           |
| Ingestion      | `CodeRepositoryIngester` | Calls the loader and chunker to produce chunks from a repository. |

The ingester owns the loop over source files.

The loader does not know about chunking.

The chunker does not know about repositories.

## `CodeRepositoryIngester`

`CodeRepositoryIngester` converts a `CodeRepository` into an iterator of `TextChunk` objects.

It receives its dependencies explicitly:

| Dependency             | Role                                                |
| ---------------------- | --------------------------------------------------- |
| `CodeRepositoryLoader` | Provides `CodeFile` objects.                        |
| `LineChunker`          | Converts each file’s text into `TextChunk` objects. |

Current constructor shape:

```python
class CodeRepositoryIngester:
    def __init__(
        self,
        loader: CodeRepositoryLoader,
        chunker: LineChunker,
    ) -> None:
        ...
```

Current ingestion method shape:

```python
def iter_chunks(
    self,
    repository: CodeRepository,
) -> Iterator[TextChunk]:
    ...
```

The method:

1. calls `loader.iter_files(repository)`
2. iterates over each `CodeFile`
3. calls `chunker.chunk_text(...)`
4. yields each `TextChunk`

## Provenance Mapping

The ingester maps `CodeFile` fields into chunk provenance.

| `CodeFile` field | `TextChunk` field           |
| ---------------- | --------------------------- |
| `relative_path`  | `source_path`               |
| `language`       | `language`                  |
| file role        | `source_kind = "code_file"` |
| `text`           | input to chunker            |

The ingester uses repository-relative paths, not absolute file paths, for `TextChunk.source_path`.

## Dependency Direction

The ingestion package may import from:

```text
projectkoios.repositories.code
projectkoios.chunking
```

The following packages must not import from `projectkoios.ingestion`:

```text
projectkoios.repositories.code
projectkoios.chunking
```

Dependency direction:

```text
ingestion imports repositories and chunking
repositories do not import ingestion
chunking does not import ingestion
```

## Public API

The current public API is exported from:

```text
projectkoios.ingestion
```

Current public objects:

```python
CodeRepositoryIngester
```

Example use:

```python
from projectkoios.chunking import LineChunker
from projectkoios.ingestion import CodeRepositoryIngester
from projectkoios.repositories.code import CodeRepositoryLoader


ingester = CodeRepositoryIngester(
    loader=CodeRepositoryLoader(),
    chunker=LineChunker(),
)

chunks = ingester.iter_chunks(repository)
```

## Tests

Tests belong under:

```text
tests/projectkoios/ingestion/
```

Current test file:

```text
tests/projectkoios/ingestion/test__CodeRepositoryIngester.py
```

Current test behaviors:

| Test                                                    | Behavior                                            |
| ------------------------------------------------------- | --------------------------------------------------- |
| `test__iter_chunks__yields_chunks_from_code_repository` | Loads code files and yields text chunks.            |
| `test__iter_chunks__preserves_relative_source_path`     | Uses `CodeFile.relative_path` as chunk source path. |
| `test__iter_chunks__sets_source_kind_to_code_file`      | Sets `source_kind` to `code_file`.                  |
| `test__iter_chunks__preserves_language`                 | Preserves file language on each chunk.              |

Tests should use temporary directories and the real `CodeRepositoryLoader` and `LineChunker`.

## Package Invariant

The `projectkoios.ingestion` package is valid when it can coordinate source loading and chunking without taking ownership of either concern.

It must not load files directly, define chunking strategy, index chunks, search chunks, call an LLM, expose API endpoints, expose MCP tools, or modify repository contents.
