"""Core types using monadic patterns with returns library."""

from dataclasses import dataclass
from typing import Callable
from returns.result import Result, Success, Failure
from returns.io import IO
from returns.curry import curry
from returns.pipeline import pipe


@dataclass(frozen=True)
class ExampleResult:
    """Result of running an example."""

    title: str
    outputs: tuple[str, ...]

    def to_lines(self) -> tuple[str, ...]:
        """Convert to printable lines."""
        return (
            "=" * 50,
            self.title,
            "=" * 50,
            *self.outputs,
            "",
        )


@dataclass(frozen=True)
class Example:
    """An example that produces results."""

    title: str
    run: Callable[[], Result[tuple[str, ...], Exception]]

    def execute(self) -> Result[ExampleResult, Exception]:
        """Execute the example and return result."""
        return self.run().map(
            lambda outputs: ExampleResult(title=self.title, outputs=outputs)
        )


def make_example(
    title: str,
) -> Callable[[Callable[[], tuple[str, ...]]], Example]:
    """Decorator to create an Example from a function."""

    def decorator(fn: Callable[[], tuple[str, ...]]) -> Example:
        def safe_run() -> Result[tuple[str, ...], Exception]:
            try:
                return Success(fn())
            except Exception as e:
                return Failure(e)

        return Example(title=title, run=safe_run)

    return decorator


class ExampleRunner:
    """Runner that composes and executes examples monadically."""

    def __init__(self, examples: tuple[Example, ...]) -> None:
        self._examples = examples

    def run_all(self) -> tuple[Result[ExampleResult, Exception], ...]:
        """Run all examples, collecting all results (both success and failure)."""
        return tuple(example.execute() for example in self._examples)

    def run_sequence(self) -> Result[tuple[ExampleResult, ...], Exception]:
        """Run all examples, failing fast on first error (monadic bind)."""
        results: list[ExampleResult] = []

        for example in self._examples:
            match example.execute():
                case Success(result):
                    results.append(result)
                case Failure(err):
                    return Failure(err)

        return Success(tuple(results))

    def run_io(self) -> IO[Result[tuple[ExampleResult, ...], Exception]]:
        """Run as IO action for deferred execution."""
        return IO(self.run_sequence)
