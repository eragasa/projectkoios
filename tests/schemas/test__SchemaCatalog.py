from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import cast

import jsonschema
import pytest

REPOSITORY_ROOT: Path = Path(__file__).resolve().parents[2]
CATALOG_PATH: Path = REPOSITORY_ROOT / "schemas/catalog.json"
DECLARATION_FIXTURES: Path = (
    REPOSITORY_ROOT / "tests/fixtures/schemas/arch/python-test-declaration"
)


def _reject_duplicate_members(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    name: str
    value: object
    for name, value in pairs:
        if name in result:
            raise ValueError(f"duplicate member {name}")
        result[name] = value
    return result


def _load_object(*, path: Path) -> dict[str, object]:
    return cast(
        dict[str, object],
        json.loads(
            path.read_bytes(),
            object_pairs_hook=_reject_duplicate_members,
        ),
    )


def _catalog_entries() -> list[dict[str, object]]:
    catalog: dict[str, object] = _load_object(path=CATALOG_PATH)
    return cast(list[dict[str, object]], catalog["schemas"])


def _python_test_declaration_schema() -> dict[str, object]:
    return _load_object(
        path=(
            REPOSITORY_ROOT
            / "schemas/arch/python-test-declaration/0.1.0.schema.json"
        )
    )


def _development_task_schema() -> dict[str, object]:
    return _load_object(
        path=(
            REPOSITORY_ROOT / "schemas/dev/development-task/0.1.0.schema.json"
        )
    )


def _valid_development_task_document() -> dict[str, object]:
    parent_fields: dict[str, object] = {
        "inputs": [],
        "outputs": [],
        "changes": [],
        "acceptance": [],
        "non_goals": ["Execution authority."],
        "value": None,
        "estimated_size": None,
        "source_bindings": [
            {
                "source_id": "example-requirements",
                "source_label": "PARENT",
            }
        ],
    }
    leaf_fields: dict[str, object] = {
        "inputs": ["An accepted requirement."],
        "outputs": ["One bounded implementation artifact."],
        "changes": ["Implement the bounded requirement."],
        "acceptance": ["The declared check passes."],
        "non_goals": ["Publication."],
        "value": "risk_reduction",
        "estimated_size": "small",
        "source_bindings": [
            {
                "source_id": "example-requirements",
                "source_label": "LEAF",
            }
        ],
    }
    return {
        "schema_version": 1,
        "document_id": "projectkoios.dev.example",
        "document_version": "0.1.0",
        "status": "OBSERVED_UNVALIDATED",
        "title": "DevelopmentTask graph example",
        "authority": {
            "source_format": "json",
            "projection_format": "markdown",
            "source_path": "docs/candidates/example.json",
            "projection_path": "docs/candidates/example.md",
            "projection_status": "generated",
        },
        "purpose": "Demonstrate many-to-many structural decomposition.",
        "source_materials": [
            {
                "source_id": "example-requirements",
                "role": "requirements_source",
                "repository_path": "docs/candidates/example.md",
                "sha256": (
                    "00000000000000000000000000000000"
                    "00000000000000000000000000000000"
                ),
                "byte_count": 1,
            }
        ],
        "tasks": [
            {
                "task_id": "DEV-0001",
                "title": "First parent",
                "objective": "Group one bounded outcome.",
                **parent_fields,
            },
            {
                "task_id": "DEV-0002",
                "title": "Second parent",
                "objective": "Group another bounded outcome.",
                **parent_fields,
            },
            {
                "task_id": "DEV-0003",
                "title": "Shared child",
                "objective": "Contribute to both parent outcomes.",
                **leaf_fields,
            },
            {
                "task_id": "DEV-0004",
                "title": "Additional child",
                "objective": "Contribute to the first parent outcome.",
                **leaf_fields,
            },
        ],
        "decomposition_edges": [
            {
                "parent_task_id": "DEV-0001",
                "child_task_id": "DEV-0003",
            },
            {
                "parent_task_id": "DEV-0002",
                "child_task_id": "DEV-0003",
            },
            {
                "parent_task_id": "DEV-0001",
                "child_task_id": "DEV-0004",
            },
        ],
        "dependency_edges": [],
    }


def test__schema_catalog__identities_and_bytes_match_sources() -> None:
    seen_ids: set[str] = set()
    registered_paths: set[str] = set()
    entry: dict[str, object]
    for entry in _catalog_entries():
        schema_id: str = cast(str, entry["schema_id"])
        source_path: str = cast(str, entry["source_path"])
        expected_sha256: str = cast(str, entry["sha256"])
        expected_byte_count: int = cast(int, entry["byte_count"])
        source: Path = REPOSITORY_ROOT / source_path
        assert schema_id not in seen_ids
        assert source_path not in registered_paths
        assert source.is_file()
        assert not source.is_symlink()
        payload: bytes = source.read_bytes()
        schema: dict[str, object] = _load_object(path=source)
        assert schema["$id"] == schema_id
        assert hashlib.sha256(payload).hexdigest() == expected_sha256
        assert len(payload) == expected_byte_count
        jsonschema.Draft202012Validator.check_schema(schema)
        seen_ids.add(schema_id)
        registered_paths.add(source_path)


def test__schema_catalog__registers_every_schema_file() -> None:
    registered_paths: set[str] = {
        cast(str, entry["source_path"]) for entry in _catalog_entries()
    }
    discovered_paths: set[str] = {
        path.relative_to(REPOSITORY_ROOT).as_posix()
        for path in REPOSITORY_ROOT.rglob("*.schema.json")
        if ".venv" not in path.parts
    }

    assert registered_paths == discovered_paths


@pytest.mark.parametrize(
    ("schema_path", "document_path"),
    (
        (
            "docs/policies/code/python.schema.json",
            "docs/policies/code/python.json",
        ),
        (
            "docs/policies/code/python_test.schema.json",
            "docs/policies/code/python_test.json",
        ),
    ),
)
def test__policy_schema__accepts_authoritative_document(
    schema_path: str,
    document_path: str,
) -> None:
    schema: dict[str, object] = _load_object(path=REPOSITORY_ROOT / schema_path)
    document: dict[str, object] = _load_object(
        path=REPOSITORY_ROOT / document_path
    )

    jsonschema.Draft202012Validator(schema).validate(document)


@pytest.mark.parametrize(
    ("schema_path", "document_path"),
    (
        (
            "docs/policies/code/python.schema.json",
            "docs/policies/code/python.json",
        ),
        (
            "docs/policies/code/python_test.schema.json",
            "docs/policies/code/python_test.json",
        ),
    ),
)
def test__policy_schema__rejects_unknown_root_field(
    schema_path: str,
    document_path: str,
) -> None:
    schema: dict[str, object] = _load_object(path=REPOSITORY_ROOT / schema_path)
    document: dict[str, object] = _load_object(
        path=REPOSITORY_ROOT / document_path
    )
    document["unknown"] = "prohibited"

    assert not jsonschema.Draft202012Validator(schema).is_valid(document)


@pytest.mark.parametrize(
    "fixture_name",
    (
        "valid-routine-evidence.json",
        "valid-claim-bearing-numerical.json",
        "valid-provider-contract.json",
        "valid-duration-regression.json",
    ),
)
def test__python_test_declaration_schema__accepts_valid_vectors(
    fixture_name: str,
) -> None:
    declaration: dict[str, object] = _load_object(
        path=DECLARATION_FIXTURES / fixture_name
    )
    validator = jsonschema.Draft202012Validator(
        _python_test_declaration_schema()
    )

    validator.validate(declaration)


def test__python_test_declaration_schema__rejects_invalid_vectors() -> None:
    vector_document: dict[str, object] = _load_object(
        path=DECLARATION_FIXTURES / "invalid-vectors.json"
    )
    vectors: list[dict[str, object]] = cast(
        list[dict[str, object]],
        vector_document["vectors"],
    )
    validator = jsonschema.Draft202012Validator(
        _python_test_declaration_schema()
    )
    vector: dict[str, object]
    for vector in vectors:
        base_fixture: str = cast(str, vector["base_fixture"])
        declaration: dict[str, object] = copy.deepcopy(
            _load_object(path=DECLARATION_FIXTURES / base_fixture)
        )
        path: list[object] = cast(list[object], vector["path"])
        target: object = declaration
        part: object
        for part in path[:-1]:
            if type(part) is str and type(target) is dict:
                target = target[part]
            elif type(part) is int and type(target) is list:
                target = target[part]
            else:
                raise AssertionError("invalid conformance-vector path")
        final_part: object = path[-1]
        if type(final_part) is str and type(target) is dict:
            target[final_part] = vector["value"]
        elif type(final_part) is int and type(target) is list:
            target[final_part] = vector["value"]
        else:
            raise AssertionError("invalid conformance-vector target")
        errors: list[jsonschema.ValidationError] = list(
            validator.iter_errors(declaration)
        )

        assert errors, vector["case_id"]
        assert cast(str, vector["expected_keyword"]) in {
            error.validator for error in errors
        }, vector["case_id"]


def test__development_task_schema__accepts_many_to_many_structure() -> None:
    validator = jsonschema.Draft202012Validator(_development_task_schema())

    assert validator.is_valid(_valid_development_task_document())


def test__development_task_schema__rejects_unknown_root_field() -> None:
    document: dict[str, object] = _valid_development_task_document()
    document["unknown"] = True
    validator = jsonschema.Draft202012Validator(_development_task_schema())

    assert not validator.is_valid(document)
