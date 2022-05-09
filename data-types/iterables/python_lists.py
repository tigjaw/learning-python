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

# use for formatting code
n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# use for formatting snippets
"""
	 tab1
		 tab2
			 tab3
				 tab4
"""

# Creating a List
print(n, "Creating a list and Printing Contents:")

txt = f"""
	 > code:
	 
		 fruit_list {t2}= ["apple", "banana", "cherry"]
		 print(fruit_list)
		 print(len(fruit_list))
		 
	 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]

print(t2, f"print(fruit_list) {t1}=", fruit_list)
print(t2, f"len(fruit_list) {t1}=", len(fruit_list))

    # Data Types
print(n, t1, "> List items can be of any data type:")

        # Single Data Types
txt = f"""
		 str_list {t2}= ['apple', 'banana', 'cherry']
		 int_list {t2}= [1, 5, 7, 9, 3]
		 bool_list {t2}= [True, False, False]
"""
print(txt)

str_list = ["apple", "banana", "cherry"]
int_list = [1, 5, 7, 9, 3]
bool_list = [True, False, False]

        # Mixed Data Types
print(t1, "> Lists can contain multiple data types:", n)

mixed_list = ["abc", 34, True, 40, "male"]

print(t2, f"mixed_list {t2}= ['abc', 34, True, 40, 'male']")

        # List Object Type
print(n, t1, "> Find the type of a list:", n)

print(t2, f"type(int_list) {t1}=", type(int_list))

# Access Items
print(n, "Accessing list items:", n)

fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(t1, f"fruit_list {t3}=", fruit_list)

    # Access Single Items
print(n, t1, "> Access Single Items:", n)

print(t2, f"fruit_list[1] {t2}=", fruit_list[1])
print(t2, f"fruit_list[-1] {t1}=", fruit_list[-1])

    # Access Range of Items
print(n, t1, "> Access Range of Items:", n)

print(t2, f"fruit_list[2:5] {t1}=", fruit_list[2:5])
print(t2, f"fruit_list[:4] {t1}=", fruit_list[:4])
print(t2, f"fruit_list[2:] {t1}=", fruit_list[2:])
print(t2, f"fruit_list[-4:-1] {t1}=", fruit_list[-4:-1])

# Check if item exists
print(n, "Check if item exists in list:")

txt = """
	 > code:
	 
		 if "apple" in fruit_list:
			 print("Yes, 'apple' is in fruit_list")
			 
	 >>> result:
"""
print(txt)

if "apple" in fruit_list:
    print(t2, "Yes, 'apple' is in fruit_list")

# Unpacking a list
print(n, "Unpacking a List")

txt = f"""
	 > code:
	 
		 fruit_list {t2}= ["Apple", "Peach", "Plum"]
		 fruit1, fruit2, fruit3 = fruit_list
			 
	 >>> result:
"""
print(txt)

fruit_list = ["Apple", "Peach", "Plum"]
fruit1, fruit2, fruit3 = fruit_list

print(t2, f"fruit1 {t2}=", fruit1)
print(t2, f"fruit2 {t2}=", fruit2)
print(t2, f"fruit3 {t2}=", fruit3)

# Changing list items
print(n, "Changing list items:", n)

fruit_list = ["apple", "banana", "cherry"]

print(t1, f"fruit_list {t3}=", fruit_list)

    # Change Single Item
print(n, t1, "> Replace a single item", n)

fruit_list[1] = "blackberry"

print(t2, f"fruit_list[1] {t2}= 'blackberry'")
print(n, t2, f">>> result: {t2}=", fruit_list)

    # Change a range of list items
print(n, t1, "> Replace a range of items", n)

fruit_list[1:3] = ["apricot", "watermelon"]

print(t2, f"fruit_list[1:3] {t1}= ['apricot', 'watermelon']")
print(n, t2, f">>> result: {t2}=", fruit_list)

    # Replace Single Item with Multiple
print(n, t1, "> Replace a single item with multiple")

fruit_list[1:2] = ["pear", "tomato"]

print(n, t2, f"fruit_list[1:2] {t1}= ['pear', 'tomato']")
print(n, t2, f">>> result: {t2}=", fruit_list)

# Inserting items
print(n, "Inserting list items at a specific index:", n)

txt = f"""
	 > code:
	 
		 fruit_list {t2}= ["apple", "banana", "cherry"]
		 
		 fruit_list.insert(2, "pineapple")
			 
	 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.insert(2, "pineapple")

