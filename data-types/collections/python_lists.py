txt = """
Python Lists!!!

    see: https://www.w3schools.com/python/python_lists.asp

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is:
    - ordered
    - changeable
    - allows duplicates

Tuple items are indexed:
    - the first item has index [0]
    - the second item has index [1] etc...

Lists are created using [square brackets]

Method	        Description
 append()	Adds an element at the end of the list
 clear()	Removes all the elements from the list
 copy()	        Returns a copy of the list
 count()	Returns the number of elements with the specified value
 extend()	Add the elements of a list (or any iterable), to the end of the current list
 index()	Returns the index of the first element with the specified value
 insert()	Adds an element at the specified position
 pop()	        Removes the element at the specified position
 remove()	Removes the item with the specified value
 reverse()	Reverses the order of the list
 sort()	        Sorts the list
"""
print(txt)

# Creating a List
print("\n", "Creating a list:")
fruit_list = ["apple", "banana", "cherry"]

print("\t", "> fruit_list", "\t\t\t=", "['apple', 'banana', 'cherry']")
    # Print List and List Length
print("\t\t", "print(fruit_list)", "\t=",fruit_list)
print("\t\t", "len(fruit_list)", "\t=", len(fruit_list))

# Data Types
print("\t","> List items can be of any data type:")
    # Single Data Types
str_list = ["apple", "banana", "cherry"]
int_list = [1, 5, 7, 9, 3]
bool_list = [True, False, False]
print("\t\t", "str_list", "\t\t=", "['apple', 'banana', 'cherry']")
print("\t\t", "int_list", "\t\t=", "[1, 5, 7, 9, 3]")
print("\t\t", "bool_list", "\t\t=", "[True, False, False]")
    # Mixed Data Types
print("\t", "> Lists can contain multiple data types:")
mixed_list = ["abc", 34, True, 40, "male"]
print("\t\t", "mixed_list", "\t\t=", "['abc', 34, True, 40, 'male']")
    # List Object Type
print("\t", "> Find the type of a list:")
print("\t\t", "type(int_list)", "\t=", type(int_list))

# Access Items
print("\n", "Accessing list items:")
    # Access Single Items
print("\t", "> mixed_list", "\t\t\t=", mixed_list)
print("\t\t", "mixed_list[1]", "\t\t=", mixed_list[1])
print("\t\t", "mixed_list[-1]", "\t=", mixed_list[-1])
    # Access Range of Items
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\t", "> fruit_list", "\t\t\t=", fruit_list)
print("\t\t", "fruit_list[2:5]", "\t=", fruit_list[2:5])
print("\t\t", "fruit_list[:4]", "\t=", fruit_list[:4])
print("\t\t", "fruit_list[2:]", "\t=", fruit_list[2:])
print("\t\t", "fruit_list[-4:-1]", "\t=", fruit_list[-4:-1])

# Check if item exists
print("\n", "Check if item exists in list:")
print("\t", "if 'apple' in fruit_list:")
if "apple" in fruit_list:
    print("\t\t", "Yes, 'apple' is in fruit_list")

# Unpacking a list
fruit_list = ["Apple", "Peach", "Plum"]
print("\n", "Unpacking a List")
print("\t", "> fruit_list", "\t\t\t=", fruit_list)
fruit1, fruit2, fruit3 = fruit_list
print("\t\t", "fruit1, fruit2, fruit3 = fruit_list")
print("\t\t", "fruit_list unpacked:")
print("\t\t\t", "fruit1", "\t=", fruit1)
print("\t\t\t", "fruit2", "\t=", fruit2)
print("\t\t\t", "fruit3", "\t=", fruit3)

# Changing list items
fruit_list = ["apple", "banana", "cherry"]
print("\n", "Changing list items:")
print("\t", "> fruit_list", "\t\t\t=", fruit_list)
    # Change Single Item
print("\t", "> Replace a single item")
fruit_list[1] = "blackberry"
print("\t\t", "fruit_list[1]", "\t\t=", "'blackberry'")
print("\t\t", "result", "\t\t=", fruit_list)
    # Change a range of list items
print("\t", "> Replace a range of items")
fruit_list[1:3] = ["apricot", "watermelon"]
print("\t\t", "fruit_list[1:3]", "\t=", "['apricot', 'watermelon']")
print("\t\t", "result", "\t\t=", fruit_list)
    # Replace Single Item with Multiple
