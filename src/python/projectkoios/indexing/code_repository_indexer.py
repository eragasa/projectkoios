# src/python/projectkoios/indexing/code_repository_indexer.py

from __future__ import annotations

from projectkoios.indexing.protocols import ChunkIndexWriter
from projectkoios.ingestion import CodeRepositoryIngester
from projectkoios.repositories.code import CodeRepository


class CodeRepositoryIndexer:
    def __init__(
        self,
        ingester: CodeRepositoryIngester,
        index_writer: ChunkIndexWriter,
    ) -> None:
        self.ingester = ingester
        self.index_writer = index_writer

    def index_repository(
        self,
        repository: CodeRepository,
    ) -> None:
        chunks = self.ingester.iter_chunks(repository)
        self.index_writer.add_chunks(chunks)