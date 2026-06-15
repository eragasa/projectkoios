# src/python/projectkoios/search/protocols.py

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from projectkoios.chunking import TextChunk
from projectkoios.search.models import ChunkSearchResult


class SearchIndex(Protocol):
    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        ...

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]:
        ...