print(t2, f"fruit_list: {t2}=", fruit_list)

# Append items
print(n, "Appending list items (to the end of the list):", n)

txt = f"""
	 > code:
	 
		 fruit_list {t2}= ["apple", "banana", "cherry"]
		 
		 fruit_list.append("orange")
			 
	 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.append("orange")

print(t2, f"fruit_list: {t2}=", fruit_list)

# Extend List
print(n, "Extending a list", n)

txt = f"""
	 > code:

                 # extend with any collection type
                
		 fruit_list {t2}= ["apple", "banana", "cherry"]
		 more_fruit {t2}= ["mango", "pineapple", "papaya"]
		 
		 fruit_list.extend(more_fruit)
			 
	 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
more_fruit = ["mango", "pineapple", "papaya"]
fruit_list.extend(more_fruit)

print(t2, f"result {t2}=", fruit_list)

# Remove List Items
print(n, "Remove list items")

    # list.remove(i) - remove specified value
print(n, t1, f"> Remove specified value")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 fruit_list.remove("banana")
			 
                 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.remove("banana")

print(t3, f"fruit_list {t1}=", fruit_list)

    # list.pop(i) - remove specified index
print(n, t1, f"> Remove specified index")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 fruit_list.pop(1)
			 
                 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.pop(1)

print(t3, f"fruit_list {t1}=", fruit_list)

    # list.pop() - remove last index
print(n, t1, f"> Remove last index")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 fruit_list.pop()
			 
                 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.pop()

print(t3, f"result {t1}=", fruit_list)

    # del list[i] - remove specified index
print(t1, f"> Remove specified index")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 del fruit_list[0]
			 
                 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
del fruit_list[0]

print(t3, f"result {t1}=", fruit_list)

    # del list - delete list
print(n, t1, f"> Delete list")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 del fruit_list
			 
                 >>> result:
"""
print(txt)

print(t3, f"result {t1}= no more list!")

    # list.clear() - clear list
print(n, t1, f"> Clear list")

txt = f"""
                 > code:
                
			 fruit_list {t1}= ["apple", "banana", "cherry"]
		 
			 fruit_list.clear()
			 
                 >>> result:
"""
print(txt)

fruit_list = ["apple", "banana", "cherry"]
fruit_list.clear()

print(t3, f"result {t1}=", fruit_list)

# Loop Through Lists
print(n, "Loop through list items")

fruit_list = ["apple", "banana", "cherry"]

print(n, t1, f"fruit_list {t3}=", fruit_list)

    # for i in list
print(n, t1, "> for i in list")

txt = f"""
                 > code:
                
			 for i in fruit_list:
                             print(i)
			 
                 >>> result:
"""
print(txt)

for i in fruit_list:
    print(t3, i)

    # for x in range(i)
print(n, t1, "> for i in range(i)")

txt = f"""
                 > code:
                
			 for i in range(len(fruit_list)):
                             print(fruit_list[i])
			 
                 >>> result:
"""
print(txt)

for i in range(len(fruit_list)):
    print(t3, fruit_list[i])
  
    # while i < j:
print(n, t1, "> while i < j")

txt = f"""
                 > code:
                 
                         i = 0
			 while i < len(fruit_list):
                             print(fruit_list[i])
                             i = i + 1
			 
                 >>> result:
"""
print(txt)

i = 0
while i < len(fruit_list):
    print(t3, fruit_list[i])
    i = i + 1

# List Comprehension
print(n, "List Comprehension")

fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]

print(n, t1, f"fruit_list {t3}=", fruit_list)

    # Iterate and include all fruit
print(n, t1, "> Iterate and include all fruit")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x for x in fruit_list]
			 
                 >>> result:
"""
print(txt)

new_list = [x for x in fruit_list]

print(t3, f"new_list {t1}=", new_list)

    # Iterate and include only fruit that contain the letter 'a'
print(n, t1, "> Iterate and include only fruit that contain the letter 'a'")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x for x in fruit_list if "a" in x]
			 
                 >>> result:
"""
print(txt)

new_list = [x for x in fruit_list if "a" in x]

print(t3, f"new_list {t1}=", new_list)

    # Iterate and include all fruit that aren't 'apple'
print(n, t1, "> Iterate and include all fruit that aren't 'apple'")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x for x in fruit_list if x != "apple"]
			 
                 >>> result:
"""
print(txt)

new_list = [x for x in fruit_list if x != "apple"]

print(t3, f"new_list {t1}=", new_list)

    # The iterable can be any iterable object, like a list, tuple, set etc
