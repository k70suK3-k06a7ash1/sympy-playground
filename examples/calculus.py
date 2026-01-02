"""Calculus examples: differentiation, integration, limits, series."""

from sympy import Symbol, sin, exp, pi, oo, diff, integrate, limit, series
from core.types import make_example


@make_example("3. 微分積分")
def calculus() -> tuple[str, ...]:
    """Demonstrate calculus operations."""
    x = Symbol("x")

    # 微分
    f = x**3 + 2 * x**2 + x
    f_prime = diff(f, x)
    f_double_prime = diff(f, x, 2)

    # 積分
    g = sin(x)
    indefinite = integrate(g, x)
    definite = integrate(g, (x, 0, pi))

    # 極限
    limit1 = limit(sin(x) / x, x, 0)
    limit2 = limit((1 + 1 / x) ** x, x, oo)

    # テイラー展開
    taylor = series(exp(x), x, 0, 6)

    return (
        f"f(x) = {f}",
        f"f'(x) = {f_prime}",
        f"f''(x) = {f_double_prime}",
        "",
        f"∫sin(x)dx = {indefinite}",
        f"∫₀^π sin(x)dx = {definite}",
        "",
        f"lim(x→0) sin(x)/x = {limit1}",
        f"lim(x→∞) (1 + 1/x)^x = {limit2}",
        "",
        f"exp(x) のテイラー展開: {taylor}",
    )
