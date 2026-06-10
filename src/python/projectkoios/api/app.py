# src/python/projectkoios/api/app.py

from fastapi import FastAPI

from projectkoios.api.config import ProjectKoiosAppConfiguration
from projectkoios.api.routers.core import create_core_router
from projectkoios.api.routers.search import create_search_router
from projectkoios.search.service import SearchService
from projectkoios.vault.service import VaultService


class ProjectKoiosApp:
    def __init__(
        self,
        configuration: ProjectKoiosAppConfiguration | None = None,
        search_service: SearchService | None = None,
        vault_service: VaultService | None = None,
    ) -> None:
        self.configuration = configuration or ProjectKoiosAppConfiguration()

        self.search_service = search_service or SearchService()
        self.vault_service = vault_service or VaultService(
            configuration=self.configuration.vault,
        )

        self.app = FastAPI(
            title=self.configuration.title,
            version=self.configuration.version,
            debug=self.configuration.debug,
        )

        self.register_routes()

    def register_routes(self) -> None:
        routers = [
            create_core_router(),
            create_search_router(self.search_service),
        ]

        for router in routers:
            self.app.include_router(router)
    
    @classmethod
    def create_app(
        cls,
        configuration: ProjectKoiosAppConfiguration | None = None,
    ) -> FastAPI:
        projectkoios_app = cls(configuration=configuration)
        return projectkoios_app.app

