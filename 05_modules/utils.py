"""Helper functions used by main.py (this file is the 'module')."""

import math


def circle_area(radius):
    """Area of a circle using math.pi from the standard library."""
    return round(math.pi * radius**2, 2)


def days_until(year, month, day):
    """Number of days from today until the given date."""
    from datetime import date

    return (date(year, month, day) - date.today()).days
