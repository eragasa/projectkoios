# repository.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# =============================================================================
# Repository model
# =============================================================================
#
# This module models a Git-backed repository layout.
#
# Current scope:
#
#     - generic Git repository layout
#     - optional Python support
#     - optional Obsidian support
#     - optional ingestion/generation support
#     - optional data directory
#
# Do not add Julia, Rust, Mojo, or TypeScript yet.
#
# The design separates:
#
#     GitRepository              = data object
#     RepositoryLayout           = concrete layout policy
#     RepositoryLayoutOptions    = enabled features
#     RepositoryLayoutFactory    = layout composer
#     RepositoryValidationResult = validation result
#     GitRepositoryValidator     = read-only validation action
#     GitRepositoryScaffolder    = mutating scaffolding action
#
# The rule is:
#
#     data should be data
#     policies should be explicit
#     actions should be actions
#     results should be inspectable
# =============================================================================


# =============================================================================
# Data object: local Git repository
# =============================================================================

@dataclass(frozen=True)
class GitRepository:
    """
    A local Git repository.

    This object represents the repository location on the local filesystem.

    It does not encode a particular folder layout. A Git repository can support
    Python, Obsidian, ingestion, generated outputs, or none of those. Those
    expectations belong in RepositoryLayout.
    """

    root: Path

    @classmethod
    def from_path(cls, path: str | Path) -> "GitRepository":
        """
        Construct a GitRepository from a string or Path.

        The path is normalized by expanding `~` and resolving relative path
        components.

        The path does not need to exist yet. This allows the object to represent
        a repository that will be scaffolded later.
        """
        return cls(root=Path(path).expanduser().resolve())

    @property
    def name(self) -> str:
        """
        Repository directory name.
        """
        return self.root.name

    @property
    def git_path(self) -> Path:
        """
        Path to the local `.git` directory.

        This is a simple local Git check. It does not yet handle worktrees,
        submodules, or `.git` files that point elsewhere.
        """
        return self.root / ".git"


# =============================================================================
# Policy object: concrete repository layout
# =============================================================================

@dataclass(frozen=True)
class RepositoryLayout:
    """
    A concrete repository layout.

    This object defines required files and directories relative to a repository
    root.

    Example required files:

        README.md
        LICENSE
        pyproject.toml

    Example required directories:

        docs
        src/python
        tests/python
        notes
        knowledge
    """

    required_files: tuple[str, ...]
    required_dirs: tuple[str, ...]

    def merge(self, *others: "RepositoryLayout") -> "RepositoryLayout":
        """
        Merge this layout with additional layout fragments.

        Duplicate entries are removed while preserving first-seen order.

        This allows a layout to be built as:

            base
            + Python support
            + Obsidian support
        """
        files = list(self.required_files)
        dirs = list(self.required_dirs)

        for other in others:
            files.extend(other.required_files)
            dirs.extend(other.required_dirs)

        return RepositoryLayout(
            required_files=tuple(dict.fromkeys(files)),
            required_dirs=tuple(dict.fromkeys(dirs)),
        )

    def required_file_paths(self, repository: GitRepository) -> tuple[Path, ...]:
        """
        Convert required file names into concrete paths under repository.root.
        """
        return tuple(repository.root / name for name in self.required_files)

    def required_dir_paths(self, repository: GitRepository) -> tuple[Path, ...]:
        """
        Convert required directory names into concrete paths under repository.root.
        """
        return tuple(repository.root / name for name in self.required_dirs)

    def required_paths(self, repository: GitRepository) -> tuple[Path, ...]:
        """
        Return all required paths.
        """
        return self.required_file_paths(repository) + self.required_dir_paths(repository)


# =============================================================================
# Configuration object: enabled repository features
# =============================================================================

@dataclass(frozen=True)
class RepositoryLayoutOptions:
    """
    Options for composing a repository layout.

    Current supported features:

        python:
            Add Python source, test, and example directories plus pyproject.toml.

        obsidian:
            Add Obsidian-facing note folders and 00_HOME.md.

        ingestion_generation:
            Add _ingest/ and _generated/ folders.

        data:
            Add data/ folders.

    Do not add future languages here until the repository actually supports them.
    """

    python: bool = False
    obsidian: bool = False
    ingestion_generation: bool = False
    data: bool = False


# =============================================================================
# Factory/composer object: build concrete layout from options
# =============================================================================

@dataclass(frozen=True)
class RepositoryLayoutFactory:
    """
    Compose a concrete RepositoryLayout from RepositoryLayoutOptions.

    The base layout is always included. Optional fragments are merged only when
    their corresponding flags are enabled.
    """

    def create(self, options: RepositoryLayoutOptions) -> RepositoryLayout:
        """
        Create a concrete repository layout.
        """
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


# =============================================================================
# Result object: repository validation result
# =============================================================================

