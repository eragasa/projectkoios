from __future__ import annotations

import inspect
from dataclasses import dataclass

from projectkoios import base
from projectkoios.base import (
    DataObject,
    DataObjectActionizer,
    DataObjectActionRequest,
    DataObjectActionResult,
    DataObjectModel,
)


@dataclass(frozen=True, slots=True)
class ExampleRequest(DataObjectActionRequest):
    value: int


@dataclass(frozen=True, slots=True)
class ExampleResult(DataObjectActionResult):
    doubled_value: int


class ExampleActionizer(DataObjectActionizer[ExampleRequest, ExampleResult]):
    def action(self, *, request: ExampleRequest) -> ExampleResult:
        return ExampleResult(doubled_value=2 * request.value)


def test__base__defines_exact_public_abcs_without_base_object() -> None:
    assert base.__all__ == (
        "DataObject",
        "DataObjectActionRequest",
        "DataObjectActionResult",
        "DataObjectActionizer",
        "DataObjectModel",
    )
    assert not hasattr(base, "BaseObject")


def test__data_object__is_a_thin_abstract_struct_boundary() -> None:
    assert inspect.isabstract(DataObject)
    assert DataObject.__abstractmethods__ == frozenset({"__init__"})


def test__data_object_model__is_an_immutable_data_object_boundary() -> None:
    request: ExampleRequest = ExampleRequest(value=3)
    result: ExampleResult = ExampleResult(doubled_value=6)

    assert isinstance(request, DataObjectModel)
    assert isinstance(request, DataObject)
    assert isinstance(result, DataObjectModel)
    assert isinstance(result, DataObject)


def test__request_and_result__have_the_exact_model_hierarchy() -> None:
    assert issubclass(DataObjectActionRequest, DataObjectModel)
    assert issubclass(DataObjectActionResult, DataObjectModel)


def test__actionizer__is_a_function_like_abstract_boundary() -> None:
    actionizer: ExampleActionizer = ExampleActionizer()

    assert inspect.isabstract(DataObjectActionizer)
    assert not issubclass(DataObjectActionizer, DataObject)
    assert actionizer.action(request=ExampleRequest(value=4)) == ExampleResult(
        doubled_value=8
    )
