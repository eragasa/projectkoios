from __future__ import annotations

from collections.abc import Iterator

from projectkoios.repositories.code.filters import (
    IGNORED_PARTS,
    SUPPORTED_SUFFIXES,
)
from projectkoios.repositories.code.models import CodeFile, CodeRepository


class CodeRepositoryLoader:
    def iter_files(self, repository: CodeRepository) -> Iterator[CodeFile]:
        root = repository.root.resolve()

        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue

            relative_path = path.relative_to(root)

            if any(part in IGNORED_PARTS for part in relative_path.parts):
                continue

            language = SUPPORTED_SUFFIXES.get(path.suffix)

            if language is None:
                continue

            yield CodeFile(
                repository_root=root,
                path=path,
                relative_path=relative_path,
                text=path.read_text(encoding="utf-8"),
                language=language,
            )

    def load(self, repository: CodeRepository) -> list[CodeFile]:
        return list(self.iter_files(repository))