print("\t", "> Replace a single item with multiple")
fruit_list[1:2] = ["pear", "tomato"]
print("\t\t", "fruit_list[1:2]", "\t=", "['pear', 'tomato']")
print("\t\t", "result", "\t\t=", fruit_list)

# Inserting items
fruit_list = ["apple", "banana", "cherry"]
print("\n", "Inserting list items at a specific index:")
print("\t", "> fruit_list", "\t\t\t=", fruit_list)

fruit_list.insert(2, "pineapple")
print("\t\t", "fruit_list.insert(2, 'pineapple')")
print("\t\t", "result", "\t\t=", fruit_list)

# Append items
fruit_list = ["apple", "banana", "cherry"]
print("\n", "Appending list items (to the end of the list):")
print("\t", "> fruit_list", "\t\t\t=", fruit_list)

print("\t\t", "fruit_list.append('orange')")
fruit_list.append("orange")
print("\t\t", "result", "\t\t=", fruit_list)

# Extend List
fruit_list = ["apple", "banana", "cherry"]
more_fruit = ["mango", "pineapple", "papaya"]
print("\n", "Extending a list")
print("\t", "> with any collection type")
print("\t\t", "fruit_list", "\t\t=", fruit_list)
print("\t\t", "more_fruit", "\t\t=", more_fruit)
fruit_list.extend(more_fruit)
print("\t\t\t", "fruit_list.extend(more_fruit)")
print("\t\t\t", "result", "\t=", fruit_list)

# Remove List Items
print("\n", "Remove list items")
    # list.remove(i) - remove specified value
print("\t", "> Remove specified value", "\t=", "list.remove(i)")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
fruit_list.remove("banana")
print("\t\t\t", "fruit_list.remove('banana')")
print("\t\t\t", "result", "\t=", fruit_list)
    # list.pop(i) - remove specified index
print("\t", "> Remove specified index", "\t=", "list.pop(i)")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
fruit_list.pop(1)
print("\t\t\t", "fruit_list.pop(1)")
print("\t\t\t", "result", "\t=", fruit_list)
    # list.pop() - remove last index
print("\t", "> Remove last index", "\t\t=", "list.pop()")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
fruit_list.pop()
print("\t\t\t", "fruit_list.pop()")
print("\t\t\t", "result", "\t=", fruit_list)
    # del list[i] - remove specified index
print("\t", "> Remove specified index", "\t=", "del list[i]")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
del fruit_list[0]
print("\t\t\t", "del fruit_list[0]")
print("\t\t\t", "result", "\t=", fruit_list)
    # del list - delete list
print("\t", "> Delete list", "\t\t\t=", "del list")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
print("\t\t\t", "del fruit_list")
print("\t\t\t", "result", "\t=", "no more list!")
    # list.clear() - clear list
print("\t", "> Clear list", "\t\t\t=", "list.clear()")
fruit_list = ["apple", "banana", "cherry"]
print("\t\t", "fruit_list", "\t\t=", fruit_list)
fruit_list.clear()
print("\t\t\t", "fruit_list.clear()")
print("\t\t\t", "result", "\t=", fruit_list)

# Loop Through Lists
print("\n", "Loop through list items")
fruit_list = ["apple", "banana", "cherry"]
print("\t", "fruit_list", "\t\t\t=", fruit_list)
    # for i in list
print("\t", "> for i in list")
print("\t\t", "for i in fruit_list:")
print("\t\t\t", "print(i)")
for i in fruit_list:
  print("\t\t\t\t", i)
    # for x in range(i)
print("\t", "> for i in range(i)")
print("\t\t", "for i in range(len(fruit_list)):")
print("\t\t\t", "print(fruit_list[i])")
for i in range(len(fruit_list)):
  print("\t\t\t\t", fruit_list[i])
    # while i < j:
print("\t", "> while i < j")
print("\t\t", "while i < len(fruit_list):")
print("\t\t\t", "print(fruit_list[i])")
print("\t\t\t", "i = i + 1")
i = 0
while i < len(fruit_list):
  print("\t\t\t\t", fruit_list[i])
  i = i + 1

