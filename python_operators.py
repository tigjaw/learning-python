txt = """
Python Operators!!!

    see: https://www.w3schools.com/python/python_operators.asp
    see: python_operators_list.py for full list

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

print(txt)

# Arithmetic operators
print("", "Arithmetic Operators")
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
