from dataclasses import dataclass

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    limit: int = Field(default=10, ge=1, le=50)


class SearchResult(BaseModel):
    title: str
    path: str
    snippet: str
    score: float


class SearchService:
    def search(self, request: SearchRequest) -> list[SearchResult]:
        results = [
            SearchResult(
                title="Particle in a Box",
                path="knowledge/quantum/particle_in_a_box.md",
                snippet=(
                    "The particle in a box is the canonical Dirichlet "
                    "boundary condition problem."
                ),
                score=1.0,
            )
        ]

        return results[: request.limit]


class VaultService:
    pass


@dataclass(frozen=True)
class ProjectKoiosAppConfiguration:
    title: str = "Project Koios"
    version: str = "0.0.0"


def create_core_router() -> APIRouter:
    router = APIRouter(tags=["core"])

    @router.get("/")
    def read_root() -> dict[str, str]:
        return {
            "message": "Hello, Project Koios",
        }

    @router.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
        }

    return router


def create_search_router(search_service: SearchService) -> APIRouter:
    router = APIRouter(prefix="/search", tags=["search"])

    @router.post("")
    def search(request: SearchRequest) -> list[SearchResult]:
        return search_service.search(request)

    return router


class ProjectKoiosApp:
    def __init__(
        self,
        configuration: ProjectKoiosAppConfiguration | None = None,
        search_service: SearchService | None = None,
        vault_service: VaultService | None = None,
    ) -> None:
        self.configuration = configuration or ProjectKoiosAppConfiguration()
        self.search_service = search_service or SearchService()
        self.vault_service = vault_service or VaultService()

        self.app = FastAPI(
            title=self.configuration.title,
            version=self.configuration.version,
        )

        self.register_routes()

    def register_routes(self) -> None:
        routers = [
            create_core_router(),
            create_search_router(self.search_service),
        ]

        for router in routers:
            self.app.include_router(router)


projectkoios_app = ProjectKoiosApp()
app = projectkoios_app.app