from pathlib import Path

from projectkoios.repositories.layout import (
    GitRepository,
    GitRepositoryScaffolder,
    RepositoryLayout,
)


def test__scaffold__creates_required_dirs(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path / "new-repo")
    layout = RepositoryLayout(
        required_files=(),
        required_dirs=("docs", "src"),
    )

    GitRepositoryScaffolder().scaffold(repo, layout)

    assert (tmp_path / "new-repo" / "docs").is_dir()
    assert (tmp_path / "new-repo" / "src").is_dir()


def test__scaffold__creates_required_files(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path / "new-repo")
    layout = RepositoryLayout(
        required_files=("README.md",),
        required_dirs=(),
    )

    GitRepositoryScaffolder().scaffold(repo, layout)

    readme = tmp_path / "new-repo" / "README.md"
    assert readme.is_file()
    assert readme.read_text(encoding="utf-8") == ""


def test__scaffold__does_not_overwrite_existing_files(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path)
    readme = tmp_path / "README.md"
    readme.write_text("preserve me\n")

    layout = RepositoryLayout(
        required_files=("README.md",),
        required_dirs=(),
    )

    GitRepositoryScaffolder().scaffold(repo, layout)

    assert readme.read_text(encoding="utf-8") == "preserve me\n"


def test__scaffold__creates_repository_root(tmp_path: Path) -> None:
    repo = GitRepository(root=tmp_path / "deeply/nested/repo")
    layout = RepositoryLayout(
        required_files=(),
        required_dirs=("docs",),
    )

    GitRepositoryScaffolder().scaffold(repo, layout)

    assert (tmp_path / "deeply/nested/repo").is_dir()
    assert (tmp_path / "deeply/nested/repo" / "docs").is_dir()
