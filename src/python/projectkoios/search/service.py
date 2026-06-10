# src/python/projectkoios/search/service.py

from projectkoios.api.models import SearchRequest, SearchResult


class SearchService:
    """
    Application service for search operations.

    At this stage, SearchService uses in-memory placeholder data. The purpose
    is to stabilize the API boundary before adding vault scanning, SQLite FTS,
    vector search, or ranking logic.
    """

    def search(self, request: SearchRequest) -> list[SearchResult]:
        """
        Return search results for the given request.

        This is currently a minimal in-memory implementation.
        """

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