"""Differential equations examples."""

from sympy import Symbol, Function, Eq, Derivative, dsolve
from core.types import make_example


@make_example("8. 微分方程式")
def differential_equations() -> tuple[str, ...]:
    """Demonstrate differential equation solving."""
    x = Symbol("x")
    f = Function("f")

    # 1階線形微分方程式: f'(x) = f(x)
    ode1 = Eq(Derivative(f(x), x), f(x))
    sol1 = dsolve(ode1, f(x))

    # 2階微分方程式: f''(x) + f(x) = 0 (調和振動子)
    ode2 = Eq(Derivative(f(x), x, 2) + f(x), 0)
    sol2 = dsolve(ode2, f(x))

    return (
        f"微分方程式: {ode1}",
        f"一般解: {sol1}",
        "",
        f"微分方程式: {ode2}",
        f"一般解: {sol2}",
    )