print(n, t1, "> The iterable can be any iterable object (e.g. in range(10))")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x for x in range(10)]
			 
                 >>> result:
"""
print(txt)

new_list = [x for x in range(10)]

print(t3, f"new_list {t1}=", new_list)

    # Iterable with a condition - e.g. if x < 5
print(n, t1, "> Iterable with a condition - e.g. if x < 5")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x for x in range(10) if x < 5]
			 
                 >>> result:
"""
print(txt)

new_list = [x for x in range(10) if x < 5]

print(t3, f"new_list {t1}=", new_list)

    # Manipulate the expression - e.g. convert to upper case
print(n, t1, "> Manipulate the expression - e.g. convert to upper case")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x.upper() for x in fruit_list]
			 
                 >>> result:
"""
print(txt)

new_list = [x.upper() for x in fruit_list]

print(t3, f"new_list {t1}=", new_list)

    # Set the outcome to whatever you like - e.g. set all values to 'hello'
print(n, t1, "> Set the outcome to whatever you like - e.g. set all values to 'hello'")

txt = f"""
                 > code:
                 
                         new_list {t1}= ['hello' for x in fruit_list]
			 
                 >>> result:
"""
print(txt)

new_list = ['hello' for x in fruit_list]

print(t3, f"new_list {t1}=", new_list)

    # Apply conditions to the expression - return 'orange' instead of 'banana'
print(n, t1, "> Apply conditions to the expression - return 'orange' instead of 'banana'")

txt = f"""
                 > code:
                 
                         new_list {t1}= [x if x != "banana" else "orange" for x in fruit_list]
			 
                 >>> result:
"""
print(txt)

new_list = [x if x != "banana" else "orange" for x in fruit_list]

print(t3, f"new_list {t1}=", new_list)

# Sort Lists
print(n, "Sort Lists", n)

str_list = ["delta", "alpha", "echo", "charlie", "bravo"]
int_list = [100, 50, 65, 82, 23]

print(t1, f"str_list {t3}=", str_list)
print(t1, f"int_list {t3}=", int_list)

    # Sort Strings (Ascending)
print(n, t1, "> Sort Strings (Ascending)")

txt = f"""
                 > code:
                 
                         str_list.sort()
			 
                 >>> result:
"""
print(txt)

str_list.sort()

print(t3, f"str_list {t1}=", str_list)

    # Sort Case-Insensitive
print(n, t1, "> Sort String (Case-Insensitive)")

txt = f"""
                 > code:
                 
                         str_list.sort(key = str.lower)
			 
                 >>> result:
"""
print(txt)

str_list.sort(key = str.lower)

print(t3, f"str_list {t1}=", str_list)

    # Sort Numberts (Ascending)
print(n, t1, "> Sort Numberts (Ascending)")

txt = f"""
                 > code:
                 
                         int_list.sort()
			 
                 >>> result:
"""
print(txt)

int_list.sort()

print(t3, f"int_list {t1}=", int_list)

    # Sort Descending
print(n, t1, "> Sort Numberts (Descending)")

txt = f"""
                 > code:
                 
                         int_list.sort(reverse = True)
                         str_list.sort(reverse = True)
			 
                 >>> result:
"""
print(txt)

int_list.sort(reverse = True)
str_list.sort(reverse = True)

print(t3, f"int_list {t1}=", int_list)
print(t3, f"str_list {t1}=", str_list)

    # Custom Sort Function
print(n, t1, "> Custom Sort Function")

txt = f"""
                 > code:

                         # sort the list based on how close the number is to 50
                         
                         def my_sort(n):
                             return abs(n - 50)

                         int_list.sort(key = my_sort)
			 
                 >>> result:
"""
print(txt)

def my_sort(n):
    return abs(n - 50)
int_list.sort(key = my_sort)

print(t3, f"result {t1}=", int_list)

# Copy Lists
print(n, "Copy Lists", n)

    # with copy() method
print(n, t1, "> with copy() method")

txt = f"""
                 > code:

                         copy_list {t1}= str_list.copy()
			 
                 >>> result:
"""
print(txt)

copy_list = str_list.copy()

print(t3, f"copy_list {t1}=", copy_list)

    # with list() method
print(n, t1, "> with list() method")

txt = f"""
                 > code:

                         copy_list {t1}= list(str_list)
			 
                 >>> result:
"""
print(txt)

copy_list = list(str_list)

print(t3, f"copy_list {t1}=", copy_list)


