# Module `projectkoios.chunking.line_chunker`

## Current responsibility

The module defines `LineChunker`, which lazily yields `TextChunk` values from
text split with `str.splitlines(keepends=True)`.

## Contract summary

- Construction requires `lines_per_chunk > 0`, `overlap_lines >= 0`, and
  `overlap_lines < lines_per_chunk`; each violation raises `ValueError`.
- Empty input yields no chunks.
- Nonempty output preserves source path, source kind, language, and original
  line endings in each selected window.
- Chunk indexes are zero-based; `start_line` and `end_line` are one-based,
  inclusive source-line numbers.
- Consecutive windows overlap by the configured number of lines.

## Navigation

- [Class `LineChunker`](LineChunker/index.md)
- [Parent subpackage](../index.md)

## Source and test mapping

- Source: `src/python/projectkoios/chunking/line_chunker.py::LineChunker`
- Tests: `tests/projectkoios/chunking/test_LineChunker.py`
