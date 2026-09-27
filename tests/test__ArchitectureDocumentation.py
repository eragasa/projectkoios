from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validate_architecture_docs import validate_repository


@pytest.fixture
def repository_root(pytestconfig: pytest.Config) -> Path:
    return pytestconfig.rootpath


def _fixture(tmp_path: Path, repository_root: Path) -> Path:
    shutil.copytree(
        repository_root / "docs/architecture",
        tmp_path / "docs/architecture",
    )
    shutil.copy2(repository_root / "pyproject.toml", tmp_path)
    return tmp_path


def _has(issues: list[str], text: str) -> None:
    assert text in "\n".join(issues)


def test__architecture_topology__repository_and_cwd_cli_are_valid(
    repository_root: Path,
) -> None:
    assert validate_repository(repository_root) == []
    result = subprocess.run(
        [
            sys.executable,
            str(repository_root / "tools/validate_architecture_docs.py"),
        ],
        cwd=repository_root,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "architecture documentation topology is valid\n"


def test__architecture_topology__requires_markers(tmp_path: Path) -> None:
    issues = validate_repository(tmp_path)
    _has(issues, "missing repository marker 'pyproject.toml'")
    _has(issues, "missing repository marker 'docs/architecture/README.md'")


def test__architecture_topology__rejects_tree_symlink(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    examples = root / "docs/architecture/examples"
    moved = root / "examples-real"
    examples.rename(moved)
    try:
        examples.symlink_to(moved, target_is_directory=True)
    except OSError as error:
        pytest.skip(f"symlinks unavailable: {error}")
    _has(validate_repository(root), "examples: symlinks are not allowed")


@pytest.mark.parametrize(
    "leaf",
    ["implementation.md", "mathematics.md", "references.md", "testing.md"],
)
def test__architecture_topology__rejects_named_leaf(
    tmp_path: Path,
    repository_root: Path,
    leaf: str,
) -> None:
    root = _fixture(tmp_path, repository_root)
    page = root / "docs/architecture/example_package/ExampleClass" / leaf
    page.parent.mkdir(parents=True)
    page.write_text("# Old layout\n", encoding="utf-8")
    _has(validate_repository(root), "Markdown leaves must be named index.md")


def test__architecture_topology__requires_exact_examples(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    example = root / "docs/architecture/examples/example_package/index.md"
    example.unlink()
    extra = root / "docs/architecture/examples/extra/index.md"
    extra.parent.mkdir()
    extra.write_text("# Extra\n", encoding="utf-8")
    issues = validate_repository(root)
    _has(issues, "missing example entry")
    _has(issues, "unexpected example entry")


def test__architecture_topology__requires_example_index_regular_file(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    example = root / "docs/architecture/examples/example_package/index.md"
    example.unlink()
    example.mkdir()
    _has(
        validate_repository(root),
        "canonical example index must be a regular file",
    )


def test__architecture_topology__allows_reserved_names_in_ordinary_paths(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    for relative in (
        "references/index.md",
        "projectkoios/references/index.md",
        "projectkoios/testing/mathematics/index.md",
    ):
        page = root / "docs/architecture" / relative
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text("# Ordinary architecture page\n", encoding="utf-8")
    assert validate_repository(root) == []


def test__architecture_topology__rejects_templates(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    (root / "docs/architecture/_templates").mkdir()
    _has(validate_repository(root), "_templates: obsolete directory")


def test__architecture_topology__allows_bounded_system_index(
    tmp_path: Path,
    repository_root: Path,
) -> None:
    root = _fixture(tmp_path, repository_root)
    system = root / "docs/architecture/_system/dependency-rules/index.md"
    system.parent.mkdir(parents=True)
    system.write_text("# Dependency rules\n", encoding="utf-8")
    assert validate_repository(root) == []

    nested = system.parent / "nested/index.md"
    nested.parent.mkdir()
    nested.write_text("# Invalid nested system page\n", encoding="utf-8")
    _has(validate_repository(root), "unsupported architecture placement")
