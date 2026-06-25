# src/python/projectkoios/indexing/protocols.py

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from projectkoios.chunking import TextChunk


class ChunkIndexWriter(Protocol):
    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        ...