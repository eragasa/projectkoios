SUPPORTED_SUFFIXES: dict[str, str] = {
    ".py": "python",
    ".toml": "toml",
    ".md": "markdown",
}

IGNORED_PARTS: set[str] = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
}