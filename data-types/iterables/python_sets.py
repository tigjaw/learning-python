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

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Creating a Set
print(n, "Creating a Set:")

fruit_set = {"apple", "banana", "cherry", "apple"}

print(t1, "> fruit_set", "\t\t\t=", "('apple', 'banana', 'cherry', 'apple')")

    # Print Set and Set Length
print(t2, "print(fruit_set)", "\t=",fruit_set)
print(t2, "len(fruit_set)", "\t=", len(fruit_set))
print(t2, "Duplicate 'apple' was not accepted")

# Data Types
print(t1,"> Set items can be of any data type:")

    # Single Data Types
str_set = {"apple", "banana", "cherry"}
int_set = {1, 5, 7, 9, 3}
bool_set = {True, False, False}

print(t2, "str_set", "\t\t=", "{'apple', 'banana', 'cherry'}")
print(t2, "int_set", "\t\t=", "{1, 5, 7, 9, 3}")
print(t2, "bool_set", "\t\t=", "{True, False, False}")

    # Mixed Data Types
print(t1, "> Sets can contain multiple data types:")

mixed_set = ("abc", 34, True, 40, "male")

print(t2, "mixed_set", "\t\t=", "('abc', 34, True, 40, 'male')")

    # Tuple Object Type
print(t1, "> Find the type of a Set:")
print(t2, "type(int_set)", "\t=", type(int_set))

# Loop / Access Items
print(n, "Loop / Access Set items via loop:")

print(t1, "> for i in set")
print(t2, "for i in fruit_set:")
print(t3, "print(i)")

for i in fruit_set:
  print(t4, i)

# Check if item exists
print(n, "Check if item exists in Set:")

print(t1, "if 'apple' in fruit_set:")

if "apple" in fruit_set:
    print(t2, "Yes, 'apple' is in fruit_set")

# Add Set items
print(n, "Add Items")

    # Add items
print(t1, "> add()")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "fruit_set", "\t\t=", fruit_set)

fruit_set.add("orange")

print(t2, "fruit_set.add('orange')")
print(t3, "fruit_set", "\t=", fruit_set)

    # Add Sets
print(t1, "> update(set)")

fruit_set = {"apple", "banana", "cherry"}
fruit_set2 = {"pineapple", "mango", "papaya"}

print(t2, "fruit_set", "\t\t=", fruit_set)
print(t2, "fruit_set2", "\t\t=", fruit_set2)

fruit_set.update(fruit_set2)

print(t2, "fruit_set.update(fruit_set2)")
print(t3, "fruit_set", "\t=", fruit_set)

    # Add Any Collection
print(t1, "> update(any iterable)")

fruit_set = {"apple", "banana", "cherry"}
fruit_list = ["kiwi", "orange"]

print(t2, "fruit_set", "\t\t=", fruit_set)
print(t2, "fruit_list", "\t\t=", fruit_list)

fruit_set.update(fruit_list)

print(t2, "fruit_set.update(fruit_list)")
print(t3, "fruit_set", "\t=", fruit_set)

# Remove Set Items
print(n, "Remove Set items")

    # set.remove(i) - remove specified value
print(t1, "> Remove specified value", "\t-", "set.remove(i)")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "If the item to remove does not exist, remove() will raise an error.")
print(t2, "fruit_list", "\t\t=", fruit_set)

fruit_set.remove("banana")

print(t2, "fruit_set.remove('banana')")
print(t3, "result", "\t=", fruit_set)

    # set.discard(i) - remove specified value
print(t1, "> Discard specified value", "\t-", "set.discard(i)")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "If the item to remove does not exist, discard() will NOT raise an error.")
print(t2, "fruit_set", "\t\t=", fruit_set)

fruit_set.discard("banana")

print(t2, "fruit_set.discard('banana')")
print(t3, "result", "\t=", fruit_set)
    # set.pop() - remove last item
print(t1, "> Remove last item", "\t\t=", "set.pop()")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "fruit_set", "\t\t=", fruit_set)

fruit_set.pop()

print(t2, "fruit_set.pop()")
print(t3, "result", "\t=", fruit_set)

    # del set - delete Set
print(t1, "> Delete Set", "\t\t\t=", "del set")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "fruit_set", "\t\t=", fruit_set)
print(t2, "del fruit_set")
print(t3, "result", "\t=", "no more Set!")

    # set.clear() - clear Set
print(t1, "> Clear Set", "\t\t\t=", "set.clear()")

fruit_set = {"apple", "banana", "cherry"}

print(t2, "fruit_set", "\t\t=", fruit_set)

fruit_set.clear()

print(t2, "fruit_set.clear()")
print(t3, "result", "\t=", fruit_set)

# Join Tuples
print(n, "Join Tuples")

    # union()
print(t1, "> with set.union(set)")

str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}

print(t2, "str_set", "\t\t=", str_set)
print(t2, "int_set", "\t\t=", int_set)

result = str_set.union(int_set)

print(t2, "result = str_set.union(int_set)")
print(t3, "result", "\t=", result)

    # update()
print(t1, "> with set.update(set)")

str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}

print(t2, "str_set", "\t\t=", str_set)
print(t2, "int_set", "\t\t=", int_set)

result = str_set.update(int_set)

print(t2, "result = str_set.update(int_set)")
print(t3, "result", "\t=", result)

    # intersection_update()
print(t1, "> with set.intersection_update(set) - preserves duplicates")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(t2, "x", "\t\t\t=", x)
print(t2, "y", "\t\t\t=", y)

x.intersection_update(y)

print(t2, "x.intersection_update(y)")
print(t3, "x", "\t\t=", x)

    # intersection()
print(t1, "> with set.intersection(set) - preserves duplicates")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(t2, "x", "\t\t\t=", x)
print(t2, "y", "\t\t\t=", y)

result = x.intersection(y)

print(t2, "result = x.intersection(y)")
print(t3, "result", "\t=", result)

    # symmetric_difference_update()
print(t1, "> with set.intersection(set) - preserves all except duplicates")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(t2, "x", "\t\t\t=", x)
print(t2, "y", "\t\t\t=", y)

x.symmetric_difference_update(y)

print(t2, "x.symmetric_difference_update(y)")
print(t3, "x", "\t=", x)

    # symmetric_difference()
print(t1, "> with set.symmetric_difference(set) - preserves all except duplicates")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(t2, "x", "\t\t\t=", x)
print(t2, "y", "\t\t\t=", y)

result = x.symmetric_difference(y)

print(t2, "result = x.symmetric_difference(y)")
print(t3, "result", "\t=", result)
