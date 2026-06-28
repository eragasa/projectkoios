# src/python/projectkoios/repositories/layout.py

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GitRepository:
    root: Path

    @classmethod
    def from_path(cls, path: str | Path) -> GitRepository:
        return cls(root=Path(path).expanduser().resolve())

    @property
    def name(self) -> str:
        return self.root.name

    @property
    def git_path(self) -> Path:
        return self.root / ".git"


@dataclass(frozen=True)
class RepositoryLayout:
    required_files: tuple[str, ...]
    required_dirs: tuple[str, ...]

    def merge(self, *others: RepositoryLayout) -> RepositoryLayout:
        files = list(self.required_files)
        dirs = list(self.required_dirs)

        for other in others:
            files.extend(other.required_files)
            dirs.extend(other.required_dirs)

        return RepositoryLayout(
            required_files=tuple(dict.fromkeys(files)),
            required_dirs=tuple(dict.fromkeys(dirs)),
        )

    def required_file_paths(
        self, repository: GitRepository
    ) -> tuple[Path, ...]:
        return tuple(repository.root / name for name in self.required_files)

    def required_dir_paths(self, repository: GitRepository) -> tuple[Path, ...]:
        return tuple(repository.root / name for name in self.required_dirs)

    def required_paths(
        self, repository: GitRepository
    ) -> tuple[Path, ...]:
        return (
            self.required_file_paths(repository)
            + self.required_dir_paths(repository)
        )


@dataclass(frozen=True)
class RepositoryLayoutOptions:
    python: bool = False
    obsidian: bool = False
    ingestion_generation: bool = False
    data: bool = False


@dataclass(frozen=True)
class RepositoryLayoutFactory:
    def create(self, options: RepositoryLayoutOptions) -> RepositoryLayout:
        layout = BASE_REPOSITORY_LAYOUT

        if options.python:
            layout = layout.merge(PYTHON_SUPPORT_LAYOUT)

        if options.obsidian:
            layout = layout.merge(OBSIDIAN_SUPPORT_LAYOUT)

        if options.ingestion_generation:
            layout = layout.merge(INGESTION_GENERATION_SUPPORT_LAYOUT)

        if options.data:
            layout = layout.merge(DATA_SUPPORT_LAYOUT)

        return layout


@dataclass(frozen=True)
class RepositoryValidationResult:
    repository: GitRepository
    layout: RepositoryLayout
    missing_files: tuple[Path, ...]
    missing_dirs: tuple[Path, ...]

    @property
    def is_valid(self) -> bool:
        return not self.missing_files and not self.missing_dirs

    @property
    def missing_paths(self) -> tuple[Path, ...]:
        return self.missing_files + self.missing_dirs


@dataclass(frozen=True)
class GitRepositoryValidator:
    def validate(
        self,
        repository: GitRepository,
        layout: RepositoryLayout,
    ) -> RepositoryValidationResult:
        missing_files = tuple(
            path
            for path in layout.required_file_paths(repository)
            if not path.is_file()
        )

        missing_dirs = tuple(
            path
            for path in layout.required_dir_paths(repository)
            if not path.is_dir()
        )

        return RepositoryValidationResult(
            repository=repository,
            layout=layout,
            missing_files=missing_files,
            missing_dirs=missing_dirs,
        )


@dataclass(frozen=True)
class GitRepositoryScaffolder:
    def scaffold(
        self,
        repository: GitRepository,
        layout: RepositoryLayout,
    ) -> None:
        repository.root.mkdir(parents=True, exist_ok=True)

        for directory in layout.required_dir_paths(repository):
            directory.mkdir(parents=True, exist_ok=True)

        for file_path in layout.required_file_paths(repository):
            if not file_path.exists():
                file_path.write_text("", encoding="utf-8")


BASE_REPOSITORY_LAYOUT = RepositoryLayout(
    required_files=(
        "README.md",
        "LICENSE",
        ".gitignore",
    ),
    required_dirs=(
        "docs",
        "src",
        "tests",
        "examples",
        "scripts",
    ),
)

PYTHON_SUPPORT_LAYOUT = RepositoryLayout(
    required_files=(
        "pyproject.toml",
    ),
    required_dirs=(
        "src/python",
        "tests/python",
        "examples/python",
    ),
)

OBSIDIAN_SUPPORT_LAYOUT = RepositoryLayout(
    required_files=(
        "00_HOME.md",
    ),
    required_dirs=(
        "notes",
        "references",
        "knowledge",
    ),
)

INGESTION_GENERATION_SUPPORT_LAYOUT = RepositoryLayout(
    required_files=(),
    required_dirs=(
        "_ingest",
        "_ingest/sources",
        "_ingest/manifests",
        "_ingest/extracted",
        "_generated",
    ),
)

DATA_SUPPORT_LAYOUT = RepositoryLayout(
    required_files=(
        "data/README.md",
    ),
    required_dirs=(
        "data",
        "data/raw",
        "data/processed",
        "data/private",
    ),
)

GENERIC_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT

PYTHON_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
)

OBSIDIAN_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    OBSIDIAN_SUPPORT_LAYOUT,
)

PYTHON_OBSIDIAN_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
    OBSIDIAN_SUPPORT_LAYOUT,
)

PYTHON_OBSIDIAN_INGESTION_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
    OBSIDIAN_SUPPORT_LAYOUT,
    INGESTION_GENERATION_SUPPORT_LAYOUT,
)
