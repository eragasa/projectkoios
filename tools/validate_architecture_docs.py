from __future__ import annotations

import argparse
import os
from pathlib import Path

ARCHITECTURE_ROOT = Path("docs/architecture")
EXAMPLE_FILES = {
    Path("examples/example_package/index.md"),
    Path("examples/example_package/example_module/index.md"),
    Path("examples/example_package/example_module/ExampleClass/index.md"),
    Path(
        "examples/example_package/example_module/ExampleClass/"
        "implementation/index.md"
    ),
    Path(
        "examples/example_package/example_module/ExampleClass/"
        "implementation/mathematics/index.md"
    ),
    Path(
        "examples/example_package/example_module/ExampleClass/"
        "implementation/references/index.md"
    ),
    Path(
        "examples/example_package/example_module/ExampleClass/"
        "implementation/testing/index.md"
    ),
}
DETAIL_NAMES = {"implementation", "mathematics", "references", "testing"}
DETAIL_CHILDREN = {"mathematics", "references", "testing"}


def _expected_example_entries() -> set[Path]:
    entries = set(EXAMPLE_FILES)
    for path in EXAMPLE_FILES:
        parent = path.parent
        while parent != Path("examples"):
            entries.add(parent)
            parent = parent.parent
    return entries


def _display(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _safe_tree(root: Path, architecture: Path, issues: list[str]) -> bool:
    for path in (architecture.parent, architecture):
        if path.is_symlink():
            issues.append(f"{_display(root, path)}: symlinks are not allowed")
            return False
    if not architecture.is_dir():
        issues.append("docs/architecture: missing architecture directory")
        return False
    safe = True
    for directory, directories, files in os.walk(
        architecture,
        followlinks=False,
    ):
        current = Path(directory)
        for name in [*directories, *files]:
            path = current / name
            if path.is_symlink():
                issues.append(
                    f"{_display(root, path)}: symlinks are not allowed"
                )
                safe = False
    return safe


def _valid_placement(relative: Path) -> bool:
    parts = relative.parts
    if relative == Path("README.md"):
        return True
    if not parts or parts[-1] != "index.md":
        return False
    directories = parts[:-1]
    if not directories:
        return False
    if directories[0] == "examples":
        return relative in EXAMPLE_FILES
    if directories[0] == "_system":
        return len(directories) == 2 and bool(directories[1])
    if any(part.startswith("_") for part in directories):
        return False
    details = [part for part in directories if part in DETAIL_NAMES]
    if not details:
        return True
    if directories[-1] == "implementation":
        return len(directories) >= 4 and details == ["implementation"]
    return (
        len(directories) >= 5
        and directories[-2] == "implementation"
        and directories[-1] in DETAIL_CHILDREN
        and details == ["implementation", directories[-1]]
    )


def validate_repository(repository_root: Path) -> list[str]:
    """Validate bounded architecture-documentation filesystem topology."""
    root = repository_root.resolve()
    architecture = root / ARCHITECTURE_ROOT
    issues: list[str] = []

    for marker in (Path("pyproject.toml"), ARCHITECTURE_ROOT / "README.md"):
        path = root / marker
        if path.is_symlink():
            issues.append(
                f"{marker.as_posix()}: repository marker must not be a symlink"
            )
        elif not path.is_file():
            issues.append(f".: missing repository marker '{marker.as_posix()}'")
    if issues or not _safe_tree(root, architecture, issues):
        return sorted(set(issues))

    obsolete = architecture / "_templates"
    if obsolete.exists():
        issues.append("docs/architecture/_templates: obsolete directory")

    expected_entries = _expected_example_entries()
    examples = architecture / "examples"
    actual_entries = (
        {
            path.relative_to(architecture)
            for path in examples.rglob("*")
            if not path.is_symlink()
        }
        if examples.is_dir()
        else set()
    )
    for missing in sorted(expected_entries - actual_entries):
        issues.append(
            f"docs/architecture/{missing.as_posix()}: missing example entry"
        )
    for extra in sorted(actual_entries - expected_entries):
        issues.append(
            f"docs/architecture/{extra.as_posix()}: unexpected example entry"
        )
    for relative in sorted(EXAMPLE_FILES):
        path = architecture / relative
        if path.exists() and not path.is_file():
            issues.append(
                f"docs/architecture/{relative.as_posix()}: canonical example "
                "index must be a regular file"
            )
    for relative in sorted(expected_entries - EXAMPLE_FILES):
        path = architecture / relative
        if path.exists() and not path.is_dir():
            issues.append(
                f"docs/architecture/{relative.as_posix()}: canonical example "
                "parent must be a directory"
            )

    for path in sorted(architecture.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in {
            ".md",
            ".markdown",
        }:
            continue
        relative = path.relative_to(architecture)
        if path.suffix != ".md":
            issues.append(
                f"{_display(root, path)}: use lowercase '.md' extension"
            )
        elif relative != Path("README.md") and path.name != "index.md":
            location = _display(root, path)
            issues.append(f"{location}: Markdown leaves must be named index.md")
        elif not _valid_placement(relative):
            issues.append(
                f"{_display(root, path)}: unsupported architecture placement"
            )
    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate architecture-documentation topology."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="repository root (defaults to the current working directory)",
    )
    issues = validate_repository(parser.parse_args().root)
    if issues:
        print(*issues, sep="\n")
        return 1
    print("architecture documentation topology is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
