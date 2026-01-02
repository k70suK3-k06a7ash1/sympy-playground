"""SymPy example modules."""

from examples.basic import basic_symbols
from examples.simplification import simplification
from examples.calculus import calculus
from examples.equations import equations
from examples.matrices import matrices
from examples.special import special_functions
from examples.latex_output import latex_output
from examples.differential_equations import differential_equations

ALL_EXAMPLES = (
    basic_symbols,
    simplification,
    calculus,
    equations,
    matrices,
    special_functions,
    latex_output,
    differential_equations,
)

__all__ = ["ALL_EXAMPLES"]
