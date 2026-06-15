from pathlib import Path

from projectkoios.repositories.code import CodeRepository, CodeRepositoryLoader


def test__load__discovers_python_files(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    repo_root.mkdir()

    source_file = repo_root / "main.py"
    source_file.write_text("print('hello')\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert len(files) == 1
    assert files[0].relative_path == Path("main.py")
    assert files[0].language == "python"
    assert files[0].text == "print('hello')\n"


def test__load__discovers_pyproject_toml(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    repo_root.mkdir()

    pyproject = repo_root / "pyproject.toml"
    pyproject.write_text("[project]\nname = 'example'\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert len(files) == 1
    assert files[0].relative_path == Path("pyproject.toml")
    assert files[0].language == "toml"


def test__load__discovers_markdown_files(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    repo_root.mkdir()

    readme = repo_root / "README.md"
    readme.write_text("# Example\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert len(files) == 1
    assert files[0].relative_path == Path("README.md")
    assert files[0].language == "markdown"


def test__load__ignores_venv(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    venv = repo_root / ".venv"
    venv.mkdir(parents=True)

    ignored_file = venv / "ignored.py"
    ignored_file.write_text("print('ignore')\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert files == []


def test__load__ignores_git_directory(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    git_dir = repo_root / ".git"
    git_dir.mkdir(parents=True)

    ignored_file = git_dir / "config"
    ignored_file.write_text("[core]\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert files == []


def test__load__returns_relative_paths(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    source_dir = repo_root / "src" / "projectkoios"
    source_dir.mkdir(parents=True)

    source_file = source_dir / "app.py"
    source_file.write_text("app = None\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert len(files) == 1
    assert files[0].relative_path == Path("src/projectkoios/app.py")


def test__load__skips_unsupported_suffixes(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    repo_root.mkdir()

    unsupported_file = repo_root / "image.png"
    unsupported_file.write_bytes(b"not really an image")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = loader.load(repository)

    assert files == []

def test__iter_files__yields_code_files(tmp_path: Path) -> None:
    repo_root = tmp_path / "example"
    repo_root.mkdir()

    source_file = repo_root / "main.py"
    source_file.write_text("print('hello')\n", encoding="utf-8")

    repository = CodeRepository(root=repo_root, name="example")
    loader = CodeRepositoryLoader()

    files = list(loader.iter_files(repository))

    assert len(files) == 1
    assert files[0].relative_path == Path("main.py")