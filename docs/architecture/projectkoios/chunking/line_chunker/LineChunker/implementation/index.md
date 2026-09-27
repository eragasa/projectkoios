# `LineChunker` implementation

## Data flow

1. Split input with `splitlines(keepends=True)`.
2. Return immediately when the resulting line list is empty.
3. Set the positive step to chunk size minus overlap.
4. Slice from the current zero-based start to the smaller of start plus chunk
   size and the line count.
5. Yield a `TextChunk` with one-based inclusive bounds and joined slice text.
6. Stop when the emitted end equals the line count; otherwise advance by the
   step and increment the chunk index.

The final-window break prevents an unnecessary overlapping suffix window. The
strict constructor constraint on overlap makes the step at least one and proves
progress for finite input.

## Navigation

- [Mathematics](mathematics/index.md)
- [Testing](testing/index.md)
- [Class contract](../index.md)

## Source mapping

- `src/python/projectkoios/chunking/line_chunker.py::LineChunker.chunk_text`
