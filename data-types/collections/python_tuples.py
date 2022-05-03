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

Tuple Methods:
Python has two built-in methods that you can use on tuples.

Method	    Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value
            and returns the position of where it was found

Tuples are written with (round brackets)
"""
print(txt)

# Creating a Tuple
print("\n", "Creating a Tuple:")
fruit_tuple = ("apple", "banana", "cherry")

print("\t", "> fruit_tuple", "\t\t\t=", "('apple', 'banana', 'cherry')")
    # Print Tuple and Tuple Length
print("\t\t", "print(fruit_tuple)", "\t=",fruit_tuple)
print("\t\t", "len(fruit_list)", "\t=", len(fruit_tuple))

# Data Types
print("\t","> Tuple items can be of any data type:")
    # Single Data Types
str_tuple = ("apple", "banana", "cherry")
int_tuple = (1, 5, 7, 9, 3)
bool_tuple = (True, False, False)
print("\t\t", "str_tuple", "\t\t=", "('apple', 'banana', 'cherry')")
print("\t\t", "int_tuple", "\t\t=", "(1, 5, 7, 9, 3)")
print("\t\t", "bool_tuple", "\t\t=", "(True, False, False)")
    # Mixed Data Types
print("\t", "> Tuples can contain multiple data types:")
mixed_tuple = ("abc", 34, True, 40, "male")
print("\t\t", "mixed_tuple", "\t\t=", "('abc', 34, True, 40, 'male')")
    # Tuple Object Type
print("\t", "> Find the type of a Tuple:")
print("\t\t", "type(int_tuple)", "\t=", type(int_tuple))

# Access Items
print("\n", "Accessing Tuple items:")
    # Access Single Items
print("\t", "> mixed_tuple", "\t\t\t=", mixed_tuple)
print("\t\t", "mixed_tuple[1]", "\t\t=", mixed_tuple[1])
print("\t\t", "mixed_tuple[-1]", "\t=", mixed_tuple[-1])
    # Access Range of Items
fruit_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("\t", "> fruit_tuple", "\t\t\t=", fruit_tuple)
print("\t\t", "fruit_tuple[2:5]", "\t=", fruit_tuple[2:5])
print("\t\t", "fruit_tuple[:4]", "\t=", fruit_tuple[:4])
print("\t\t", "fruit_tuple[2:]", "\t=", fruit_tuple[2:])
print("\t\t", "fruit_tuple[-4:-1]", "\t=", fruit_tuple[-4:-1])

# Check if item exists
print("\n", "Check if item exists in Tuple:")
print("\t", "if 'apple' in fruit_tuple:")
if "apple" in fruit_tuple:
    print("\t\t", "Yes, 'apple' is in fruit_tuple")

# Changing Tuple items
fruit_tuple = ("apple", "banana", "cherry")
print("\n", "Changing Tuple - convert the Tuple into a List and back into a Tuple:")
print("\t", "> fruit_tuple", "\t\t\t=", fruit_tuple)
print("\t\t", "fruit_list = list(fruit_tuple)")
print("\t\t", "fruit_list[1] = 'kiwi'")
print("\t\t", "modified_tuple = tuple(fruit_list)")
fruit_list = list(fruit_tuple)
fruit_list[1] = "kiwi"
modified_tuple = tuple(fruit_list)
print("\t\t\t", "modified_tuple", "=", modified_tuple)

# Append Tuple items
fruit_tuple = ("apple", "banana", "cherry")
print("\n", "Append items - convert the Tuple into a List and back into a Tuple:")
print("\t", "> fruit_tuple", "\t\t\t=", fruit_list)
print("\t\t", "fruit_list = list(fruit_tuple)")
print("\t\t", "fruit_list.append('orange')")
print("\t\t", "fruit_tuple = tuple(fruit_list)")
fruit_list = list(fruit_tuple)
fruit_list.append("orange")
fruit_tuple = tuple(fruit_list)
print("\t\t\t", "fruit_tuple", "\t=", fruit_tuple)

# Remove Tuple Items
fruit_tuple = ("apple", "banana", "cherry")
    # Remove Tuple Values
print("\n", "Remove items - convert the Tuple into a List and back into a Tuple:")
print("\t", "> fruit_tuple", "\t\t\t=", fruit_tuple)
print("\t\t", "fruit_list = list(fruit_tuple)")
print("\t\t", "fruit_list.remove('apple')")
print("\t\t", "fruit_tuple = tuple(fruit_list)")
fruit_list = list(fruit_tuple)
fruit_list.remove("apple")
fruit_tuple = tuple(fruit_list)
print("\t\t\t", "fruit_tuple", "\t=", fruit_tuple)
    # Delete Tuple
print("\n", "Delete Tuple")
print("\t", "del fruit_tuple")
print("\t\t", "result", "\t\t=", "no more list!")

# Unpacking a Tuple
print("\n", "Unpacking a Tuple")
    # Basic unpacking
fruit_tuple = ("Apple", "Peach", "Plum")
print("\t", "> Basic Unpacking")
print("\t", "fruit_tuple", "\t\t\t=", fruit_tuple)
(fruit1, fruit2, fruit3) = fruit_tuple
print("\t\t", "(fruit1, fruit2, fruit3) = fruit_tuple")
print("\t\t", "fruit_tuple unpacked:")
print("\t\t\t", "fruit1", "\t=", fruit1)
print("\t\t\t", "fruit2", "\t=", fruit2)
print("\t\t\t", "fruit3", "\t=", fruit3)
    # Using *Asterisk
fruit_tuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
print("\t", "> Unpacking with *Asterisk")
print("\t", "fruit_tuple", "\t\t\t=", fruit_tuple)
        # *fruit1
(*fruit1, fruit2, fruit3) = fruit_tuple
print("\t\t", "(*fruit1, fruit2, fruit3) = fruit_tuple")
print("\t\t", "fruit_tuple unpacked:")
print("\t\t\t", "fruit1", "\t=", fruit1)
print("\t\t\t", "fruit2", "\t=", fruit2)
print("\t\t\t", "fruit3", "\t=", fruit3)
        # *fruit2
(fruit1, *fruit2, fruit3) = fruit_tuple
print("\t\t", "(fruit1, *fruit2, fruit3) = fruit_tuple")
print("\t\t", "fruit_tuple unpacked:")
print("\t\t\t", "fruit1", "\t=", fruit1)
print("\t\t\t", "fruit2", "\t=", fruit2)
print("\t\t\t", "fruit3", "\t=", fruit3)
        # *fruit3
(fruit1, fruit2, *fruit3) = fruit_tuple
print("\t\t", "(fruit1, fruit2, *fruit3) = fruit_tuple")
print("\t\t", "fruit_tuple unpacked:")
print("\t\t\t", "fruit1", "\t=", fruit1)
print("\t\t\t", "fruit2", "\t=", fruit2)
print("\t\t\t", "fruit3", "\t=", fruit3)

# Loop Through Tuples
print("\n", "Loop through Tuple items")
fruit_tuple = ("Apple", "Peach", "Plum")
print("\t", "fruit_tuple", "\t\t\t=", fruit_tuple)
    # for i in tuple
print("\t", "> for i in tuple")
print("\t\t", "for i in fruit_tuple:")
print("\t\t\t", "print(i)")
for i in fruit_tuple:
  print("\t\t\t\t", i)
    # for i in range(j)
print("\t", "> for i in range(j)")
print("\t\t", "for i in range(len(fruit_tuple)):")
print("\t\t\t", "print(fruit_tuple[i])")
for i in range(len(fruit_tuple)):
  print("\t\t\t\t", fruit_tuple[i])
    # while i < j
print("\t", "> while i < j")
print("\t\t", "while i < len(fruit_tuple):")
print("\t\t\t", "print(fruit_tuple[i])")
print("\t\t\t", "i = i + 1")
i = 0
while i < len(fruit_tuple):
  print("\t\t\t\t", fruit_tuple[i])
  i = i + 1

# Join Tuples
print("\n", "Join Tuples")
str_tuple = ("a", "b", "c")
int_tuple = (1, 2, 3)
print("\t", "str_tuple", "\t\t\t=", str_tuple)
print("\t", "int_tuple", "\t\t\t=", int_tuple)
    # add
print("\t", "> join with + (add)")
result = str_tuple + int_tuple
print("\t\t", "result = str_tuple + int_tuple")
print("\t\t\t", "result", "\t=", result)
    # multiply
print("\t", "> join with * (multiply)")
result = str_tuple * 2
print("\t\t", "result = str_tuple * 2")
print("\t\t\t", "result", "\t=", result)
