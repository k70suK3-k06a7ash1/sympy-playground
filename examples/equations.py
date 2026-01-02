"""Equation solving examples."""

from sympy import symbols, sin, solve, Eq, solveset, S
from core.types import make_example


@make_example("4. 方程式を解く")
def equations() -> tuple[str, ...]:
    """Demonstrate equation solving."""
    x, y = symbols("x y")

    # 代数方程式
    eq1 = x**2 - 5 * x + 6
    solutions1 = solve(eq1, x)

    # 連立方程式
    eq2 = Eq(x + y, 10)
    eq3 = Eq(x - y, 2)
    solutions2 = solve([eq2, eq3], [x, y])

    # 三角方程式
    solutions3 = solveset(sin(x), x, domain=S.Reals)

    return (
        f"x² - 5x + 6 = 0 の解: {solutions1}",
        f"x + y = 10, x - y = 2 の解: {solutions2}",
        f"sin(x) = 0 の解: {solutions3}",
    )
