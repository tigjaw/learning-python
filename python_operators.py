txt = """
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

print("\n", "Python Operators")
print("\n", txt)

print("see 'python_operators_list.py' for full list")

# Arithmetic operators
print("\n", "Arithmetic Operators")
print("\t", " 10 + 5 =", 10 + 5)
print("\t", " 10 * 5 =", 10 * 5)
print("\t", " 10 / 5 =", 10 / 5)

# Membership operators
print("\n", "Membership Operators")
print("\t", "fruits = ['apple', 'banana']")
print("\t", "if 'apple' in fruits:")
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("\t\t", "Yes, apple is a fruit!")
