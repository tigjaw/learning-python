txt = """
PYTHON LISTS (List):

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
"""
print(txt)

print("\n", "Creating a List:")
fruit_list = ["apple", "banana", "cherry"]
print("\t", "fruit_list = ['apple', 'banana', 'cherry']")
print("\t\t", "print(fruit_list)", "\t=",fruit_list)
print("\t\t", "len(fruit_list)", "\t=", len(fruit_list))

# Data Types
print("\t","List items can be of any data type:")
string_list = ["apple", "banana", "cherry"]
int_list = [1, 5, 7, 9, 3]
bool_list = [True, False, False]
print("\t\t", "string_list", "\t\t=", "['apple', 'banana', 'cherry']")
print("\t\t", "int_list", "\t\t=", "[1, 5, 7, 9, 3]")
print("\t\t", "bool_list", "\t\t=", "[True, False, False]")
print("\t", "A list can contain different data types:")
mixed_list = ["abc", 34, True, 40, "male"]
print("\t\t", "mixed_list", "\t\t=", "['abc', 34, True, 40, 'male']")
print("\t", "Find the type of a list:")
print("\t\t", "type(int_list)", "\t=", type(int_list))

# Access Items
print("\n", "Accessing List Items:")
print("\t", "mixed_list", "\t\t=", mixed_list)
print("\t\t", "mixed_list[1]", "\t\t=", mixed_list[1])
print("\t\t", "mixed_list[-1]", "\t=", mixed_list[-1])
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\t", "fruit_list", "\t\t=", fruit_list)
print("\t", "fruit_list[2:5]", "\t=", fruit_list[2:5])
print("\t", "fruit_list[:4]", "\t=", fruit_list[:4])
print("\t", "fruit_list[2:]", "\t=", fruit_list[2:])
print("\t", "fruit_list[-4:-1]", "\t=", fruit_list[-4:-1])

# Check if item exists
print("\n", "Check if item exists in list")
print("\t", "if 'apple' in thislist:")
if "apple" in fruit_list:
    print("\t\t", "Yes, 'apple' is in the fruits list")
