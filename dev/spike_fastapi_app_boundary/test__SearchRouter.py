# dev/spike_fastapi_app_boundary/test__SearchRouter.py

"""
Tests for the search router factory.

These tests verify that create_search_router() exposes the minimal search
endpoint and that FastAPI/Pydantic validation is applied at the HTTP boundary.
"""

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from .routers.search import create_search_router
from .services import SearchService


@pytest.fixture
def client() -> TestClient:
    """
    Create a TestClient containing only the search router.

    This isolates SearchRouter behavior from ProjectKoiosApp composition.
    """

    app = FastAPI()
    app.include_router(create_search_router(SearchService()))

    return TestClient(app)


def test__search_endpoint__returns_results(client: TestClient) -> None:
    """
    POST /search should return a list of search results.
    """

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


def test__search_endpoint__rejects_empty_query(
    client: TestClient,
) -> None:
    """
    POST /search should reject an empty query string.
    """

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
    """
    POST /search should reject limit values above the request model maximum.
    """

    response = client.post(
        "/search",
        json={
            "query": "particle",
            "limit": 100,
        },
    )

    assert response.status_code == 422


def test__search_endpoint__respects_limit(client: TestClient) -> None:
    """
    POST /search should limit the number of returned results.
    """

    response = client.post(
        "/search",
        json={
            "query": "particle",
            "limit": 1,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1