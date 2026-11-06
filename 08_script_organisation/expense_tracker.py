"""Exercise 8: script organisation. A tiny expense tracker.

Structure: small helper functions, one main() that ties them together,
and the `if __name__ == "__main__":` guard at the bottom.
"""


def add_expense(expenses, name, amount):
    """Add an expense (a dictionary) to the list."""
    expenses.append({"name": name, "amount": amount})


def total(expenses):
    """Return the total of all expenses."""
    return sum(item["amount"] for item in expenses)


def show(expenses):
    """Print every expense and the total."""
    for item in expenses:
        print(f"- {item['name']}: N{item['amount']:,}")
    print(f"Total: N{total(expenses):,}")


def main():
    expenses = []
    add_expense(expenses, "Transport", 1500)
    add_expense(expenses, "Data subscription", 5000)
    add_expense(expenses, "Lunch", 2500)
    show(expenses)


if __name__ == "__main__":
    main()
