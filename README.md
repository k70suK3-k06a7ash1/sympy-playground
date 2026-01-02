# SymPy Playground

SymPy の使用例集。`returns` ライブラリを使った Monadic Pattern で実装。

## セットアップ

```bash
uv sync
```

## 実行

```bash
# 全例を実行
uv run python main.py

# テスト実行
uv run pytest -v
```

## プロジェクト構造

```
sympy-playground/
├── main.py                       # エントリーポイント
├── core/                         # コアモジュール
│   ├── types.py                  # Result/IO モナドパターン
│   └── printer.py                # IO出力
├── examples/                     # セマンティック境界で分割
│   ├── basic.py                  # シンボル基本操作
│   ├── simplification.py         # 式の簡略化
│   ├── calculus.py               # 微分積分
│   ├── equations.py              # 方程式
│   ├── matrices.py               # 行列演算
│   ├── special.py                # 特殊関数・定数
│   ├── latex_output.py           # LaTeX出力
│   └── differential_equations.py # 微分方程式
└── tests/
    ├── test_types.py             # コア型テスト
    └── test_examples.py          # 例のテスト
```

## 新しい例を追加

```python
# examples/my_example.py
from sympy import symbols, solve
from core.types import make_example

@make_example("9. 新しい例")
def my_example() -> tuple[str, ...]:
    """例外は自動的に Failure にラップされる"""
    x = symbols("x")
    result = solve(x**2 - 4, x)
    return (
        f"方程式: x² - 4 = 0",
        f"解: {result}",
    )
```

```python
# examples/__init__.py に追加
from examples.my_example import my_example

ALL_EXAMPLES = (
    # ...既存の例...
    my_example,
)
```

## Monadic Pattern

| パターン | 用途 |
|---------|------|
| `Result[T, E]` | 成功/失敗を表現 |
| `Success` / `Failure` | パターンマッチで分岐 |
| `make_example` | 例外を自動的に `Failure` にラップ |
| `ExampleRunner.run_sequence` | fail-fast (最初のエラーで停止) |
| `ExampleRunner.run_all` | 全結果を収集 |
| `IO[T]` | 副作用の遅延実行 |

### 使用例

```python
from returns.result import Success, Failure
from core.types import ExampleRunner
from examples import ALL_EXAMPLES

runner = ExampleRunner(ALL_EXAMPLES)

# 1. fail-fast: 最初のエラーで停止
match runner.run_sequence():
    case Success(results):
        for r in results:
            print(r.title)
    case Failure(err):
        print(f"Error: {err}")

# 2. 全収集: エラーがあっても全て実行
for result in runner.run_all():
    match result:
        case Success(r):
            print(f"✓ {r.title}")
        case Failure(e):
            print(f"✗ {e}")

# 3. 個別の例を実行
from examples.calculus import calculus

match calculus.execute():
    case Success(result):
        for line in result.to_lines():
            print(line)
```

## SymPy 例の内容

| # | カテゴリ | 内容 |
|---|---------|------|
| 1 | 基本操作 | シンボル定義、式の作成、値代入、因数分解 |
| 2 | 簡略化 | simplify, expand, factor, trigsimp |
| 3 | 微分積分 | 微分、積分、定積分、極限、テイラー展開 |
| 4 | 方程式 | 代数方程式、連立方程式、三角方程式 |
| 5 | 行列 | 行列式、逆行列、固有値・固有ベクトル |
| 6 | 特殊関数 | π, e, i, オイラーの等式、階乗、総和 |
| 7 | LaTeX出力 | 数式をLaTeX形式で出力 |
| 8 | 微分方程式 | 1階・2階常微分方程式の解法 |
