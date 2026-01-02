"""SymPy 使用例集 - Monadic Pattern with returns library."""

from returns.result import Success, Failure

from sympy import init_printing

from core.types import ExampleRunner
from core.printer import print_results, print_completion
from examples import ALL_EXAMPLES


def main() -> None:
    """Run all examples using monadic composition."""
    init_printing(use_unicode=True)

    runner = ExampleRunner(ALL_EXAMPLES)

    # Run all examples with monadic composition (fail-fast)
    match runner.run_sequence():
        case Success(results):
            print_results(results)._inner_value()
            print_completion()._inner_value()

        case Failure(err):
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
