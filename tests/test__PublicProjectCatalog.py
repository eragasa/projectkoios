from __future__ import annotations

import json
from pathlib import Path
from typing import cast
from urllib.parse import urlsplit

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPOSITORY_ROOT / "public/project-catalog.json"


def _reject_duplicate_fields(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def _catalog() -> dict[str, object]:
    return cast(
        dict[str, object],
        json.loads(
            CATALOG_PATH.read_bytes(),
            object_pairs_hook=_reject_duplicate_fields,
        ),
    )


def test__public_project_catalog__has_bounded_root_and_unique_identity() -> (
    None
):
    catalog = _catalog()

    assert set(catalog) == {"schema_version", "projects"}
    assert catalog["schema_version"] == "1"
    projects = cast(list[dict[str, object]], catalog["projects"])
    identifiers = [cast(str, project["id"]) for project in projects]
    slugs = [cast(str, project["slug"]) for project in projects]
    assert identifiers == ["projectkoios"]
    assert len(identifiers) == len(set(identifiers))
    assert len(slugs) == len(set(slugs))


def test__projectkoios_public_record__separates_capabilities_and_limits() -> (
    None
):
    project = cast(list[dict[str, object]], _catalog()["projects"])[0]

    assert set(project) == {
        "id",
        "slug",
        "name",
        "tagline",
        "summary",
        "status",
        "topics",
        "purposes",
        "principles",
        "capabilities",
        "limitations",
        "links",
    }
    assert project["status"] == "active-development"
    capabilities = cast(list[dict[str, object]], project["capabilities"])
    assert {capability["status"] for capability in capabilities} == {
        "available",
        "in-development",
    }
    limitations = cast(list[str], project["limitations"])
    assert any("scientific validation" in item for item in limitations)
    assert any("remote-user authentication" in item for item in limitations)


def test__public_catalog__contains_only_safe_links_and_text() -> None:
    document = _catalog()
    serialized = json.dumps(document, ensure_ascii=False)

    assert "/Users/" not in serialized
    assert "~/" not in serialized
    assert not any(ord(character) < 32 for character in serialized)

    projects = cast(list[dict[str, object]], document["projects"])
    for project in projects:
        links = cast(list[dict[str, str]], project["links"])
        for link in links:
            parsed = urlsplit(link["url"])
            assert parsed.scheme == "https"
            assert parsed.hostname == "github.com"
            assert parsed.username is None
            assert parsed.password is None
            assert parsed.port is None
            assert parsed.query == ""
            assert parsed.fragment == ""
