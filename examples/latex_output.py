"""LaTeX output examples."""

from sympy import Symbol, exp, integrate, latex
from core.types import make_example


@make_example("7. LaTeX出力")
def latex_output() -> tuple[str, ...]:
    """Demonstrate LaTeX output generation."""
    x = Symbol("x")

    # ガウス積分
    expr1 = integrate(exp(-(x**2)), x)
    latex1 = latex(expr1)

    # 有理式
    expr2 = (x**2 + 2 * x + 1) / (x**3 - 1)
    latex2 = latex(expr2)

    return (
        f"式: {expr1}",
        f"LaTeX: {latex1}",
        "",
        f"式: {expr2}",
        f"LaTeX: {latex2}",
    )
