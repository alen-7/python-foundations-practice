"""Exercise 4: functions."""


def calculate_average(scores):
    """Return the average of a list of scores. Raises ValueError if empty."""
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(scores)


def is_passing(score, pass_mark=40):
    """Return True if the score meets the pass mark."""
    return score >= pass_mark


def format_name(first, last):
    """Return a neatly formatted full name, e.g. 'Ude, Chinecherem'."""
    return f"{last.strip().title()}, {first.strip().title()}"


if __name__ == "__main__":
    print(calculate_average([60, 70, 80]))
    print(is_passing(45))
    print(format_name("  chinecherem", "UDE "))
