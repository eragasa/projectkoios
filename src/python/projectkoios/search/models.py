# src/python/projectkoios/search/models.py

from __future__ import annotations

from dataclasses import dataclass

from projectkoios.chunking import TextChunk


@dataclass(frozen=True)
class ChunkSearchResult:
    chunk: TextChunk
    score: float