"""Basic symbol operations."""

from sympy import symbols, factor
from core.types import Example, make_example


@make_example("1. 基本的なシンボル操作")
def basic_symbols() -> tuple[str, ...]:
    """Demonstrate basic symbol operations."""
    x, y, z = symbols("x y z")

    # 式の作成
    expr = x**2 + 2 * x * y + y**2

    # 値の代入
    result = expr.subs(x, 2).subs(y, 3)

    return (
        f"式: {expr}",
        f"x=2, y=3 を代入: {result}",
        f"因数分解: {factor(expr)}",
    )
