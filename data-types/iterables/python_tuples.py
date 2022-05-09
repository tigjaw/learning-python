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

# use for formatting code
n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# use for formatting snippets
"""
	 tab1
		 tab2
			 tab3
				 tab4
"""

# Creating a Tuple
print(n, "Creating a Tuple:", n)

fruit_tuple = ("apple", "banana", "cherry")

print(t1, f"fruit_tuple {t3}= ('apple', 'banana', 'cherry')", n)

    # Print Tuple and Tuple Length
print(t2, f"print(fruit_tuple) {t1}=",fruit_tuple)
print(t2, f"len(fruit_list) {t1}=", len(fruit_tuple))

# Data Types
print(n, t1,"> Tuple items can be of any data type:")

    # Single Data Types
txt = f"""
		 str_tuple {t2}= ("apple", "banana", "cherry")
		 int_tuple {t2}= (1, 5, 7, 9, 3)
		 bool_tuple {t2}= (True, False, False)
"""
print(txt)

str_tuple = ("apple", "banana", "cherry")
int_tuple = (1, 5, 7, 9, 3)
bool_tuple = (True, False, False)

    # Mixed Data Types
print(t1, "> Tuples can contain multiple data types:")

mixed_tuple = ("abc", 34, True, 40, "male")

print(n, t2, f"mixed_tuple {t2}= ('abc', 34, True, 40, 'male')")

    # Tuple Object Type
print(n, t1, "> Find the type of a Tuple:")

print(n, t2, f"type(int_tuple) {t1}=", type(int_tuple))

# Access Items
print(n, "Accessing Tuple items:")

fruit_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(n, t1, f"fruit_tuple {t3}=", fruit_tuple)

    # Access Single Items
print(n, t1, "> Access Single Items:", n)

print(t2, f"fruit_tuple[1] {t1}=", fruit_tuple[1])
print(t2, f"fruit_tuple[-1] {t1}=", fruit_tuple[-1])

    # Access Range of Items
print(n, t1, "> Access Range of Items:", n)

print(t2, f"fruit_tuple[2:5] {t1}=", fruit_tuple[2:5])
print(t2, f"fruit_tuple[:4] {t1}=", fruit_tuple[:4])
print(t2, f"fruit_tuple[2:] {t1}=", fruit_tuple[2:])
print(t2, f"fruit_tuple[-4:-1] {t1}=", fruit_tuple[-4:-1])

# Check if item exists
print(n, "Check if item exists in Tuple:")

txt = f"""
		 > code;
		 
			 if "apple" in fruit_tuple:
				 print("Yes, 'apple' is in fruit_tuple")

		 >>> result:
"""
print(txt)

if "apple" in fruit_tuple:
    print(t3, "Yes, 'apple' is in fruit_tuple")

# Changing Tuple items
print(n, "Changing Tuple")

txt = f"""
		 > code;
		 
                         # convert the Tuple into a List and back into a Tuple
                         
			 fruit_tuple {t1}= ("apple", "banana", "cherry")
			 fruit_list {t1}= list(fruit_tuple)
			 fruit_list[1] {t1}= "kiwi"
			 modified_tuple = tuple(fruit_list)

		 >>> result:
"""
print(txt)

fruit_tuple = ("apple", "banana", "cherry")
fruit_list = list(fruit_tuple)
fruit_list[1] = "kiwi"
modified_tuple = tuple(fruit_list)

print(t3, "modified_tuple =", modified_tuple)

# Append Tuple items
print(n, "Append items")

txt = f"""
		 > code;
		 
                         # convert the Tuple into a List and back into a Tuple
                         
			 fruit_tuple {t1}= ("apple", "banana", "cherry")
                         fruit_list {t1}= list(fruit_tuple)
                         
                         fruit_list.append("orange")
                         
                         fruit_tuple {t1}= tuple(fruit_list)

		 >>> result:
"""
print(txt)

fruit_tuple = ("apple", "banana", "cherry")
fruit_list = list(fruit_tuple)
fruit_list.append("orange")
fruit_tuple = tuple(fruit_list)

print(t3, f"fruit_tuple {t1}=", fruit_tuple)

# Remove Tuple Items
fruit_tuple = ("apple", "banana", "cherry")

    # Remove Tuple Values
print(n, "Remove items")

txt = f"""
		 > code;
		 
                         # convert the Tuple into a List and back into a Tuple
                         
			 fruit_list {t1}= list(fruit_tuple)
			 
                         fruit_list.remove("apple")
                         
                         fruit_tuple {t1}= tuple(fruit_list)

		 >>> result:
"""
print(txt)

