# Ingestion Package Architecture

## Purpose

The `projectkoios.ingestion` package owns source processing, canonical evidence,
and page projection. For citation-aligned page content, Ingestion emits the
exact `projectkoios.ingestion.page.projection.result.PageProjectionResult` and
stops at that contract.

Search owns deterministic, versioned chunk derivation from the exact result.
This boundary supersedes the earlier prototype design in which Ingestion
coordinated chunking and emitted `TextChunk` objects. The
`CodeRepositoryIngester` material below describes that superseded prototype,
not current cross-repository ownership.

## Package Boundary

The package is responsible for:

* processing admitted sources into canonical evidence
* preserving source and evidence provenance
* deriving canonical citation-aligned page projections
* emitting the exact `PageProjectionResult` owner contract

The package is not responsible for:

* deriving or defining Search chunks
* indexing chunks
* searching chunks
* embedding chunks
* ranking chunks
* building RAG prompts
* calling an LLM
* exposing HTTP endpoints
* exposing MCP tools
* modifying source repositories

## Superseded prototype layout

```text
src/python/projectkoios/ingestion/
├── __init__.py
└── code_repository_ingester.py
```

## Superseded prototype object

| Object | Meaning | Status |
| --- | --- | --- |
| `CodeRepositoryIngester` | Coordinated `CodeRepositoryLoader` and `LineChunker` for code repositories. | superseded prototype |

## Responsibility Split

| Layer | Responsibility |
| --- | --- |
| Ingestion evidence and page projection | Produces the exact `PageProjectionResult`. |
| Search chunk derivation | Imports that exact leaf contract and derives deterministic, versioned Search chunks. |
| Applications | Owns cross-capability application composition without translating the leaf contract. |
| Workflow | Owns generic orchestration, state, retries, and replay. |

Ingestion does not own the loop that derives Search chunks. Chunk derivation
does not grant Ingestion or Search's derivation module indexing, retrieval,
publication, model-selection or model-execution, application-composition, or
workflow-orchestration authority.

## Superseded `CodeRepositoryIngester` prototype

The prototype `CodeRepositoryIngester` converted a `CodeRepository` into an
iterator of `TextChunk` objects. That behavior does not define the current
Ingestion-to-Search boundary.

It received its dependencies explicitly:

| Dependency             | Role                                                |
| ---------------------- | --------------------------------------------------- |
| `CodeRepositoryLoader` | Provides `CodeFile` objects.                        |
| `LineChunker`          | Converts each file’s text into `TextChunk` objects. |

Prototype constructor shape:

```python
class CodeRepositoryIngester:
    def __init__(
        self,
        loader: CodeRepositoryLoader,
        chunker: LineChunker,
    ) -> None: ...
```

Prototype ingestion method shape:

```python
def iter_chunks(
    self,
    repository: CodeRepository,
) -> Iterator[TextChunk]: ...
```

The method:

1. calls `loader.iter_files(repository)`
2. iterates over each `CodeFile`
3. calls `chunker.chunk_text(...)`
4. yields each `TextChunk`

## Superseded prototype provenance mapping

The prototype ingester mapped `CodeFile` fields into chunk provenance.

| `CodeFile` field | `TextChunk` field           |
| ---------------- | --------------------------- |
| `relative_path`  | `source_path`               |
| `language`       | `language`                  |
| file role        | `source_kind = "code_file"` |
| `text`           | input to chunker            |

The prototype used repository-relative paths, not absolute file paths, for
`TextChunk.source_path`. This mapping grants no current chunk ownership to
Ingestion.

## Dependency Direction

The current production dependency is narrow and one-way:

```text
projectkoios-search
  -> projectkoios.ingestion.page.projection.result.PageProjectionResult
```

`projectkoios-ingestion` must not import `projectkoios-search`. Search consumes
the exact leaf value directly; a duplicate DTO and an Applications-owned
translation or mapping layer are not part of the current architecture.
Applications retains composition ownership, and Workflow retains orchestration
ownership.

## Superseded prototype public API

The prototype public API was exported from:

```text
projectkoios.ingestion
```

Prototype public objects:

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

## Superseded prototype tests

Prototype tests belonged under:

```text
tests/projectkoios/ingestion/
```

Prototype test file:

```text
tests/projectkoios/ingestion/test__CodeRepositoryIngester.py
```

Prototype test behaviors:

| Test                                                    | Behavior                                            |
| ------------------------------------------------------- | --------------------------------------------------- |
| `test__iter_chunks__yields_chunks_from_code_repository` | Loads code files and yields text chunks.            |
| `test__iter_chunks__preserves_relative_source_path`     | Uses `CodeFile.relative_path` as chunk source path. |
| `test__iter_chunks__sets_source_kind_to_code_file`      | Sets `source_kind` to `code_file`.                  |
| `test__iter_chunks__preserves_language`                 | Preserves file language on each chunk.              |

Tests should use temporary directories and the real `CodeRepositoryLoader` and `LineChunker`.

## Package Invariant

The `projectkoios.ingestion` package is valid when it can produce canonical
source evidence and the exact `PageProjectionResult` without deriving Search
chunks or depending on Search.

It must not own Search chunk contracts or derivation, index or retrieve chunks,
publish content, select or invoke models, compose applications, orchestrate
workflows, call an LLM, expose API or MCP endpoints, or modify source material.
