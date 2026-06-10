# tests/api/routers/search/test__SearchRouter.py

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from projectkoios.api.routers.search import create_search_router
from projectkoios.search.service import SearchService


@pytest.fixture
def client() -> TestClient:
    """
    Create a TestClient containing only the search router.

    This isolates SearchRouter behavior from full ProjectKoiosApp
    composition.
    """

    app = FastAPI()
    app.include_router(create_search_router(SearchService()))

    return TestClient(app)


def test__search_endpoint__returns_results(client: TestClient) -> None:
    response = client.post(
        "/search",
        json={
            "query": "particle",
            "limit": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1

    result = data[0]

    assert result["title"] == "Particle in a Box"
    assert result["path"] == "knowledge/quantum/particle_in_a_box.md"
    assert result["snippet"] == (
        "The particle in a box is the canonical Dirichlet "
        "boundary condition problem."
    )
    assert result["score"] == 1.0
    assert result["object_type"] == "note"


def test__search_endpoint__rejects_empty_query(client: TestClient) -> None:
    response = client.post(
        "/search",
        json={
            "query": "",
            "limit": 10,
        },
    )

    assert response.status_code == 422


def test__search_endpoint__rejects_limit_above_maximum(
    client: TestClient,
) -> None:
    response = client.post(
        "/search",
        json={
            "query": "particle",
            "limit": 100,
        },
    )

    assert response.status_code == 422