"""Exercise 5: modules. Importing our own module and the standard library."""

import random
from utils import circle_area, days_until

print("Area of a circle with radius 5:", circle_area(5))
print("Days until 1 January 2027:", days_until(2027, 1, 1))
print("A random number from 1 to 10:", random.randint(1, 10))
