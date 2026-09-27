# Class `projectkoios.chunking.line_chunker.LineChunker`

## Constructor contract

`LineChunker(lines_per_chunk=80, overlap_lines=10)` stores validated integer
window parameters. The required domain is `lines_per_chunk > 0` and
`0 <= overlap_lines < lines_per_chunk`.

## Output contract

`chunk_text` returns an iterator. Each yielded `TextChunk` contains the supplied
metadata, a zero-based `chunk_index`, a one-based inclusive line interval, and
the exact concatenation of source lines in that interval. Empty text yields an
empty iterator.

The positive step `lines_per_chunk - overlap_lines` advances every nonterminal
window. The loop stops after yielding the first window whose end reaches the
input line count, so finite input terminates.

## Navigation

- [Implementation](implementation/index.md)
- [Parent module](../index.md)

## Source mapping

- `src/python/projectkoios/chunking/line_chunker.py::LineChunker.__init__`
- `src/python/projectkoios/chunking/line_chunker.py::LineChunker.chunk_text`
