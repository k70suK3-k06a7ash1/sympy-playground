"""Special functions and constants examples."""

from sympy import (
    symbols,
    pi,
    E,
    I,
    exp,
    simplify,
    Rational,
    factorial,
    binomial,
    summation,
)
from core.types import make_example


@make_example("6. 特殊関数と定数")
def special_functions() -> tuple[str, ...]:
    """Demonstrate special functions and constants."""
    n, k = symbols("n k")

    # 数学定数
    pi_val = pi.evalf()
    e_val = E.evalf()
    i_squared = I**2

    # オイラーの等式
    euler = simplify(exp(I * pi) + 1)

    # 有理数演算
    rational_sum = Rational(1, 3) + Rational(1, 6)

    # 階乗と二項係数
    fact_10 = factorial(10)
    binom_10_3 = binomial(10, 3)

    # 総和
    sum_symbolic = summation(k, (k, 1, n))
    sum_numeric = summation(k, (k, 1, 100))

    return (
        f"円周率 π = {pi_val}",
        f"自然対数の底 e = {e_val}",
        f"虚数単位 i² = {i_squared}",
        "",
        f"オイラーの等式: e^(iπ) + 1 = {euler}",
        "",
        f"有理数: 1/3 + 1/6 = {rational_sum}",
        f"10! = {fact_10}",
        f"C(10, 3) = {binom_10_3}",
        "",
        f"Σ(k=1 to n) k = {sum_symbolic}",
        f"Σ(k=1 to 100) k = {sum_numeric}",
    )
