from __future__ import annotations

import json
import runpy
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pytest

REPOSITORY_ROOT: Path = Path(__file__).resolve().parents[2]
TOOL_PATH: Path = REPOSITORY_ROOT / "tools/render_python_policy.py"
TOOL_NAMESPACE: dict[str, object] = runpy.run_path(str(TOOL_PATH))
SOURCE_PATH: Path = cast(Path, TOOL_NAMESPACE["SOURCE_PATH"])
PROJECTION_PATH: Path = cast(Path, TOOL_NAMESPACE["PROJECTION_PATH"])
VALIDATED_PROJECTION: Callable[[], bytes] = cast(
    Callable[[], bytes], TOOL_NAMESPACE["_validated_projection"]
)
LOAD_OBJECT: Callable[..., tuple[bytes, dict[str, object]]] = cast(
    Callable[..., tuple[bytes, dict[str, object]]],
    TOOL_NAMESPACE["_load_object"],
)


def _policy() -> dict[str, object]:
    return cast(dict[str, object], json.loads(SOURCE_PATH.read_bytes()))


def test__projection__matches_authoritative_policy() -> None:
    expected: bytes = VALIDATED_PROJECTION()

    assert PROJECTION_PATH.read_bytes() == expected


def test__object_model__uses_exact_operation_taxonomy() -> None:
    policy: dict[str, object] = _policy()
    object_model: dict[str, object] = cast(
        dict[str, object], policy["object_model"]
    )
    roles: list[dict[str, object]] = cast(
        list[dict[str, object]], object_model["roles"]
    )

    assert object_model["flow"] == [
        "data_object_action_request",
        "data_object_actionizer",
        "data_object_action_result",
    ]
    assert [role["display_name"] for role in roles] == [
        "DataObject",
        "DataObjectActionRequest",
        "DataObjectActionizer",
        "DataObjectActionResult",
    ]
    assert "DataObjectActionResponse" not in json.dumps(policy)


def test__optional_model__is_a_nonrequired_data_object_refinement() -> None:
    policy: dict[str, object] = _policy()
    object_model: dict[str, object] = cast(
        dict[str, object], policy["object_model"]
    )
    model: dict[str, object] = cast(
        dict[str, object], object_model["optional_model"]
    )

    assert model["display_name"] == "DataObjectModel"
    assert model["required"] is False
    assert "more specific DataObject classification" in cast(
        str, model["relationship"]
    )


def test__initializer_migrations__remain_separate() -> None:
    policy: dict[str, object] = _policy()
    initializers: dict[str, object] = cast(
        dict[str, object], policy["package_initializers"]
    )
    migration: dict[str, object] = cast(
        dict[str, object], initializers["migration"]
    )

    assert set(migration) == {
        "implementation_extraction",
        "facade_narrowing",
    }
    assert "deprecation" in json.dumps(migration["facade_narrowing"])
    assert "re-exports" in json.dumps(migration["implementation_extraction"])


def test__loader__rejects_duplicate_json_members(tmp_path: Path) -> None:
    source: Path = tmp_path / "duplicate.json"
    source.write_text('{"policy_id": "first", "policy_id": "second"}')

    with pytest.raises(ValueError, match="duplicate JSON member: policy_id"):
        LOAD_OBJECT(path=source)
