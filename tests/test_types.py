"""Tests for core types."""

import pytest
from returns.result import Success, Failure

from core.types import Example, ExampleResult, ExampleRunner, make_example


class TestExampleResult:
    """Tests for ExampleResult dataclass."""

    def test_to_lines_returns_formatted_output(self) -> None:
        result = ExampleResult(
            title="Test Title",
            outputs=("line 1", "line 2"),
        )
        lines = result.to_lines()

        assert lines[0] == "=" * 50
        assert lines[1] == "Test Title"
        assert lines[2] == "=" * 50
        assert lines[3] == "line 1"
        assert lines[4] == "line 2"
        assert lines[5] == ""

    def test_immutable(self) -> None:
        result = ExampleResult(title="Test", outputs=("a",))
        with pytest.raises(AttributeError):
            result.title = "Changed"  # type: ignore


class TestExample:
    """Tests for Example dataclass."""

    def test_execute_success(self) -> None:
        example = Example(
            title="Success Example",
            run=lambda: Success(("output 1", "output 2")),
        )
        result = example.execute()

        assert isinstance(result, Success)
        assert result.unwrap().title == "Success Example"
        assert result.unwrap().outputs == ("output 1", "output 2")

    def test_execute_failure(self) -> None:
        error = ValueError("test error")
        example = Example(
            title="Failure Example",
            run=lambda: Failure(error),
        )
        result = example.execute()

        assert isinstance(result, Failure)
        assert result.failure() == error


class TestMakeExample:
    """Tests for make_example decorator."""

    def test_creates_example_from_function(self) -> None:
        @make_example("Decorated Example")
        def sample() -> tuple[str, ...]:
            return ("result",)

        assert isinstance(sample, Example)
        assert sample.title == "Decorated Example"

    def test_wraps_success(self) -> None:
        @make_example("Success")
        def success_fn() -> tuple[str, ...]:
            return ("ok",)

        result = success_fn.execute()
        assert isinstance(result, Success)
        assert result.unwrap().outputs == ("ok",)

    def test_wraps_exception_in_failure(self) -> None:
        @make_example("Failure")
        def failing_fn() -> tuple[str, ...]:
            raise ValueError("boom")

        result = failing_fn.execute()
        assert isinstance(result, Failure)
        assert isinstance(result.failure(), ValueError)


class TestExampleRunner:
    """Tests for ExampleRunner."""

    def test_run_sequence_all_success(self) -> None:
        examples = (
            Example(title="A", run=lambda: Success(("a",))),
            Example(title="B", run=lambda: Success(("b",))),
        )
        runner = ExampleRunner(examples)
        result = runner.run_sequence()

        assert isinstance(result, Success)
        results = result.unwrap()
        assert len(results) == 2
        assert results[0].title == "A"
        assert results[1].title == "B"

    def test_run_sequence_fails_fast(self) -> None:
        error = ValueError("fail")
        call_count = 0

        def counting_success() -> Success[tuple[str, ...]]:
            nonlocal call_count
            call_count += 1
            return Success(("ok",))

        examples = (
            Example(title="A", run=counting_success),
            Example(title="B", run=lambda: Failure(error)),
            Example(title="C", run=counting_success),
        )
        runner = ExampleRunner(examples)
        result = runner.run_sequence()

        assert isinstance(result, Failure)
        assert result.failure() == error
        assert call_count == 1  # C was never executed

    def test_run_all_collects_all_results(self) -> None:
        error = ValueError("fail")
        examples = (
            Example(title="A", run=lambda: Success(("a",))),
            Example(title="B", run=lambda: Failure(error)),
            Example(title="C", run=lambda: Success(("c",))),
        )
        runner = ExampleRunner(examples)
        results = runner.run_all()

        assert len(results) == 3
        assert isinstance(results[0], Success)
        assert isinstance(results[1], Failure)
        assert isinstance(results[2], Success)
