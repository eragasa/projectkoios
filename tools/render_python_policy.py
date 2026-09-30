"""Render or check the one Project Koios Python-policy projection.

This tool is intentionally limited to ``docs/policies/code/python.json`` and
its schema and Markdown projection. It is not a generic policy, architecture,
or workflow renderer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import cast

import jsonschema  # type: ignore[import-untyped]

REPOSITORY_ROOT: Path = Path(__file__).resolve().parents[1]
SOURCE_PATH: Path = REPOSITORY_ROOT / "docs/policies/code/python.json"
SCHEMA_PATH: Path = REPOSITORY_ROOT / "docs/policies/code/python.schema.json"
PROJECTION_PATH: Path = REPOSITORY_ROOT / "docs/policies/code/python.md"
MAX_INPUT_BYTES: int = 1_000_000

JsonObject = dict[str, object]


def _reject_duplicate_members(
    pairs: list[tuple[str, object]],
) -> JsonObject:
    result: JsonObject = {}
    name: str
    value: object
    for name, value in pairs:
        if name in result:
            raise ValueError(f"duplicate JSON member: {name}")
        result[name] = value
    return result


def _reject_json_constant(value: str) -> object:
    raise ValueError(f"prohibited JSON constant: {value}")


def _load_object(*, path: Path) -> tuple[bytes, JsonObject]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"input must be a regular non-symlinked file: {path}")
    payload: bytes = path.read_bytes()
    if len(payload) > MAX_INPUT_BYTES:
        raise ValueError(f"input exceeds {MAX_INPUT_BYTES} bytes: {path}")
    value: object = json.loads(
        payload,
        object_pairs_hook=_reject_duplicate_members,
        parse_constant=_reject_json_constant,
    )
    if type(value) is not dict:
        raise ValueError(f"JSON root must be an object: {path}")
    return payload, cast(JsonObject, value)


def _object(*, value: object, label: str) -> JsonObject:
    if type(value) is not dict:
        raise ValueError(f"{label} must be an object")
    return cast(JsonObject, value)


def _objects(*, value: object, label: str) -> list[JsonObject]:
    if type(value) is not list:
        raise ValueError(f"{label} must be a list")
    result: list[JsonObject] = []
    item: object
    for item in cast(list[object], value):
        result.append(_object(value=item, label=f"{label} item"))
    return result


def _string(*, value: object, label: str) -> str:
    if type(value) is not str:
        raise ValueError(f"{label} must be a string")
    return cast(str, value)


def _strings(*, value: object, label: str) -> list[str]:
    if type(value) is not list:
        raise ValueError(f"{label} must be a list")
    result: list[str] = []
    item: object
    for item in cast(list[object], value):
        result.append(_string(value=item, label=f"{label} item"))
    return result


def _field(*, owner: JsonObject, name: str) -> object:
    try:
        return owner[name]
    except KeyError as error:
        raise ValueError(f"missing field: {name}") from error


def _add_list(*, lines: list[str], values: list[str]) -> None:
    value: str
    for value in values:
        lines.append(f"- {value}")


def _render_role(*, lines: list[str], role: JsonObject) -> None:
    display_name: str = _string(
        value=_field(owner=role, name="display_name"),
        label="role display_name",
    )
    python_form: str = _string(
        value=_field(owner=role, name="default_python_form"),
        label="role default_python_form",
    )
    lines.extend(
        [
            f"### {display_name}",
            "",
            f"Default Python form: {python_form}.",
            "",
            "Responsibilities:",
            "",
        ]
    )
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=role, name="responsibilities"),
            label="role responsibilities",
        ),
    )
    lines.extend(["", "Prohibitions:", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=role, name="prohibitions"),
            label="role prohibitions",
        ),
    )
    lines.append("")


def _render_google_rules(
    *,
    lines: list[str],
    source: JsonObject,
    extraction: JsonObject,
) -> None:
    revision: str = _string(
        value=_field(owner=source, name="revision"),
        label="Google revision",
    )
    document_url: str = _string(
        value=_field(owner=source, name="document_url"),
        label="Google document URL",
    )
    license_url: str = _string(
        value=_field(owner=source, name="license_url"),
        label="Google license URL",
    )
    lines.extend(
        [
            "## Google Python Style Guide profile",
            "",
            "Project Koios applies explicit source-linked dispositions to a "
            "pinned Google Python Style Guide revision. The owning repository "
            "remains authoritative where an extracted rule is adapted.",
            "",
            "### Upstream source",
            "",
            f"- Title: [Google Python Style Guide]({document_url})",
            f"- Revision: `{revision}`",
            "- Git blob SHA-1: "
            f"`{_field(owner=source, name='blob_sha1')}`",
            "- Source SHA-256: "
            f"`{_field(owner=source, name='sha256')}`",
            f"- Source byte count: `{_field(owner=source, name='byte_count')}`",
            "- License: "
            f"[{_field(owner=source, name='license')}]({license_url})",
            "",
            "This projection identifies modifications through explicit `ADAPT` "
            "dispositions and attributes the upstream guide to Google under "
            "CC BY 3.0.",
            "",
            "### Extraction coverage",
            "",
            _string(
                value=_field(owner=extraction, name="scope"),
                label="extraction scope",
            ),
            "",
            _string(
                value=_field(owner=extraction, name="method"),
                label="extraction method",
            ),
            "",
            "### Rule dispositions",
            "",
        ]
    )
    rule: JsonObject
    for rule in _objects(
        value=_field(owner=extraction, name="rules"),
        label="Google rules",
    ):
        section: str = _string(
            value=_field(owner=rule, name="section"),
            label="rule section",
        )
        title: str = _string(
            value=_field(owner=rule, name="title"),
            label="rule title",
        )
        anchor: str = _string(
            value=_field(owner=rule, name="anchor"),
            label="rule anchor",
        )
        disposition: str = _string(
            value=_field(owner=rule, name="disposition"),
            label="rule disposition",
        )
        excerpt: str = _string(
            value=_field(owner=rule, name="source_excerpt"),
            label="source excerpt",
        )
        lines.extend(
            [
                f"#### {section} {title} — {disposition}",
                "",
                f"- Rule ID: `{_field(owner=rule, name='rule_id')}`",
                f"- Upstream section: [{section}]({document_url}#{anchor})",
                "",
                "Upstream excerpt:",
                "",
                f"> {excerpt}",
                "",
                "Project Koios rule:",
                "",
                _string(
                    value=_field(owner=rule, name="project_rule"),
                    label="project rule",
                ),
                "",
                "Rationale:",
                "",
                _string(
                    value=_field(owner=rule, name="rationale"),
                    label="rule rationale",
                ),
                "",
            ]
        )


def render(*, source_bytes: bytes, document: JsonObject) -> bytes:
    object_model: JsonObject = _object(
        value=_field(owner=document, name="object_model"),
        label="object_model",
    )
    initializer_policy: JsonObject = _object(
        value=_field(owner=document, name="package_initializers"),
        label="package_initializers",
    )
    lines: list[str] = [
        "<!-- GENERATED FILE. DO NOT EDIT. -->",
        "",
        f"# {_field(owner=document, name='title')}",
        "",
        "> **GENERATED MARKDOWN PROJECTION.**",
        "> [`docs/policies/code/python.json`](python.json) is authoritative.",
        "> Regenerate this file with "
        "`python3.14 -m tools.render_python_policy --write`; do not edit it "
        "independently.",
        "",
        f"- Policy ID: `{_field(owner=document, name='policy_id')}`",
        f"- Policy version: `{_field(owner=document, name='policy_version')}`",
        f"- Status: **{_field(owner=document, name='status')}**",
        "- Source SHA-256: "
        f"`{hashlib.sha256(source_bytes).hexdigest()}`",
        "",
        "## Purpose",
        "",
        _string(
            value=_field(owner=document, name="purpose"),
            label="purpose",
        ),
        "",
        "## Scope",
        "",
    ]
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=document, name="scope"),
            label="scope",
        ),
    )
    lines.extend(["", "## Exclusions", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=document, name="exclusions"),
            label="exclusions",
        ),
    )
    lines.extend(["", "## Precedence", "", "From highest to lowest:", ""])
    precedence: list[str] = _strings(
        value=_field(owner=document, name="precedence"),
        label="precedence",
    )
    index: int
    value: str
    for index, value in enumerate(precedence, start=1):
        lines.append(f"{index}. {value}")
    lines.extend(
        [
            "",
            "## Object model",
            "",
            "The domain-operation flow is:",
            "",
            "```text",
            "DataObjectActionRequest → DataObjectActionizer → "
            "DataObjectActionResult",
            "```",
            "",
            "A request identifies its input `DataObject` values and, only when "
            "the domain needs one, an exact `DataObjectModel`.",
            "",
            "These are architecture roles. They do not require public base "
            "classes with the taxonomy names.",
            "",
            "```mermaid",
            "classDiagram",
            "    class DataObject {",
            "        <<architecture role>>",
            "        immutable domain state",
            "        intrinsic invariants",
            "    }",
            "    class DataObjectModel {",
            "        <<optional DataObject role>>",
            "        immutable domain model",
            "    }",
            "    class DataObjectActionRequest {",
            "        <<architecture role>>",
            "        immutable operation intent",
            "    }",
            "    class DataObjectActionizer {",
            "        <<architecture role>>",
            "        explicit dependencies",
            "        one named operation",
            "    }",
            "    class DataObjectActionResult {",
            "        <<architecture role>>",
            "        immutable closed outcome",
            "    }",
            "",
            "    DataObjectModel --> DataObject : refines classification",
            "    DataObjectActionRequest --> DataObject : identifies input",
            "    DataObjectActionRequest --> DataObjectModel : optionally uses",
            "    DataObjectActionizer --> DataObjectActionRequest : processes",
            "    DataObjectActionizer --> DataObjectActionResult : returns",
            "    DataObjectActionResult --> DataObjectActionRequest "
            ": identifies",
            "```",
            "",
        ]
    )
    role: JsonObject
    for role in _objects(
        value=_field(owner=object_model, name="roles"),
        label="object model roles",
    ):
        _render_role(lines=lines, role=role)
    optional_model: JsonObject = _object(
        value=_field(owner=object_model, name="optional_model"),
        label="optional_model",
    )
    lines.extend(
        [
            "### Optional DataObjectModel",
            "",
            _string(
                value=_field(owner=optional_model, name="relationship"),
                label="model relationship",
            ),
            "",
        ]
    )
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=optional_model, name="rules"),
            label="model rules",
        ),
    )
    lines.extend(["", "### Object-model rules", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=object_model, name="rules"),
            label="object model rules",
        ),
    )
    lines.extend(
        [
            "",
            "## Package initializers",
            "",
            _string(
                value=_field(owner=initializer_policy, name="principle"),
                label="initializer principle",
            ),
            "",
            "### Rules",
            "",
        ]
    )
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=initializer_policy, name="rules"),
            label="initializer rules",
        ),
    )
    migration: JsonObject = _object(
        value=_field(owner=initializer_policy, name="migration"),
        label="initializer migration",
    )
    lines.extend(["", "### Implementation extraction", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=migration, name="implementation_extraction"),
            label="implementation extraction",
        ),
    )
    lines.extend(["", "### Facade narrowing", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=migration, name="facade_narrowing"),
            label="facade narrowing",
        ),
    )
    lines.append("")
    google: JsonObject = _object(
        value=_field(owner=document, name="google_python_style"),
        label="google_python_style",
    )
    _render_google_rules(
        lines=lines,
        source=_object(
            value=_field(owner=google, name="source"),
            label="Google source",
        ),
        extraction=_object(
            value=_field(owner=google, name="extraction"),
            label="Google extraction",
        ),
    )
    lines.extend(["## Python rules", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=document, name="python_rules"),
            label="Python rules",
        ),
    )
    validation: JsonObject = _object(
        value=_field(owner=document, name="validation"),
        label="validation",
    )
    lines.extend(["", "## Minimum validation", "", "```bash"])
    lines.extend(
        _strings(
            value=_field(owner=validation, name="minimum_commands"),
            label="minimum commands",
        )
    )
    lines.extend(["```", ""])
    validation_rules: list[str] = _strings(
        value=_field(owner=validation, name="rules"),
        label="validation rules",
    )
    validation_rule: str
    for validation_rule in validation_rules:
        lines.extend([validation_rule, ""])
    lines.extend(["## Deferred decisions", ""])
    _add_list(
        lines=lines,
        values=_strings(
            value=_field(owner=document, name="deferred"),
            label="deferred decisions",
        ),
    )
    return ("\n".join(lines) + "\n").encode("utf-8")


def _validated_projection() -> bytes:
    source_bytes: bytes
    document: JsonObject
    source_bytes, document = _load_object(path=SOURCE_PATH)
    _schema_bytes: bytes
    schema: JsonObject
    _schema_bytes, schema = _load_object(path=SCHEMA_PATH)
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(document)
    return render(source_bytes=source_bytes, document=document)


def _check() -> int:
    expected: bytes = _validated_projection()
    if PROJECTION_PATH.is_symlink() or not PROJECTION_PATH.is_file():
        print(
            f"projection is not a regular file: {PROJECTION_PATH}",
            file=sys.stderr,
        )
        return 1
    actual: bytes = PROJECTION_PATH.read_bytes()
    if actual != expected:
        print(
            "Python-policy projection drift: run "
            "python3.14 -m tools.render_python_policy --write",
            file=sys.stderr,
        )
        return 1
    print("Python-policy projection is current.")
    return 0


def _write() -> int:
    expected: bytes = _validated_projection()
    if PROJECTION_PATH.is_symlink():
        print(
            f"refusing to replace symlink: {PROJECTION_PATH}",
            file=sys.stderr,
        )
        return 1
    PROJECTION_PATH.write_bytes(expected)
    print(f"Wrote {PROJECTION_PATH.relative_to(REPOSITORY_ROOT)}")
    return 0


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Render or check the fixed Project Koios Python policy.",
    )
    mode: argparse._MutuallyExclusiveGroup = (
        parser.add_mutually_exclusive_group(required=True)
    )
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    arguments: argparse.Namespace = parser.parse_args()
    try:
        if arguments.check:
            return _check()
        return _write()
    except (
        OSError,
        UnicodeDecodeError,
        json.JSONDecodeError,
        jsonschema.SchemaError,
        jsonschema.ValidationError,
        ValueError,
    ) as error:
        print(f"Python-policy projection failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
