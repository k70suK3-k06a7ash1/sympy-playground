"""Tests for SymPy examples."""

import pytest
from returns.result import Success

from examples.basic import basic_symbols
from examples.simplification import simplification
from examples.calculus import calculus
from examples.equations import equations
from examples.matrices import matrices
from examples.special import special_functions
from examples.latex_output import latex_output
from examples.differential_equations import differential_equations
from examples import ALL_EXAMPLES


class TestBasicSymbols:
    """Tests for basic symbol operations."""

    def test_executes_successfully(self) -> None:
        result = basic_symbols.execute()
        assert isinstance(result, Success)

    def test_outputs_contain_expected_content(self) -> None:
        result = basic_symbols.execute().unwrap()
        outputs = result.outputs

        assert any("x**2 + 2*x*y + y**2" in o for o in outputs)
        assert any("25" in o for o in outputs)
        assert any("(x + y)**2" in o for o in outputs)


class TestSimplification:
    """Tests for simplification examples."""

    def test_executes_successfully(self) -> None:
        result = simplification.execute()
        assert isinstance(result, Success)

    def test_pythagorean_identity(self) -> None:
        result = simplification.execute().unwrap()
        outputs = result.outputs

        assert any("sin" in o and "cos" in o and "= 1" in o for o in outputs)


class TestCalculus:
    """Tests for calculus examples."""

    def test_executes_successfully(self) -> None:
        result = calculus.execute()
        assert isinstance(result, Success)

    def test_derivative(self) -> None:
        result = calculus.execute().unwrap()
        outputs = result.outputs

        assert any("f'(x)" in o for o in outputs)

    def test_integral(self) -> None:
        result = calculus.execute().unwrap()
        outputs = result.outputs

        assert any("∫" in o or "sin" in o for o in outputs)


class TestEquations:
    """Tests for equation solving examples."""

    def test_executes_successfully(self) -> None:
        result = equations.execute()
        assert isinstance(result, Success)

    def test_quadratic_solution(self) -> None:
        result = equations.execute().unwrap()
        outputs = result.outputs

        # x^2 - 5x + 6 = 0 has solutions 2 and 3
        assert any("[2, 3]" in o for o in outputs)


class TestMatrices:
    """Tests for matrix operation examples."""

    def test_executes_successfully(self) -> None:
        result = matrices.execute()
        assert isinstance(result, Success)

    def test_determinant(self) -> None:
        result = matrices.execute().unwrap()
        outputs = result.outputs

        # det([[1,2],[3,4]]) = -2
        assert any("det(A) = -2" in o for o in outputs)


class TestSpecialFunctions:
    """Tests for special functions examples."""

    def test_executes_successfully(self) -> None:
        result = special_functions.execute()
        assert isinstance(result, Success)

    def test_euler_identity(self) -> None:
        result = special_functions.execute().unwrap()
        outputs = result.outputs

        assert any("e^(iπ) + 1 = 0" in o for o in outputs)


class TestLatexOutput:
    """Tests for LaTeX output examples."""

    def test_executes_successfully(self) -> None:
        result = latex_output.execute()
        assert isinstance(result, Success)

    def test_produces_latex(self) -> None:
        result = latex_output.execute().unwrap()
        outputs = result.outputs

        assert any("LaTeX:" in o for o in outputs)
        assert any("\\" in o for o in outputs)  # LaTeX commands contain backslash


class TestDifferentialEquations:
    """Tests for differential equation examples."""

    def test_executes_successfully(self) -> None:
        result = differential_equations.execute()
        assert isinstance(result, Success)

    def test_ode_solution(self) -> None:
        result = differential_equations.execute().unwrap()
        outputs = result.outputs

        assert any("一般解" in o for o in outputs)


class TestAllExamples:
    """Integration tests for all examples."""

    def test_all_examples_count(self) -> None:
        assert len(ALL_EXAMPLES) == 8

    @pytest.mark.parametrize("example", ALL_EXAMPLES)
    def test_each_example_executes_successfully(self, example) -> None:
        result = example.execute()
        assert isinstance(result, Success), f"{example.title} failed: {result}"

    @pytest.mark.parametrize("example", ALL_EXAMPLES)
    def test_each_example_produces_output(self, example) -> None:
        result = example.execute().unwrap()
        assert len(result.outputs) > 0, f"{example.title} produced no output"
