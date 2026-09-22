from __future__ import annotations

import json
from pathlib import Path
from typing import cast
from urllib.parse import urlsplit

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPOSITORY_ROOT / "public/course-catalog.json"


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


def _courses() -> list[dict[str, object]]:
    institutions = cast(list[dict[str, object]], _catalog()["institutions"])
    return [
        course
        for institution in institutions
        for course in cast(list[dict[str, object]], institution["courses"])
    ]


def test__public_course_catalog__covers_all_identified_course_codes() -> None:
    catalog = _catalog()
    institutions = cast(list[dict[str, object]], catalog["institutions"])
    courses = _courses()

    assert set(catalog) == {
        "schema_version",
        "reviewed_on",
        "source",
        "publication_boundary",
        "institutions",
        "unresolved_collections",
    }
    assert catalog["schema_version"] == "1"
    assert catalog["reviewed_on"] == "2026-09-22"
    assert [institution["id"] for institution in institutions] == [
        "dlsu",
        "pacific",
        "uf",
    ]
    assert len(courses) == 40
    identifiers = [cast(str, course["id"]) for course in courses]
    assert len(identifiers) == len(set(identifiers))


def test__public_course_catalog__publishes_no_course_materials() -> None:
    courses = _courses()
    statuses = [course["materials_status"] for course in courses]

    assert statuses.count("review-candidate") == 3
    assert statuses.count("inventory-only") == 37
    assert "published" not in statuses
    titled_courses = {
        cast(str, course["code"]): course["title"]
        for course in courses
        if course["title"] is not None
    }
    assert titled_courses == {
        "ENGR219": "Numerical Methods for Engineering",
        "MATH057": "Applied Differential Equations I",
        "MATH157": "Applied Differential Equations II",
    }


def test__public_course_catalog__uses_stable_public_inventory_evidence() -> (
    None
):
    catalog = _catalog()
    source = cast(dict[str, object], catalog["source"])
    source_url = cast(str, source["url"])
    parsed = urlsplit(source_url)

    assert source["repository"] == "eragasa/projectkoios-courses"
    assert source["revision"] == "7bd6ce797d10381d436b89dbc12b226a95719d42"
    assert parsed.scheme == "https"
    assert parsed.hostname == "github.com"
    assert cast(str, source["revision"]) in parsed.path

    serialized = json.dumps(catalog, ensure_ascii=False)
    assert "/Users/" not in serialized
    assert "Dropbox/" not in serialized
    assert "student name" not in serialized.casefold()
