from pathlib import Path

from projectkoios.repositories.layout import GitRepository


def test__from_path__expands_user_home() -> None:
    repo = GitRepository.from_path("~/some-repo")
    assert str(repo.root).startswith("/")
    assert repo.root.name == "some-repo"


def test__from_path__resolves_relative_path() -> None:
    repo = GitRepository.from_path("relative/path")
    assert repo.root.is_absolute()


def test__name__returns_directory_name() -> None:
    repo = GitRepository(root=Path("/repos/my-project"))
    assert repo.name == "my-project"


def test__git_path__returns_dot_git_under_root() -> None:
    repo = GitRepository(root=Path("/repos/my-project"))
    assert repo.git_path == Path("/repos/my-project/.git")
