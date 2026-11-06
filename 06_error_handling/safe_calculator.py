"""Exercise 6: error handling. A calculator that does not crash."""


def divide(a, b):
    """Divide a by b, returning a message instead of crashing."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: you cannot divide by zero"


def to_number(text):
    """Convert text to a float, or return None if it is not a number."""
    try:
        return float(text)
    except ValueError:
        return None


if __name__ == "__main__":
    first = to_number(input("First number: "))
    second = to_number(input("Second number: "))
    if first is None or second is None:
        print("Error: please enter valid numbers")
    else:
        print("Result:", divide(first, second))
