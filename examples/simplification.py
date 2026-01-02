"""Expression simplification examples."""

from sympy import symbols, sin, cos, simplify, expand, factor, trigsimp
from core.types import make_example


@make_example("2. 式の簡略化")
def simplification() -> tuple[str, ...]:
    """Demonstrate expression simplification."""
    x, y = symbols("x y")

    # simplify: ピタゴラスの定理
    expr1 = sin(x) ** 2 + cos(x) ** 2

    # expand: 展開
    expr2 = (x + 1) ** 3

    # factor: 因数分解
    expr3 = x**3 - x**2 + x - 1

    # trigsimp: 三角関数の簡略化
    expr4 = sin(x) * cos(y) + cos(x) * sin(y)

    return (
        f"sin²(x) + cos²(x) = {simplify(expr1)}",
        f"(x + 1)³ 展開 = {expand(expr2)}",
        f"x³ - x² + x - 1 因数分解 = {factor(expr3)}",
        f"sin(x)cos(y) + cos(x)sin(y) = {trigsimp(expr4)}",
    )
