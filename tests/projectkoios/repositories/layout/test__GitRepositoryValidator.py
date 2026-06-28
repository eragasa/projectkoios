from pathlib import Path

from projectkoios.repositories.layout import (
    GitRepository,
    GitRepositoryValidator,
    RepositoryLayout,
)


def test__validate__reports_missing_files(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path)
    layout = RepositoryLayout(
        required_files=("README.md",),
        required_dirs=(),
    )

    result = GitRepositoryValidator().validate(repo, layout)

    assert not result.is_valid
    assert result.missing_files == (tmp_path / "README.md",)


def test__validate__reports_missing_dirs(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path)
    layout = RepositoryLayout(
        required_files=(),
        required_dirs=("docs",),
    )

    result = GitRepositoryValidator().validate(repo, layout)

    assert not result.is_valid
    assert result.missing_dirs == (tmp_path / "docs",)


def test__validate__valid_when_all_paths_exist(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("# Test\n")
    docs = tmp_path / "docs"
    docs.mkdir()

    repo = GitRepository(root=tmp_path)
    layout = RepositoryLayout(
        required_files=("README.md",),
        required_dirs=("docs",),
    )

    result = GitRepositoryValidator().validate(repo, layout)

    assert result.is_valid
    assert result.missing_files == ()
    assert result.missing_dirs == ()


def test__validate__reports_all_missing_paths(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path)
    layout = RepositoryLayout(
        required_files=("README.md", "LICENSE"),
        required_dirs=("docs", "tests"),
    )

    result = GitRepositoryValidator().validate(repo, layout)

    assert not result.is_valid
    assert len(result.missing_paths) == 4