# List Comprehension
print("\n", "List Comprehension")
fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]
print("\t", "fruit_list", "\t\t\t=", fruit_list)
print() # Iterate and include all fruit
print("\t", "> Iterate and include all fruit")
new_list = [x for x in fruit_list]
print("\t\t", "new_list", "\t\t=" ,"[x for x in fruit_list]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Iterate and include only fruit that contain the letter 'a'
print("\t", "> Iterate and include only fruit that contain the letter 'a'")
new_list = [x for x in fruit_list if "a" in x]
print("\t\t", "new_list", "\t\t=" ,"[x for x in fruit_list if 'a' in x]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Iterate and include all fruit that aren't 'apple'
print("\t", "> Iterate and include all fruit that aren't 'apple'")
new_list = [x for x in fruit_list if x != "apple"]
print("\t\t", "newlist", "\t\t=" ,"[x for x in fruit_list if x != 'apple']")
print("\t\t", "new_list", "\t\t=", new_list)
print() # The iterable can be any iterable object, like a list, tuple, set etc
print("\t", "> The iterable can be any iterable object (e.g. in range(10))")
new_list = [x for x in range(10)]
print("\t\t", "new_list", "\t\t=" ,"[x for x in range(10)]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Iterable with a condition - e.g. if x < 5
print("\t", "> Iterable with a condition - e.g. if x < 5")
new_list = [x for x in range(10) if x < 5]
print("\t\t", "new_list", "\t\t=" ,"[x for x in range(10) if x < 5]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Manipulate the expression - e.g. convert to upper case
print("\t", "> Manipulate the expression - e.g. convert to upper case")
new_list = [x.upper() for x in fruit_list]
print("\t\t", "new_list", "\t\t=" ,"[x.upper() for x in fruit_list]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Set the outcome to whatever you like - e.g. set all values to 'hello'
print("\t", "> Set the outcome to whatever you like - e.g. set all values to 'hello'")
new_list = ['hello' for x in fruit_list]
print("\t\t", "new_list", "\t\t=" ,"['hello' for x in fruit_list]")
print("\t\t", "new_list", "\t\t=", new_list)
print() # Apply conditions to the expression - return 'orange' instead of 'banana'
print("\t", "> Apply conditions to the expression - return 'orange' instead of 'banana'")
new_list = [x if x != "banana" else "orange" for x in fruit_list]
print("\t\t", "new_list", "\t\t=" ,"[x if x != 'banana' else 'orange' for x in fruit_list]")
print("\t\t", "new_list", "\t\t=", new_list)

# Sort Lists
print("\n", "Sort Lists")
str_list = ["delta", "alpha", "echo", "charlie", "bravo"]
int_list = [100, 50, 65, 82, 23]
print() # Sort Strings (Ascending)
print("\t", "> Sort Strings (Ascending)")
print("\t", "str_list", "\t\t\t=", str_list)
str_list.sort()
print("\t\t", "str_list.sort()")
print("\t\t", "str_list", "\t\t=", str_list)
print() # Sort Numberts (Ascending)
print("\t", "> Sort Numberts (Ascending)")
print("\t", "int_list", "\t\t\t=", int_list)
int_list.sort()
print("\t\t", "int_list.sort()")
print("\t\t", "int_list", "\t\t=", int_list)
print () # Sort Descending
print("\t", "> Sort Numberts (Descending)")
int_list.sort(reverse = True)
print("\t\t", "int_list.sort(reverse = True)")
print("\t\t", "int_list", "\t\t=", int_list)
str_list.sort(reverse = True)
print("\t\t", "str_list.sort(reverse = True)")
print("\t\t", "str_list", "\t\t=", str_list)
print() # Sort Case-Insensitive
print("\t", "> Sort Case-Insensitive")
str_list.sort(key = str.lower)
print("\t\t", "str_list.sort(key = str.lower)")
print("\t\t", "str_list", "\t\t=", str_list)
print() # Custom Sort Function
print("\t", "> Custom Sort Function - e.g. sort the list based on how close the number is to 50")
print("\t\t", "def my_sort(n):")
print("\t\t\t", "return abs(n - 50)")
print("\t\t", "int_list.sort(key = my_sort)")
def my_sort(n):
  return abs(n - 50)
int_list.sort(key = my_sort)
print("\t\t\t", "result", "\t=", int_list)

# Copy Lists
print("\n", "Copy Lists")
print() # with copy() method
print("\t", "Make a copy of a list with the copy() method")
copy_list = str_list.copy()
print("\t\t", "copy_list = str_list.copy()")
print("\t\t", "copy_list", "\t\t=", copy_list)
print() # with list() method
print("\t", "Make a copy of a list with the list() method")
copy_list = list(str_list)
print("\t\t", "copy_list = list(str_list)")
print("\t\t", "copy_list", "\t\t=", copy_list)


