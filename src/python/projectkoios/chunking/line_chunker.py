#src/python/projectkoios/chunking/line_chunker.py

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from projectkoios.chunking.models import TextChunk


class LineChunker:
    def __init__(
        self,
        lines_per_chunk: int = 80,
        overlap_lines: int = 10,
    ) -> None:
        if lines_per_chunk <= 0:
            raise ValueError("lines_per_chunk must be positive")

        if overlap_lines < 0:
            raise ValueError("overlap_lines must be non-negative")

        if overlap_lines >= lines_per_chunk:
            raise ValueError("overlap_lines must be less than lines_per_chunk")

        self.lines_per_chunk = lines_per_chunk
        self.overlap_lines = overlap_lines

    def chunk_text(
        self,
        *,
        text: str,
        source_path: Path,
        source_kind: str,
        language: str,
    ) -> Iterator[TextChunk]:
        lines = text.splitlines(keepends=True)

        if not lines:
            return

        step = self.lines_per_chunk - self.overlap_lines
        start_index = 0
        chunk_index = 0

        while start_index < len(lines):
            end_index = min(start_index + self.lines_per_chunk, len(lines))

            yield TextChunk(
                source_path=source_path,
                source_kind=source_kind,
                language=language,
                chunk_index=chunk_index,
                start_line=start_index + 1,
                end_line=end_index,
                text="".join(lines[start_index:end_index]),
            )

            if end_index == len(lines):
                break

            start_index += step
            chunk_index += 1