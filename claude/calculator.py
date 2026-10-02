"""A basic command-line calculator supporting + - * / ** sq() and parentheses."""

import ast
import operator

BINARY_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}

UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def evaluate(expression):
    """Safely evaluate an arithmetic expression and return the result."""
    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body)


def _eval_node(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPS:
        return BINARY_OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
        return UNARY_OPS[type(node.op)](_eval_node(node.operand))
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sq"
        and len(node.args) == 1
        and not node.keywords
    ):
        value = _eval_node(node.args[0])
        return value * value
    raise ValueError("unsupported expression")


def main():
    print("Basic calculator. Type 'quit' or 'exit' to stop.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.lower() in ("quit", "exit"):
            break
        if not line:
            continue
        try:
            print(evaluate(line))
        except ZeroDivisionError:
            print("Error: division by zero")
        except (SyntaxError, ValueError):
            print("Error: invalid expression")


if __name__ == "__main__":
    main()
