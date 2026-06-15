# Chunking Package Architecture

## Purpose

The `projectkoios.chunking` package converts loaded text sources into smaller addressable text units.

A chunk is a bounded region of text with provenance. It records where the text came from, what source type it belongs to, what language or media type it has, and where the chunk begins and ends inside the source.

Chunking is not specific to RAG. RAG is one downstream consumer of chunks.

Chunks may also support search, citation, summarization, review, diagnostics, comparison, and prompt construction.

## Package Boundary

The package is responsible for:

* splitting text into bounded text chunks
* preserving source path information
* preserving source kind information
* preserving language or file-type information
* recording chunk order
* recording line ranges for line-based text sources

The package is not responsible for:

* loading files
* discovering repositories
* parsing repositories
* extracting text from PDFs
* indexing chunks
* searching chunks
* ranking chunks
* building RAG prompts
* calling an LLM
* storing chunks permanently

## Package Layout

```text
src/python/projectkoios/chunking/
├── __init__.py
├── models.py
└── line_chunker.py
```

## Core Objects

| Object        | Meaning                                                     | Status  |
| ------------- | ----------------------------------------------------------- | ------- |
| `TextChunk`   | A bounded text region with source provenance.               | current |
| `LineChunker` | A chunking strategy that splits text by fixed line windows. | current |

## `TextChunk`

`TextChunk` is the common output object for chunking.

```python
@dataclass(frozen=True)
class TextChunk:
    source_path: Path
    source_kind: str
    language: str
    chunk_index: int
    start_line: int
    end_line: int
    text: str
```

| Field         | Type   | Meaning                                                                                       |
| ------------- | ------ | --------------------------------------------------------------------------------------------- |
| `source_path` | `Path` | Path identifying the source object. For repository files, this should be repository-relative. |
| `source_kind` | `str`  | Kind of source object, such as `code_file`, `markdown_note`, or `pdf_text`.                   |
| `language`    | `str`  | Source language or file type, such as `python`, `markdown`, or `text`.                        |
| `chunk_index` | `int`  | Zero-based chunk order within the source object.                                              |
| `start_line`  | `int`  | One-based first line included in the chunk.                                                   |
| `end_line`    | `int`  | One-based last line included in the chunk.                                                    |
| `text`        | `str`  | Chunk text.                                                                                   |

Line ranges are inclusive.

Example:

| Field         | Value                                |
| ------------- | ------------------------------------ |
| `source_path` | `src/python/projectkoios/api/app.py` |
| `source_kind` | `code_file`                          |
| `language`    | `python`                             |
| `chunk_index` | `0`                                  |
| `start_line`  | `1`                                  |
| `end_line`    | `80`                                 |

## `LineChunker`

`LineChunker` splits text into fixed-size line windows.

It is the first chunking strategy because it is simple, deterministic, and works for code, Markdown, and extracted plain text.

The chunker accepts text and provenance fields. It does not know about repositories, filesystems, RAG, search, or LLMs.

## Loader and Chunker Separation

Repository loaders produce source objects.

Chunkers produce chunks.

Ingesters later coordinate loaders and chunkers.

| Layer              | Example object                 | Responsibility                                        |
| ------------------ | ------------------------------ | ----------------------------------------------------- |
| Repository loading | `CodeRepositoryLoader`         | Loads `CodeFile` objects.                             |
| Chunking           | `LineChunker`                  | Converts text into `TextChunk` objects.               |
| Ingestion          | `CodeRepositoryIngester` later | Calls loader, calls chunker, sends chunks downstream. |

The chunking package must not import `projectkoios.repositories.code`.

The repository package must not import `projectkoios.chunking`.

A later ingestion package may import both.

## Chunker Interface

The current chunker interface is:

```python
chunk_text(
    *,
    text: str,
    source_path: Path,
    source_kind: str,
    language: str,
) -> Iterator[TextChunk]
```

This keeps chunking independent of source type.

A code file can be chunked by passing:

```python
chunker.chunk_text(
    text=code_file.text,
    source_path=code_file.relative_path,
    source_kind="code_file",
    language=code_file.language,
)
```

A Markdown note can later use the same interface:

```python
chunker.chunk_text(
    text=note_file.text,
    source_path=note_file.relative_path,
    source_kind="markdown_note",
    language="markdown",
)
```

## Line Chunking Rules

`LineChunker` uses two parameters:

| Parameter         | Meaning                                           |
| ----------------- | ------------------------------------------------- |
| `lines_per_chunk` | Maximum number of lines in one chunk.             |
| `overlap_lines`   | Number of lines repeated between adjacent chunks. |

Rules:

* `lines_per_chunk` must be positive.
* `overlap_lines` must be non-negative.
* `overlap_lines` must be less than `lines_per_chunk`.
* Empty text produces no chunks.
* Chunk indices are zero-based.
* Line numbers are one-based.
* `start_line` and `end_line` are inclusive.
* Chunk text preserves original line endings.

Example with `lines_per_chunk = 3` and `overlap_lines = 1`:

| Chunk | Lines |
| ----- | ----- |
| `0`   | `1-3` |
| `1`   | `3-5` |
| `2`   | `5-7` |

## Current Implementation Scope

The first implementation only provides line-window chunking.

It does not provide:

* Markdown heading-aware chunking
* Python AST-aware chunking
* PDF page chunking
* semantic chunking
* token-count chunking
* chunk ranking
* chunk embedding
* chunk storage
* automatic chunker selection

Those can be added later as separate strategies.

Possible later chunkers:

| Chunker           | Strategy                                         |
| ----------------- | ------------------------------------------------ |
| `MarkdownChunker` | Split Markdown by headings and sections.         |
| `PythonChunker`   | Split Python by classes, functions, and imports. |
| `PdfPageChunker`  | Split extracted PDF text by page ranges.         |
| `TokenChunker`    | Split text by token budget.                      |

## Tests

Tests belong under:

```text
tests/projectkoios/chunking/
```

Current test file:

```text
tests/projectkoios/chunking/test__LineChunker.py
```

Initial test behaviors:

| Test                                                              | Behavior                                 |
| ----------------------------------------------------------------- | ---------------------------------------- |
| `test__chunk_text__returns_single_chunk_for_short_text`           | Short text produces one chunk.           |
| `test__chunk_text__splits_long_text_into_line_windows`            | Long text is split into multiple chunks. |
| `test__chunk_text__supports_overlap`                              | Adjacent chunks share overlap lines.     |
| `test__chunk_text__returns_no_chunks_for_empty_text`              | Empty text produces no chunks.           |
| `test__init__rejects_non_positive_lines_per_chunk`                | Invalid chunk size is rejected.          |
| `test__init__rejects_negative_overlap`                            | Negative overlap is rejected.            |
| `test__init__rejects_overlap_greater_than_or_equal_to_chunk_size` | Overlap must be smaller than chunk size. |

## Package Invariant

The `projectkoios.chunking` package is valid when it can convert supplied text into deterministic `TextChunk` objects with preserved source provenance and line ranges.

The package must not load source files, discover repositories, index chunks, search chunks, call an LLM, or depend on RAG-specific behavior.
