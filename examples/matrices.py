"""Matrix operations examples."""

from sympy import Symbol, Matrix, det
from core.types import make_example


@make_example("5. 行列演算")
def matrices() -> tuple[str, ...]:
    """Demonstrate matrix operations."""
    # 行列の作成
    A = Matrix([[1, 2], [3, 4]])

    # 逆行列
    A_inv = A.inv()

    # 固有値と固有ベクトル
    eigenvalues = A.eigenvals()
    eigenvects = A.eigenvects()

    # シンボリック行列
    x = Symbol("x")
    B = Matrix([[x, 1], [1, x]])
    det_B = det(B)

    return (
        f"行列 A:\n{A}",
        "",
        f"行列式 det(A) = {det(A)}",
        "",
        f"逆行列 A⁻¹:\n{A_inv}",
        "",
        f"固有値: {eigenvalues}",
        f"固有ベクトル: {eigenvects}",
        "",
        f"シンボリック行列 B の行列式: {det_B}",
    )
