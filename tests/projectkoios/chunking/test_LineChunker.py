from pathlib import Path

import pytest
from projectkoios.chunking import LineChunker


def test__chunk_text__returns_single_chunk_for_short_text() -> None:
    chunker = LineChunker(lines_per_chunk=10, overlap_lines=0)

    chunks = list(
        chunker.chunk_text(
            text="a\nb\nc\n",
            source_path=Path("src/example.py"),
            source_kind="code_file",
            language="python",
        )
    )

    assert len(chunks) == 1
    assert chunks[0].chunk_index == 0
    assert chunks[0].start_line == 1
    assert chunks[0].end_line == 3
    assert chunks[0].text == "a\nb\nc\n"
    assert chunks[0].source_path == Path("src/example.py")
    assert chunks[0].source_kind == "code_file"
    assert chunks[0].language == "python"


def test__chunk_text__splits_long_text_into_line_windows() -> None:
    chunker = LineChunker(lines_per_chunk=3, overlap_lines=0)

    text = "1\n2\n3\n4\n5\n"

    chunks = list(
        chunker.chunk_text(
            text=text,
            source_path=Path("src/example.py"),
            source_kind="code_file",
            language="python",
        )
    )

    assert len(chunks) == 2

    assert chunks[0].chunk_index == 0
    assert chunks[0].start_line == 1
    assert chunks[0].end_line == 3
    assert chunks[0].text == "1\n2\n3\n"

    assert chunks[1].chunk_index == 1
    assert chunks[1].start_line == 4
    assert chunks[1].end_line == 5
    assert chunks[1].text == "4\n5\n"


def test__chunk_text__supports_overlap() -> None:
    chunker = LineChunker(lines_per_chunk=3, overlap_lines=1)

    text = "1\n2\n3\n4\n5\n"

    chunks = list(
        chunker.chunk_text(
            text=text,
            source_path=Path("src/example.py"),
            source_kind="code_file",
            language="python",
        )
    )

    assert len(chunks) == 2

    assert chunks[0].chunk_index == 0
    assert chunks[0].start_line == 1
    assert chunks[0].end_line == 3
    assert chunks[0].text == "1\n2\n3\n"

    assert chunks[1].chunk_index == 1
    assert chunks[1].start_line == 3
    assert chunks[1].end_line == 5
    assert chunks[1].text == "3\n4\n5\n"


def test__chunk_text__returns_no_chunks_for_empty_text() -> None:
    chunker = LineChunker(lines_per_chunk=3, overlap_lines=0)

    chunks = list(
        chunker.chunk_text(
            text="",
            source_path=Path("src/example.py"),
            source_kind="code_file",
            language="python",
        )
    )

    assert chunks == []


def test__init__rejects_non_positive_lines_per_chunk() -> None:
    with pytest.raises(ValueError, match="lines_per_chunk must be positive"):
        LineChunker(lines_per_chunk=0, overlap_lines=0)


def test__init__rejects_negative_overlap() -> None:
    with pytest.raises(ValueError, match="overlap_lines must be non-negative"):
        LineChunker(lines_per_chunk=10, overlap_lines=-1)


def test__init__rejects_overlap_greater_than_or_equal_to_chunk_size() -> None:
    with pytest.raises(
        ValueError,
        match="overlap_lines must be less than lines_per_chunk",
    ):
        LineChunker(lines_per_chunk=10, overlap_lines=10)