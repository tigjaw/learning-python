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

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Creating a List
print(n, "Creating a list:")

fruit_list = ["apple", "banana", "cherry"]
print(t1, "> fruit_list", "\t\t\t=", "['apple', 'banana', 'cherry']")

    # Print List and List Length
print(t2, "print(fruit_list)", "\t=",fruit_list)
print(t2, "len(fruit_list)", "\t=", len(fruit_list))

# Data Types
print(t1,"> List items can be of any data type:")

    # Single Data Types
str_list = ["apple", "banana", "cherry"]
int_list = [1, 5, 7, 9, 3]
bool_list = [True, False, False]

print(t2, "str_list", "\t\t=", "['apple', 'banana', 'cherry']")
print(t2, "int_list", "\t\t=", "[1, 5, 7, 9, 3]")
print(t2, "bool_list", "\t\t=", "[True, False, False]")

    # Mixed Data Types
print(t1, "> Lists can contain multiple data types:")

mixed_list = ["abc", 34, True, 40, "male"]

print(t2, "mixed_list", "\t\t=", "['abc', 34, True, 40, 'male']")

    # List Object Type
print(t1, "> Find the type of a list:")

print(t2, "type(int_list)", "\t=", type(int_list))

# Access Items
print(n, "Accessing list items:")

fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(t1, "fruit_list", "\t\t\t=", fruit_list, n)

    # Access Single Items
print(t1, "> Access Single Items:", fruit_list)

print(t2, "fruit_list[1]", "\t\t=", fruit_list[1])
print(t2, "fruit_list[-1]", "\t=", fruit_list[-1])

    # Access Range of Items
print(t1, "> Access Range of Items:", fruit_list)

print(t2, "fruit_list[2:5]", "\t=", fruit_list[2:5])
print(t2, "fruit_list[:4]", "\t=", fruit_list[:4])
print(t2, "fruit_list[2:]", "\t=", fruit_list[2:])
print(t2, "fruit_list[-4:-1]", "\t=", fruit_list[-4:-1])

# Check if item exists
print(n, "Check if item exists in list:")

print(t1, "if 'apple' in fruit_list:")

if "apple" in fruit_list:
    print(t2, "Yes, 'apple' is in fruit_list")

# Unpacking a list
print(n, "Unpacking a List")

fruit_list = ["Apple", "Peach", "Plum"]

print(t1, "> fruit_list", "\t\t\t=", fruit_list)

fruit1, fruit2, fruit3 = fruit_list

print(t2, "fruit1, fruit2, fruit3 = fruit_list")
print(t2, "fruit_list unpacked:")
print(t3, "fruit1", "\t=", fruit1)
print(t3, "fruit2", "\t=", fruit2)
print(t3, "fruit3", "\t=", fruit3)

# Changing list items
print(n, "Changing list items:")

fruit_list = ["apple", "banana", "cherry"]

print(t1, "> fruit_list", "\t\t\t=", fruit_list)

    # Change Single Item
print(t1, "> Replace a single item")

fruit_list[1] = "blackberry"

print(t2, "fruit_list[1]", "\t\t=", "'blackberry'")
print(t2, "result", "\t\t=", fruit_list)

    # Change a range of list items
print(t1, "> Replace a range of items")

fruit_list[1:3] = ["apricot", "watermelon"]

print(t2, "fruit_list[1:3]", "\t=", "['apricot', 'watermelon']")
print(t2, "result", "\t\t=", fruit_list)

    # Replace Single Item with Multiple
print(t1, "> Replace a single item with multiple")

fruit_list[1:2] = ["pear", "tomato"]

print(t2, "fruit_list[1:2]", "\t=", "['pear', 'tomato']")
print(t2, "result", "\t\t=", fruit_list)

# Inserting items
print(n, "Inserting list items at a specific index:")

fruit_list = ["apple", "banana", "cherry"]

print(t1, "> fruit_list", "\t\t\t=", fruit_list)

fruit_list.insert(2, "pineapple")

print(t2, "fruit_list.insert(2, 'pineapple')")
print(t2, "result", "\t\t=", fruit_list)

