from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CodeRepository:
    root: Path
    name: str
    remote_url: str | None = None


@dataclass(frozen=True)
class CodeFile:
    repository_root: Path
    path: Path
    relative_path: Path
    text: str
    language: str

