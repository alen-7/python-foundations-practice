"""Exercise 3: loops."""


def multiplication_table(number, up_to=10):
    """Print the multiplication table of a number using a for loop."""
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")


def total_expenses(expenses):
    """Add up a list of expenses using a for loop."""
    total = 0
    for amount in expenses:
        total += amount
    return total


def countdown(start):
    """Count down to zero using a while loop."""
    while start > 0:
        print(start)
        start -= 1
    print("Go!")


if __name__ == "__main__":
    multiplication_table(7)
    print("Total:", total_expenses([1500, 2300, 800, 450]))
    countdown(5)