# Append items
print(n, "Appending list items (to the end of the list):")

fruit_list = ["apple", "banana", "cherry"]

print(t1, "> fruit_list", "\t\t\t=", fruit_list)
print(t2, "fruit_list.append('orange')")

fruit_list.append("orange")

print(t2, "result", "\t\t=", fruit_list)

# Extend List
print(n, "Extending a list")

fruit_list = ["apple", "banana", "cherry"]
more_fruit = ["mango", "pineapple", "papaya"]

print(t1, "> with any collection type")
print(t2, "fruit_list", "\t\t=", fruit_list)
print(t2, "more_fruit", "\t\t=", more_fruit)

fruit_list.extend(more_fruit)

print(t3, "fruit_list.extend(more_fruit)")
print(t3, "result", "\t=", fruit_list)

# Remove List Items
print(n, "Remove list items")

    # list.remove(i) - remove specified value
print(t1, "> Remove specified value", "\t=", "list.remove(i)")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)

fruit_list.remove("banana")

print(t3, "fruit_list.remove('banana')")
print(t3, "result", "\t=", fruit_list)

    # list.pop(i) - remove specified index
print(t1, "> Remove specified index", "\t=", "list.pop(i)")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)

fruit_list.pop(1)

print(t3, "fruit_list.pop(1)")
print(t3, "result", "\t=", fruit_list)

    # list.pop() - remove last index
print(t1, "> Remove last index", "\t\t=", "list.pop()")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)

fruit_list.pop()

print(t3, "fruit_list.pop()")
print(t3, "result", "\t=", fruit_list)

    # del list[i] - remove specified index
print(t1, "> Remove specified index", "\t=", "del list[i]")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)

del fruit_list[0]

print(t3, "del fruit_list[0]")
print(t3, "result", "\t=", fruit_list)

    # del list - delete list
print(t1, "> Delete list", "\t\t\t=", "del list")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)
print(t3, "del fruit_list")
print(t3, "result", "\t=", "no more list!")

    # list.clear() - clear list
print(t1, "> Clear list", "\t\t\t=", "list.clear()")

fruit_list = ["apple", "banana", "cherry"]

print(t2, "fruit_list", "\t\t=", fruit_list)

fruit_list.clear()

print(t3, "fruit_list.clear()")
print(t3, "result", "\t=", fruit_list)

# Loop Through Lists
print(n, "Loop through list items")

fruit_list = ["apple", "banana", "cherry"]

print(t1, "fruit_list", "\t\t\t=", fruit_list)

    # for i in list
print(n, t1, "> for i in list")

print(t2, "for i in fruit_list:")
print(t3, "print(i)")

for i in fruit_list:
  print(t4, i)

    # for x in range(i)
print(n, t1, "> for i in range(i)")

print(t2, "for i in range(len(fruit_list)):")
print(t3, "print(fruit_list[i])")

for i in range(len(fruit_list)):
  print(t4, fruit_list[i])
  
    # while i < j:
print(n, t1, "> while i < j")

print(t2, "while i < len(fruit_list):")
print(t3, "print(fruit_list[i])")
print(t3, "i = i + 1")

i = 0
while i < len(fruit_list):
  print(t4, fruit_list[i])
  i = i + 1

# List Comprehension
print(n, "List Comprehension")

fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]

print(t1, "fruit_list", "\t\t\t=", fruit_list)

    # Iterate and include all fruit
print(n, t1, "> Iterate and include all fruit")

new_list = [x for x in fruit_list]

print(t2, "new_list", "\t\t=" ,"[x for x in fruit_list]")
print(t2, "new_list", "\t\t=", new_list)

    # Iterate and include only fruit that contain the letter 'a'
print(n, t1, "> Iterate and include only fruit that contain the letter 'a'")

new_list = [x for x in fruit_list if "a" in x]

print(t2, "new_list", "\t\t=" ,"[x for x in fruit_list if 'a' in x]")
print(t2, "new_list", "\t\t=", new_list)

    # Iterate and include all fruit that aren't 'apple'
print(n, t1, "> Iterate and include all fruit that aren't 'apple'")

new_list = [x for x in fruit_list if x != "apple"]

