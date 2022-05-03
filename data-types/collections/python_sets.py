txt = """
Python Sets!!!

    see: https://www.w3schools.com/python/python_sets.asp

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A tuple is a collection which is:
    - unordered
    - unchangeable*
    - unindexed
    - does not allow duplicates

Set Methods
Python has a set of built-in methods that you can use on sets.

Method	                        Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	        Removes the items in this set that are also included in another, specified set
discard()	                Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	Inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                Updates the set with the union of this set and others

* you can remove items and add new items.
"""

print(txt)

# Creating a Set
print("\n", "Creating a Set:")
fruit_set = {"apple", "banana", "cherry", "apple"}

print("\t", "> fruit_set", "\t\t\t=", "('apple', 'banana', 'cherry', 'apple')")
    # Print Set and Set Length
print("\t\t", "print(fruit_set)", "\t=",fruit_set)
print("\t\t", "len(fruit_set)", "\t=", len(fruit_set))
print("\t\t", "Duplicate 'apple' was not accepted")

# Data Types
print("\t","> Set items can be of any data type:")
    # Single Data Types
str_set = {"apple", "banana", "cherry"}
int_set = {1, 5, 7, 9, 3}
bool_set = {True, False, False}
print("\t\t", "str_set", "\t\t=", "{'apple', 'banana', 'cherry'}")
print("\t\t", "int_set", "\t\t=", "{1, 5, 7, 9, 3}")
print("\t\t", "bool_set", "\t\t=", "{True, False, False}")
    # Mixed Data Types
print("\t", "> Sets can contain multiple data types:")
mixed_set = ("abc", 34, True, 40, "male")
print("\t\t", "mixed_set", "\t\t=", "('abc', 34, True, 40, 'male')")
    # Tuple Object Type
print("\t", "> Find the type of a Set:")
print("\t\t", "type(int_set)", "\t=", type(int_set))

# Loop / Access Items
print("\n", "Loop / Access Set items via loop:")
print("\t", "> for i in set")
print("\t\t", "for i in fruit_set:")
print("\t\t\t", "print(i)")
for i in fruit_set:
  print("\t\t\t\t", i)

# Check if item exists
print("\n", "Check if item exists in Set:")
print("\t", "if 'apple' in fruit_set:")
if "apple" in fruit_set:
    print("\t\t", "Yes, 'apple' is in fruit_set")

# Add Set items
print("\n", "Add Items")

    # Add items
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> add()")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
fruit_set.add("orange")
print("\t\t", "fruit_set.add('orange')")
print("\t\t\t", "fruit_set", "\t=", fruit_set)

    # Add Sets
fruit_set = {"apple", "banana", "cherry"}
fruit_set2 = {"pineapple", "mango", "papaya"}
print("\t", "> update(set)")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
print("\t\t", "fruit_set2", "\t\t=", fruit_set2)
fruit_set.update(fruit_set2)
print("\t\t", "fruit_set.update(fruit_set2)")
print("\t\t\t", "fruit_set", "\t=", fruit_set)

    # Add Any Collection
fruit_set = {"apple", "banana", "cherry"}
fruit_list = ["kiwi", "orange"]
print("\t", "> update(any iterable)")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
print("\t\t", "fruit_list", "\t\t=", fruit_list)
fruit_set.update(fruit_list)
print("\t\t", "fruit_set.update(fruit_list)")
print("\t\t\t", "fruit_set", "\t=", fruit_set)

# Remove Set Items
print("\n", "Remove Set items")
    # set.remove(i) - remove specified value
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> Remove specified value", "\t-", "set.remove(i)")
print()
print("\t\t", "If the item to remove does not exist, remove() will raise an error.")
print()
print("\t\t", "fruit_list", "\t\t=", fruit_set)
fruit_set.remove("banana")
print("\t\t", "fruit_set.remove('banana')")
print("\t\t\t", "result", "\t=", fruit_set)
    # set.discard(i) - remove specified value
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> Discard specified value", "\t-", "set.discard(i)")
print()
print("\t\t", "If the item to remove does not exist, discard() will NOT raise an error.")
print()
print("\t\t", "fruit_set", "\t\t=", fruit_set)
fruit_set.discard("banana")
print("\t\t", "fruit_set.discard('banana')")
print("\t\t\t", "result", "\t=", fruit_set)
    # set.pop() - remove last item
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> Remove last item", "\t\t=", "set.pop()")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
fruit_set.pop()
print("\t\t", "fruit_set.pop()")
print("\t\t\t", "result", "\t=", fruit_set)
    # del set - delete Set
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> Delete Set", "\t\t\t=", "del set")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
print("\t\t", "del fruit_set")
print("\t\t\t", "result", "\t=", "no more Set!")
    # set.clear() - clear Set
fruit_set = {"apple", "banana", "cherry"}
print("\t", "> Clear Set", "\t\t\t=", "set.clear()")
print("\t\t", "fruit_set", "\t\t=", fruit_set)
fruit_set.clear()
print("\t\t", "fruit_set.clear()")
print("\t\t\t", "result", "\t=", fruit_set)

# Join Tuples
print("\n", "Join Tuples")

    # union()
print("\t", "> with set.union(set)")
str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}
print("\t\t", "str_set", "\t\t=", str_set)
print("\t\t", "int_set", "\t\t=", int_set)
result = str_set.union(int_set)
print("\t\t", "result = str_set.union(int_set)")
print("\t\t\t", "result", "\t=", result)

    # update()
print("\t", "> with set.update(set)")
str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}
print("\t\t", "str_set", "\t\t=", str_set)
print("\t\t", "int_set", "\t\t=", int_set)
result = str_set.update(int_set)
print("\t\t", "result = str_set.update(int_set)")
print("\t\t\t", "result", "\t=", result)

    # intersection_update()
print("\t", "> with set.intersection_update(set) - preserves duplicates")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("\t\t", "x", "\t\t\t=", x)
print("\t\t", "y", "\t\t\t=", y)
x.intersection_update(y)
print("\t\t", "x.intersection_update(y)")
print("\t\t\t", "x", "\t\t=", x)

    # intersection()
print("\t", "> with set.intersection(set) - preserves duplicates")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("\t\t", "x", "\t\t\t=", x)
print("\t\t", "y", "\t\t\t=", y)
result = x.intersection(y)
print("\t\t", "result = x.intersection(y)")
print("\t\t\t", "result", "\t=", result)

    # symmetric_difference_update()
print("\t", "> with set.intersection(set) - preserves all except duplicates")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("\t\t", "x", "\t\t\t=", x)
print("\t\t", "y", "\t\t\t=", y)
x.symmetric_difference_update(y)
print("\t\t", "x.symmetric_difference_update(y)")
print("\t\t\t", "x", "\t=", x)

    # symmetric_difference()
print("\t", "> with set.symmetric_difference(set) - preserves all except duplicates")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("\t\t", "x", "\t\t\t=", x)
print("\t\t", "y", "\t\t\t=", y)
result = x.symmetric_difference(y)
print("\t\t", "result = x.symmetric_difference(y)")
print("\t\t\t", "result", "\t=", result)
