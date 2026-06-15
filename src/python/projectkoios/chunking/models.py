#src/python/projectkoios/chunking/models.py

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextChunk:
    source_path: Path
    source_kind: str
    language: str
    chunk_index: int
    start_line: int
    end_line: int
    text: str