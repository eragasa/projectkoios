# src/python/projectkoios/repositories/models.py

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Repository:
    root: Path
    name: str
    remote_url: str | None = None


@dataclass(frozen=True)
class RepositoryFile:
    repository_root: Path
    path: Path
    relative_path: Path
    text: str
    language: str