fruit_list = list(fruit_tuple)
fruit_list.remove("apple")
fruit_tuple = tuple(fruit_list)

print(t3, f"fruit_tuple {t1}=", fruit_tuple)

    # Delete Tuple
print(n, "Delete Tuple")

txt = f"""
		 > code;
                         
			 del fruit_tuple

		 >>> result:
"""
print(txt)

print(t3, f"no more Tuple!")

# Unpacking a Tuple
print(n, "Unpacking a Tuple")

    # Basic unpacking
print(n, t1, "> Basic Unpacking")

txt = f"""
		 > code;
                         
			 fruit_tuple {t3}= ("Apple", "Peach", "Plum")
			 
			 (fruit1, fruit2, fruit3) {t1}= fruit_tuple

		 >>> result:
"""
print(txt)

fruit_tuple = ("Apple", "Peach", "Plum")
(fruit1, fruit2, fruit3) = fruit_tuple

print(t3, f"fruit1 {t3}=", fruit1)
print(t3, f"fruit2 {t3}=", fruit2)
print(t3, f"fruit3 {t3}=", fruit3)

    # Using *Asterisk
print(n, t1, "> Unpacking with *Asterisk")

fruit_tuple = ("apple", "banana", "cherry", "strawberry", "raspberry")

print(n, t2, f"fruit_tuple {t2}=", fruit_tuple)

        # *fruit1
print(n, t2, "> (*fruit1, fruit2, fruit3) = fruit_tuple")

(*fruit1, fruit2, fruit3) = fruit_tuple

print(n, t2, ">>> unpacked:", n)
print(t3, f"fruit1 {t1}=", fruit1)
print(t3, f"fruit2 {t1}=", fruit2)
print(t3, f"fruit3 {t1}=", fruit3)

        # *fruit2
print(n, t2, "> (fruit1, *fruit2, fruit3) = fruit_tuple")

(fruit1, *fruit2, fruit3) = fruit_tuple

print(n, t2, ">>> unpacked:", n)
print(t3, f"fruit1 {t1}=", fruit1)
print(t3, f"fruit2 {t1}=", fruit2)
print(t3, f"fruit3 {t1}=", fruit3)

        # *fruit3
print(n, t2, "> (fruit1, fruit2, *fruit3) = fruit_tuple")

(fruit1, fruit2, *fruit3) = fruit_tuple

print(n, t2, ">>> unpacked:", n)
print(t3, f"fruit1 {t1}=", fruit1)
print(t3, f"fruit2 {t1}=", fruit2)
print(t3, f"fruit3 {t1}=", fruit3)

# Loop Through Tuples
print(n, "Loop through Tuple items")

fruit_tuple = ("Apple", "Peach", "Plum")

print(n, t1, f"fruit_tuple =", fruit_tuple)

    # for i in tuple
print(n, t1, "> for i in tuple")

txt = """
		 for i in fruit_tuple:
                     print(i)

                 >>> result:
"""
print(txt)

for i in fruit_tuple:
    print(t3, i)

    # for i in range(j)
print(n, t1, "> for i in range(j)")

txt = """
		 for i in range(len(fruit_tuple)):
                     print(fruit_tuple[i])

                 >>> result:
"""
print(txt)

for i in range(len(fruit_tuple)):
    print(t3, fruit_tuple[i])

    # while i < j
print(n, t1, "> while i < j")

txt = """
		 i = 0
		 while i < len(fruit_tuple):
                     print(fruit_tuple[i])
                     i = i + 1

                 >>> result:
"""
print(txt)

i = 0
while i < len(fruit_tuple):
    print(t3, fruit_tuple[i])
    i = i + 1

# Join Tuples
print(n, "Join Tuples")

txt = f"""
	 str_tuple {t2}= ("a", "b", "c")
	 int_tuple {t2}= (1, 2, 3)
"""
print(txt)

str_tuple = ("a", "b", "c")
int_tuple = (1, 2, 3)

    # add
print(t1, "> join with + (add)")

txt = """
		 join = str_tuple + int_tuple

                 >>> result:
"""
print(txt)

join = str_tuple + int_tuple

print(t3, f"join {t1}=", join)

    # multiply
print(n, t1, "> join with * (multiply)")

txt = """
		 join = str_tuple * 2

                 >>> result:
"""
print(txt)

join = str_tuple * 2

print(t3, f"join {t1}=", join)
