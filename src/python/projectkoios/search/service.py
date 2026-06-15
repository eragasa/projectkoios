# src/python/projectkoios/search/service.py

from __future__ import annotations

from collections.abc import Iterable

from projectkoios.chunking import TextChunk
from projectkoios.search.memory_search_index import MemorySearchIndex
from projectkoios.search.models import ChunkSearchResult
from projectkoios.search.protocols import SearchIndex


class SearchService:
    def __init__(
        self,
        search_index: SearchIndex | None = None,
    ) -> None:
        self.search_index = search_index or MemorySearchIndex()

    def add_chunks(self, chunks: Iterable[TextChunk]) -> None:
        self.search_index.add_chunks(chunks)

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> list[ChunkSearchResult]:
        return self.search_index.search(
            query=query,
            limit=limit,
        )