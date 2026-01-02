"""Output printing utilities."""

from returns.io import IO
from core.types import ExampleResult


def print_header(title: str) -> IO[None]:
    """Print a section header."""

    def _print() -> None:
        print("=" * 50)
        print(title)
        print("=" * 50)

    return IO(_print)


def print_result(result: ExampleResult) -> IO[None]:
    """Print an example result."""

    def _print() -> None:
        for line in result.to_lines():
            print(line)

    return IO(_print)


def print_results(results: tuple[ExampleResult, ...]) -> IO[None]:
    """Print multiple example results."""

    def _print() -> None:
        for result in results:
            for line in result.to_lines():
                print(line)

    return IO(_print)


def print_completion() -> IO[None]:
    """Print completion message."""

    def _print() -> None:
        print("=" * 50)
        print("SymPy 使用例 完了!")
        print("=" * 50)

    return IO(_print)
