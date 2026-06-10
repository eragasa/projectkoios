# dev/spike_fastapi_app_boundary/test__SearchService.py

from .models import SearchRequest
from .services import SearchService


def test__search__returns_results() -> None:
    service = SearchService()

    results = service.search(
        SearchRequest(
            query="particle",
            limit=10,
        )
    )

    assert len(results) == 1

    result = results[0]

    assert result.title == "Particle in a Box"
    assert result.path == "knowledge/quantum/particle_in_a_box.md"
    assert result.score == 1.0
    assert result.object_type == "note"


def test__search__respects_limit() -> None:
    service = SearchService()

    results = service.search(
        SearchRequest(
            query="particle",
            limit=1,
        )
    )

    assert len(results) == 1

def test__search__returns_empty_list_when_query_does_not_match() -> None:
    """
    search() should return no results when the query does not match
    the indexed in-memory document.
    """

    service = SearchService()

    results = service.search(
        SearchRequest(
            query="nonexistent",
            limit=10,
        )
    )

    assert results == []