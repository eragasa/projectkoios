# `LineChunker` testing

## Exact test mapping

All tests are in `tests/projectkoios/chunking/test_LineChunker.py`:

- `test__chunk_text__returns_single_chunk_for_short_text`
- `test__chunk_text__splits_long_text_into_line_windows`
- `test__chunk_text__supports_overlap`
- `test__chunk_text__returns_no_chunks_for_empty_text`
- `test__init__rejects_non_positive_lines_per_chunk`
- `test__init__rejects_negative_overlap`
- `test__init__rejects_overlap_greater_than_or_equal_to_chunk_size`

## Evidence

- **Implementation conformance — supported:** the mapped tests exercise
  constructor constraints, metadata and text output, one-based bounds, overlap,
  final partial windows, and empty input.
- **Numerical verification — supported for mapped fixtures:** integer line
  intervals and overlap are compared with Python `==` (tolerance zero) on
  CPython 3.12.13 with pytest 9.0.3 for the documented short-example domain;
  exhaustive parameters and the repository's Python 3.14 target are not
  verified by that local run.
- **Scientific validation — not applicable:** line-window partitioning makes no
  scientific or physical-model claim.
- **Human acceptance — not evaluated:** no accepting authority or operational
  approval is represented by these unit tests.

Termination follows from the validated positive step and finite line count; the
tests exercise representative terminating paths rather than a formal runtime
proof.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Mathematics](../mathematics/index.md)
