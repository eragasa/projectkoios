# dev/spike_fastapi_app_boundary/services.py

from .config import VaultConfiguration
from .models import SearchRequest, SearchResult


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
                object_type="note",
            )
        ]

        return results[: request.limit]


class VaultService:
    def __init__(self, configuration: VaultConfiguration) -> None:
        self.configuration = configuration