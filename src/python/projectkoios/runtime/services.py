# src/python/projectkoios/runtime/services.py

from __future__ import annotations

from dataclasses import dataclass

from projectkoios.api.config import ProjectKoiosAppConfiguration
from projectkoios.indexing import InMemoryChunkIndex
from projectkoios.search.service import SearchService
from projectkoios.vault.service import VaultService


# Runtime composition layer.
#
# This module wires together concrete services for the current prototype
# application. It exists to keep interface adapters, such as FastAPI routes,
# from constructing domain services directly.
#
# Long-term plan:
# - this module is not intended to become `projectkoios-core`
# - runtime wiring should move with the executable application that owns it
# - API-specific wiring should eventually live with `projectkoios-api`
# - agent-specific wiring should eventually live with `projectkoios-agent`
# - shared stable domain objects may later move to `projectkoios-core`
#
# In short:
#   core defines shared concepts
#   runtime assembles concrete implementations


@dataclass(frozen=True)
class ProjectKoiosServices:
    """
    Runtime service bundle for the current Project Koios application.

    This object groups concrete services that are shared by interface adapters
    such as FastAPI routes, CLI commands, notebooks, or future local apps.

    It is intentionally a runtime composition object, not a domain model.
    """

    search: SearchService
    vault: VaultService


def create_services(
    configuration: ProjectKoiosAppConfiguration,
) -> ProjectKoiosServices:
    """
    Build the default Project Koios service bundle.

    This function wires concrete implementations together. The API layer should
    not need to know which search index, vault service, or storage backend is
    used by default.
    """

    search_index = InMemoryChunkIndex()

    search_service = SearchService(
        search_index=search_index,
    )

    vault_service = VaultService(
        configuration=configuration.vault,
    )

    return ProjectKoiosServices(
        search=search_service,
        vault=vault_service,
    )