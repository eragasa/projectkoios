from pathlib import Path

from projectkoios.repositories.layout import (
    BASE_REPOSITORY_LAYOUT,
    DATA_SUPPORT_LAYOUT,
    OBSIDIAN_SUPPORT_LAYOUT,
    PYTHON_OBSIDIAN_INGESTION_REPOSITORY_LAYOUT,
    PYTHON_OBSIDIAN_REPOSITORY_LAYOUT,
    PYTHON_REPOSITORY_LAYOUT,
    PYTHON_SUPPORT_LAYOUT,
    GitRepository,
    RepositoryLayout,
    RepositoryLayoutFactory,
    RepositoryLayoutOptions,
)


def test__merge__deduplicates_entries() -> None:
    a = RepositoryLayout(
        required_files=("README.md", "LICENSE"),
        required_dirs=("docs",),
    )
    b = RepositoryLayout(
        required_files=("LICENSE", "CHANGELOG.md"),
        required_dirs=("docs", "tests"),
    )

    merged = a.merge(b)

    assert merged.required_files == ("README.md", "LICENSE", "CHANGELOG.md")
    assert merged.required_dirs == ("docs", "tests")


def test__required_file_paths__returns_paths_under_root() -> None:
    repo = GitRepository(root=Path("/repos/my-project"))
    layout = RepositoryLayout(
        required_files=("README.md", "pyproject.toml"),
        required_dirs=(),
    )

    paths = layout.required_file_paths(repo)

    assert paths == (
        Path("/repos/my-project/README.md"),
        Path("/repos/my-project/pyproject.toml"),
    )


def test__required_dir_paths__returns_paths_under_root() -> None:
    repo = GitRepository(root=Path("/repos/my-project"))
    layout = RepositoryLayout(
        required_files=(),
        required_dirs=("src", "tests"),
    )

    paths = layout.required_dir_paths(repo)

    assert paths == (
        Path("/repos/my-project/src"),
        Path("/repos/my-project/tests"),
    )


def test__required_paths__combines_files_and_dirs() -> None:
    repo = GitRepository(root=Path("/repos/my-project"))
    layout = RepositoryLayout(
        required_files=("README.md",),
        required_dirs=("src",),
    )

    paths = layout.required_paths(repo)

    assert paths == (
        Path("/repos/my-project/README.md"),
        Path("/repos/my-project/src"),
    )


def test__base_layout__has_standard_files_and_dirs() -> None:
    assert "README.md" in BASE_REPOSITORY_LAYOUT.required_files
    assert "LICENSE" in BASE_REPOSITORY_LAYOUT.required_files
    assert "docs" in BASE_REPOSITORY_LAYOUT.required_dirs
    assert "src" in BASE_REPOSITORY_LAYOUT.required_dirs
    assert "tests" in BASE_REPOSITORY_LAYOUT.required_dirs


def test__python_support__adds_pyproject_toml_and_dirs() -> None:
    assert "pyproject.toml" in PYTHON_SUPPORT_LAYOUT.required_files
    assert "src/python" in PYTHON_SUPPORT_LAYOUT.required_dirs
    assert "tests/python" in PYTHON_SUPPORT_LAYOUT.required_dirs


def test__obsidian_support__adds_home_note_and_dirs() -> None:
    assert "00_HOME.md" in OBSIDIAN_SUPPORT_LAYOUT.required_files
    assert "notes" in OBSIDIAN_SUPPORT_LAYOUT.required_dirs
    assert "references" in OBSIDIAN_SUPPORT_LAYOUT.required_dirs


def test__python_repository_layout__includes_base_and_python() -> None:
    assert "pyproject.toml" in PYTHON_REPOSITORY_LAYOUT.required_files
    assert "README.md" in PYTHON_REPOSITORY_LAYOUT.required_files
    assert "src/python" in PYTHON_REPOSITORY_LAYOUT.required_dirs
    assert "docs" in PYTHON_REPOSITORY_LAYOUT.required_dirs


def test__python_obsidian_layout__combines_both() -> None:
    assert "pyproject.toml" in PYTHON_OBSIDIAN_REPOSITORY_LAYOUT.required_files
    assert "00_HOME.md" in PYTHON_OBSIDIAN_REPOSITORY_LAYOUT.required_files
    assert "src/python" in PYTHON_OBSIDIAN_REPOSITORY_LAYOUT.required_dirs
    assert "notes" in PYTHON_OBSIDIAN_REPOSITORY_LAYOUT.required_dirs


def test__python_obsidian_ingestion_layout__includes_all() -> None:
    ingest = PYTHON_OBSIDIAN_INGESTION_REPOSITORY_LAYOUT
    assert "_ingest" in ingest.required_dirs
    assert "_generated" in ingest.required_dirs


def test__factory__base_only() -> None:
    factory = RepositoryLayoutFactory()
    layout = factory.create(RepositoryLayoutOptions())
    assert layout == BASE_REPOSITORY_LAYOUT


def test__factory__python_only() -> None:
    factory = RepositoryLayoutFactory()
    layout = factory.create(RepositoryLayoutOptions(python=True))
    assert "pyproject.toml" in layout.required_files
    assert "00_HOME.md" not in layout.required_files


def test__factory__python_and_obsidian() -> None:
    factory = RepositoryLayoutFactory()
    layout = factory.create(
        RepositoryLayoutOptions(python=True, obsidian=True),
    )
    assert "pyproject.toml" in layout.required_files
    assert "00_HOME.md" in layout.required_files
    assert "src/python" in layout.required_dirs
    assert "notes" in layout.required_dirs


def test__factory__data_support() -> None:
    factory = RepositoryLayoutFactory()
    layout = factory.create(RepositoryLayoutOptions(data=True))
    assert "data/README.md" in layout.required_files
    assert "data/raw" in layout.required_dirs
    assert "data/processed" in layout.required_dirs
    assert "data/private" in layout.required_dirs


def test__data_support_layout__has_readme_and_data_dirs() -> None:
    assert "data/README.md" in DATA_SUPPORT_LAYOUT.required_files
    assert "data" in DATA_SUPPORT_LAYOUT.required_dirs
    assert "data/raw" in DATA_SUPPORT_LAYOUT.required_dirs
    assert "data/processed" in DATA_SUPPORT_LAYOUT.required_dirs
    assert "data/private" in DATA_SUPPORT_LAYOUT.required_dirs
