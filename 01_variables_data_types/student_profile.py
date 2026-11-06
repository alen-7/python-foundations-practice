"""Exercise 1: variables and data types."""

name = "Chinecherem Ude"  # str
age = 24  # int
cgpa = 4.5  # float
is_corper = True  # bool
skills = ["Python", "Git"]  # list
address = {"city": "Abuja", "country": "Nigeria"}  # dict

print("Student profile")
print("---------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Currently serving NYSC: {is_corper}")
print(f"Skills: {', '.join(skills)}")
print(f"Location: {address['city']}, {address['country']}")

# type() shows the data type of each variable
for label, value in [
    ("name", name),
    ("age", age),
    ("cgpa", cgpa),
    ("is_corper", is_corper),
    ("skills", skills),
    ("address", address),
]:
    print(f"{label} is a {type(value).__name__}")
