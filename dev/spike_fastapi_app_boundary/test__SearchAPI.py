# dev/spike_fastapi_app_boundary/test__SearchAPI.py

import pytest
from fastapi.testclient import TestClient

from .app import ProjectKoiosApp


@pytest.fixture
def client() -> TestClient:
    app = ProjectKoiosApp.create_app()
    return TestClient(app)


def test__search_endpoint__returns_json_results(client: TestClient) -> None:
    response = client.post(
        "/search",
        json={
            "query": "particle",
            "limit": 10,
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test__search_endpoint__rejects_empty_query(client: TestClient) -> None:
    response = client.post(
        "/search",
        json={
            "query": "",
            "limit": 10,
        },
    )

    assert response.status_code == 422