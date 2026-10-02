"""Simple CLI calculator for +, -, *, /."""


def calculate(left: float, operator: str, right: float) -> float:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return left / right
    raise ValueError(f"Unknown operator: {operator}")


def main() -> None:
    print("CLI calculator. Operators: +  -  *  /")
    print("Type q or quit at any prompt to exit.\n")

    while True:
        first = input("First number: ").strip()
        if first.lower() in {"q", "quit"}:
            break

        operator = input("Operator (+, -, *, /): ").strip()
        if operator.lower() in {"q", "quit"}:
            break

        second = input("Second number: ").strip()
        if second.lower() in {"q", "quit"}:
            break

        try:
            left = float(first)
            right = float(second)
            result = calculate(left, operator, right)
        except ValueError as exc:
            if "could not convert" in str(exc).lower() or "invalid literal" in str(exc).lower():
                print("Please enter valid numbers.\n")
            else:
                print("Use only +, -, *, or /.\n")
            continue
        except ZeroDivisionError as exc:
            print(f"{exc}\n")
            continue

        print(f"Result: {result}\n")

        again = input("Another calculation? (y/n): ").strip().lower()
        if again in {"q", "quit", "n", "no"}:
            break
        print()

    print("Goodbye.")


if __name__ == "__main__":
    main()