print(t2, "newlist", "\t\t=" ,"[x for x in fruit_list if x != 'apple']")
print(t2, "new_list", "\t\t=", new_list)

    # The iterable can be any iterable object, like a list, tuple, set etc
print(n, t1, "> The iterable can be any iterable object (e.g. in range(10))")

new_list = [x for x in range(10)]

print(t2, "new_list", "\t\t=" ,"[x for x in range(10)]")
print(t2, "new_list", "\t\t=", new_list)

    # Iterable with a condition - e.g. if x < 5
print(n, t1, "> Iterable with a condition - e.g. if x < 5")

new_list = [x for x in range(10) if x < 5]

print(t2, "new_list", "\t\t=" ,"[x for x in range(10) if x < 5]")
print(t2, "new_list", "\t\t=", new_list)

    # Manipulate the expression - e.g. convert to upper case
print(n, t1, "> Manipulate the expression - e.g. convert to upper case")

new_list = [x.upper() for x in fruit_list]

print(t2, "new_list", "\t\t=" ,"[x.upper() for x in fruit_list]")
print(t2, "new_list", "\t\t=", new_list)

    # Set the outcome to whatever you like - e.g. set all values to 'hello'
print(n, t1, "> Set the outcome to whatever you like - e.g. set all values to 'hello'")

new_list = ['hello' for x in fruit_list]

print(t2, "new_list", "\t\t=" ,"['hello' for x in fruit_list]")
print(t2, "new_list", "\t\t=", new_list)

    # Apply conditions to the expression - return 'orange' instead of 'banana'
print(n, t1, "> Apply conditions to the expression - return 'orange' instead of 'banana'")

new_list = [x if x != "banana" else "orange" for x in fruit_list]

print(t2, "new_list", "\t\t=" ,"[x if x != 'banana' else 'orange' for x in fruit_list]")
print(t2, "new_list", "\t\t=", new_list)

# Sort Lists
print(n, "Sort Lists")

str_list = ["delta", "alpha", "echo", "charlie", "bravo"]
int_list = [100, 50, 65, 82, 23]

    # Sort Strings (Ascending)
print(n, t1, "> Sort Strings (Ascending)")
print(t1, "str_list", "\t\t\t=", str_list)

str_list.sort()

print(t2, "str_list.sort()")
print(t2, "str_list", "\t\t=", str_list)

    # Sort Numberts (Ascending)
print(n, t1, "> Sort Numberts (Ascending)")
print(t1, "int_list", "\t\t\t=", int_list)

int_list.sort()

print(t2, "int_list.sort()")
print(t2, "int_list", "\t\t=", int_list)

    # Sort Descending
print(n, t1, "> Sort Numberts (Descending)")

int_list.sort(reverse = True)

print(t2, "int_list.sort(reverse = True)")
print(t2, "int_list", "\t\t=", int_list)

str_list.sort(reverse = True)

print(t2, "str_list.sort(reverse = True)")
print(t2, "str_list", "\t\t=", str_list)

    # Sort Case-Insensitive
print(n, t1, "> Sort Case-Insensitive")

str_list.sort(key = str.lower)

print(t2, "str_list.sort(key = str.lower)")
print(t2, "str_list", "\t\t=", str_list)

    # Custom Sort Function
print(n, t1, "> Custom Sort Function - e.g. sort the list based on how close the number is to 50")
print(t2, "def my_sort(n):")
print(t3, "return abs(n - 50)")
print(t2, "int_list.sort(key = my_sort)")

def my_sort(n):
  return abs(n - 50)
int_list.sort(key = my_sort)

print(t3, "result", "\t=", int_list)

# Copy Lists
print(n, "Copy Lists")

    # with copy() method

print(n, t1, "Make a copy of a list with the copy() method")

copy_list = str_list.copy()

print(t2, "copy_list = str_list.copy()")
print(t2, "copy_list", "\t\t=", copy_list)

    # with list() method
print(n, t1, "Make a copy of a list with the list() method")

copy_list = list(str_list)

print(t2, "copy_list = list(str_list)")
print(t2, "copy_list", "\t\t=", copy_list)