@dataclass(frozen=True)
class RepositoryValidationResult:
    """
    Result of validating a repository against a layout.

    This object records the result. It does not print, scaffold, or mutate.
    """

    repository: GitRepository
    layout: RepositoryLayout
    missing_files: tuple[Path, ...]
    missing_dirs: tuple[Path, ...]

    @property
    def is_valid(self) -> bool:
        """
        True if no required files or directories are missing.
        """
        return not self.missing_files and not self.missing_dirs

    @property
    def missing_paths(self) -> tuple[Path, ...]:
        """
        Flat tuple of all missing paths.
        """
        return self.missing_files + self.missing_dirs


# =============================================================================
# Service/action object: read-only validation
# =============================================================================

@dataclass(frozen=True)
class GitRepositoryValidator:
    """
    Validate a GitRepository against a RepositoryLayout.

    This class is read-only.

    It is intentionally instantiable even though currently stateless because it
    may later acquire configuration such as strictness, reporting, or additional
    checks.
    """

    def validate(
        self,
        repository: GitRepository,
        layout: RepositoryLayout,
    ) -> RepositoryValidationResult:
        """
        Validate required files and directories.

        Files are checked with Path.is_file().
        Directories are checked with Path.is_dir().
        """
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


# =============================================================================
# Service/action object: mutating scaffolding
# =============================================================================

@dataclass(frozen=True)
class GitRepositoryScaffolder:
    """
    Create a repository layout.

    This class mutates the filesystem.

    Current behavior:

        - creates the repository root,
        - creates required directories,
        - creates missing required files as empty files,
        - does not overwrite existing files,
        - does not initialize Git,
        - does not call GitHub.

    It is intentionally conservative during development.
    """

    def scaffold(
        self,
        repository: GitRepository,
        layout: RepositoryLayout,
    ) -> None:
        """
        Create the required files and directories for a layout.
        """
        repository.root.mkdir(parents=True, exist_ok=True)

        for directory in layout.required_dir_paths(repository):
            directory.mkdir(parents=True, exist_ok=True)

        for file_path in layout.required_file_paths(repository):
            if not file_path.exists():
                file_path.write_text("", encoding="utf-8")


# =============================================================================
# Layout fragments
# =============================================================================
#
# These are composable layout fragments.
#
# BASE_REPOSITORY_LAYOUT is the minimal standard.
#
# PYTHON_SUPPORT_LAYOUT, OBSIDIAN_SUPPORT_LAYOUT,
# INGESTION_GENERATION_SUPPORT_LAYOUT, and DATA_SUPPORT_LAYOUT are optional.
# =============================================================================


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
"""
Base technical repository layout.

This is intentionally language-neutral.
"""


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
"""
Python support fragment.

Adds:

    pyproject.toml
    src/python/
    tests/python/
    examples/python/
"""


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
"""
Obsidian support fragment.

Adds:

    00_HOME.md
    notes/
    references/
    knowledge/

The repository root can be opened as an Obsidian vault.
"""


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
"""
Ingestion/generation support fragment.

Adds:

    _ingest/
    _ingest/sources/
    _ingest/manifests/
    _ingest/extracted/
    _generated/

Policy:

    _generated/ is not canonical.

Reviewed material should be moved into notes/, references/, or knowledge/.
"""


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
"""
Data support fragment.

Adds:

    data/
    data/raw/
    data/processed/
    data/private/

Usually data/private/ should be gitignored.
"""


# =============================================================================
# Convenience presets
# =============================================================================
#
# These are small named presets for the current supported cases.
# =============================================================================


GENERIC_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT
"""
Base repository only.
"""


PYTHON_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
)
"""
Base repository + Python support.
"""


OBSIDIAN_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    OBSIDIAN_SUPPORT_LAYOUT,
)
"""
Base repository + Obsidian support.
"""


PYTHON_OBSIDIAN_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
    OBSIDIAN_SUPPORT_LAYOUT,
)
"""
Base repository + Python support + Obsidian support.
"""


PYTHON_OBSIDIAN_INGESTION_REPOSITORY_LAYOUT = BASE_REPOSITORY_LAYOUT.merge(
    PYTHON_SUPPORT_LAYOUT,
    OBSIDIAN_SUPPORT_LAYOUT,
    INGESTION_GENERATION_SUPPORT_LAYOUT,
)
"""
Base repository + Python support + Obsidian support + ingestion/generation.
"""


# =============================================================================
# Example usage
# =============================================================================

if __name__ == "__main__":
    repo = GitRepository.from_path("~/repos/example-repo")

    options = RepositoryLayoutOptions(
        python=True,
        obsidian=True,
        ingestion_generation=False,
        data=False,
    )

    layout = RepositoryLayoutFactory().create(options)

    validator = GitRepositoryValidator()
    result = validator.validate(repository=repo, layout=layout)

    if result.is_valid:
        print(f"{repo.name} satisfies the layout.")
    else:
        print(f"{repo.name} is missing required paths:")

        for path in result.missing_files:
            print(f"  missing file: {path}")

        for path in result.missing_dirs:
            print(f"  missing dir:  {path}")

    # To create the layout explicitly:
    #
    # scaffolder = GitRepositoryScaffolder()
    # scaffolder.scaffold(repository=repo, layout=layout)
