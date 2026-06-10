# dev/spike_fastapi_app_boundary/search.py
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