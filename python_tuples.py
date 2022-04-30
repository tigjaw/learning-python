txt = """
Python Tuples!!!

    see: https://www.w3schools.com/python/python_tuples.asp

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is:
    - ordered
    - unchangeable
    - allows duplicates

Tuple items are indexed:
    - the first item has index [0]
    - the second item has index [1] etc...

Tuples are written with round brackets.
"""
print(txt)

fruit_tuple = ("apple", "banana", "cherry")
txt = "fruit_list = ('apple', 'banana', 'cherry')"
print("", "Create a tuple:")
print("\t", txt)
print("", "Print a tuple:")
print("\t", fruit_tuple)

print()
print("", "Tuple can contain:")
print("", "- duplicate values")
print("", "- any data type")
print("", "- mixed data types in one tuple")

string_tuple = ("apple", "banana", "cherry")
int_tuple = (1, 5, 7, 9, 3)
boolean_tuple = (True, False, False)
mixed_tuple = ("abc", 34, True, 40, "male")
print("\t", "string_tuple", "\t=", string_tuple)
print("\t", "int_tuple", "\t=", int_tuple)
print("\t", "boolean_tuple", "\t=", boolean_tuple)
print("\t", "mixed_tuple", "\t=", mixed_tuple)

print("\n", "Tuples are defined as objects with the data type 'tuple':")
print("\t", type(mixed_tuple))

# creating and unpacking a tuple
print("\n", "Unpacking a Tuple:")
fruit_tuple = ("Grapes", "Strawberry", "Pineapple")
print("\t", "fruit_tuple = ('Grapes', 'Strawberry', 'Pineapple')")
print("\t", "fruit1, fruit2, fruit3 = fruit_tuple")
fruit1, fruit2, fruit3 = fruit_tuple
print("\t\t", "fruit1 = ", fruit1)
print("\t\t", "fruit2 = ", fruit2)
print("\t\t", "fruit3 = ", fruit3)
