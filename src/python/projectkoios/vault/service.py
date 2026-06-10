# src/python/projectkoios/vault/service.py

from pathlib import Path

from projectkoios.api.config import VaultConfiguration


class VaultService:
    """
    Application service for vault-level operations.

    At this stage, VaultService only owns the vault configuration and exposes
    basic path-state checks. File scanning, Markdown parsing, and front matter
    extraction should be added later in separate vault modules.
    """

    def __init__(self, configuration: VaultConfiguration) -> None:
        self.configuration = configuration

    @property
    def path(self) -> Path | None:
        """
        Return the configured vault path.

        None means no vault has been configured yet.
        """

        return self.configuration.path

    def is_configured(self) -> bool:
        """
        Return True if a vault path has been configured.
        """

        return self.path is not None

    def exists(self) -> bool:
        """
        Return True if the configured vault path exists as a directory.
        """

        if self.path is None:
            return False

        return self.path.exists() and self.path.is_dir()