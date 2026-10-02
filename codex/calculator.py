"""A simple command-line calculator."""


def calculate(first: float, operator: str, second: float) -> float:
    """Perform one calculation using the selected operator."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second
    if operator == "square":
        return first**2
    raise ValueError("Invalid operator.")


def main() -> None:
    """Run the interactive calculator loop."""
    print("Simple Calculator")
    print("Enter q at any prompt to quit.")

    while True:
        first_input = input("First number: ").strip()
        if first_input.lower() == "q":
            break

        try:
            first = float(first_input)
        except ValueError:
            print("Error: please enter a valid number.")
            continue

        operator = input("Operation (+, -, *, /, square): ").strip().lower()
        if operator.lower() == "q":
            break
        if operator not in {"+", "-", "*", "/", "square"}:
            print("Error: please choose +, -, *, /, or square.")
            continue

        if operator == "square":
            print(f"Result: {calculate(first, operator, 0):g}")
            continue

        second_input = input("Second number: ").strip()
        if second_input.lower() == "q":
            break

        try:
            second = float(second_input)
        except ValueError:
            print("Error: please enter a valid number.")
            continue

        try:
            result = calculate(first, operator, second)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
