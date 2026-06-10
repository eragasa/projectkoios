from fastapi import APIRouter

from projectkoios.api.models import SearchRequest, SearchResult
from projectkoios.search.service import SearchService


def create_search_router(
    search_service: SearchService
) -> APIRouter:
    router = APIRouter(prefix="/search", tags=["search"])

    @router.post("")
    def search(request: SearchRequest) -> list[SearchResult]:
        return search_service.search(request)

    return router