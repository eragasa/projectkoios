from fastapi import APIRouter

from ..models import SearchRequest, SearchResult
from ..services import SearchService


def create_search_router(
    search_service: SearchService
) -> APIRouter:
    router = APIRouter(prefix="/search", tags=["search"])

    @router.post("")
    def search(request: SearchRequest) -> list[SearchResult]:
        return search_service.search(request)

    return router