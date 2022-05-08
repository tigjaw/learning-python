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
 clear()	                Removes all the elements from the set
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
 union()	                Return a set containing the union of sets
 update()	                Updates the set with the union of this set and others

* you can remove items and add new items.
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

# Creating a Set
print(n, "Creating a Set:", n)

fruit_set = {"apple", "banana", "cherry", "apple"}

print(t1, f"fruit_set {t3}= ('apple', 'banana', 'cherry', 'apple')", n)

    # Print Set and Set Length
print(t2, f"print(fruit_set) {t1}=", fruit_set)
print(t2, f"len(fruit_set) {t1}=", len(fruit_set))
print(t2, "Duplicate 'apple' was not accepted", n)

# Data Types
print(t1,"> Set items can be of any data type:")

    # Single Data Types
txt = f"""
		 str_set {t2}= {'apple', 'banana', 'cherry'}
		 int_set {t2}= {1, 5, 7, 9, 3}
		 bool_set {t2}= {True, False, False}
"""
print(txt)

str_set = {"apple", "banana", "cherry"}
int_set = {1, 5, 7, 9, 3}
bool_set = {True, False, False}

    # Mixed Data Types
print(t1, "> Sets can contain multiple data types:", n)

mixed_set = ("abc", 34, True, 40, "male")

print(t2, f"mixed_set {t2}= ('abc', 34, True, 40, 'male')", n)

    # Tuple Object Type
print(t1, "> Find the type of a Set:", n)

print(t2, f"type(int_set) {t2}=", type(int_set))

# Loop / Access Items
print(n, "Loop / Access Set items via loop:")

txt = f"""
		 > code;
		 
			 for i in fruit_set:
				 print(i)

		 >>> result:
"""
print(txt)

for i in fruit_set:
  print(t3, i)

# Check if item exists
print(n, "Check if item exists in Set:")

txt = f"""
		 > code;
		 
			 if "apple" in fruit_set:
				 print("Yes, 'apple' is in fruit_set")

		 >>> result:
"""
print(txt)

if "apple" in fruit_set:
    print(t3, "Yes, 'apple' is in fruit_set")

# Add Set items
print(n, "Add Items", n)

    # Add items
print(t1, "> add()")

txt = f"""
		 > code;
		 
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 fruit_set.add("orange")

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set.add("orange")

print(t3, f"fruit_set {t1}=", fruit_set)

    # Add Sets
print(n, t1, "> update(set)")

txt = f"""
		 > code;
		 
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 fruit_set2 {t1}= {"pineapple", "mango", "papaya"}
			 
			 fruit_set.update(fruit_set2)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set2 = {"pineapple", "mango", "papaya"}
fruit_set.update(fruit_set2)

print(t3, f"fruit_set {t1}=", fruit_set)

    # Add Any Collection
print(n, t1, "> update(any iterable)")

txt = f"""
		 > code;
		 
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 fruit_list {t1}= ["kiwi", "orange"]
			 
			 fruit_set.update(fruit_list)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_list = ["kiwi", "orange"]

fruit_set.update(fruit_list)

print(t3, f"fruit_set {t1}=", fruit_set)

# Remove Set Items
print(n, "Remove Set items", n)

    # set.remove(i) - remove specified value
print(t1, f"> Remove specified value {t1}- set.remove(i)")

txt = f"""
		 > code;
		 
                         #If the item to remove does not exist, remove() WILL raise an error.
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 fruit_set.remove("banana")

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set.remove("banana")

print(t3, f"result {t1}=", fruit_set)

    # set.discard(i) - remove specified value
print(n, t1, f"> Discard specified value {t1}- set.discard(i)")

txt = f"""
		 > code;
		 
                         #If the item to remove does not exist, discard() will NOT raise an error.
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 fruit_set.discard("banana")

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set.discard("banana")

print(t3, f"result {t1}=", fruit_set)

    # set.pop() - remove last item
print(n, t1, f"> Remove last item {t2}= set.pop()")

txt = f"""
		 > code;
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 fruit_set.pop()

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set.pop()

print(t3, f"result {t1}=", fruit_set)

    # del set - delete Set
print(n, t1, f"> Delete Set {t3}= " "del set")

txt = f"""
		 > code;
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 del fruit_set

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}

print(t3, f"result {t1}=", "no more Set!")

    # set.clear() - clear Set
print(n, t1, f"> Clear Set {t3}= " "set.clear()")

txt = f"""
		 > code;
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 
			 fruit_set.clear()

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
fruit_set.clear()

print(t3, f"result {t1}=", fruit_set)

# Join Tuples
print(n, "Join Tuples")

    # union()
print(n, t1, "> set.union(set)")

txt = f"""
		 > code;
                         
			 str_set {t1}= {"a", "b" , "c"}
			 int_set {t1}= {1, 2, 3}
			 
			 new_set = str_set.union(int_set)

		 >>> result:
"""
print(txt)

str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}
new_set = str_set.union(int_set)

print(t3, f"new_set {t1}=", new_set)

    # update()
print(n, t1, "> set.update(set)")

txt = f"""
		 > code;
                         
			 str_set {t1}= {"a", "b" , "c"}
			 int_set {t1}= {1, 2, 3}
			 
			 new_set = str_set.update(int_set)

		 >>> result:
"""
print(txt)

str_set = {"a", "b" , "c"}
int_set = {1, 2, 3}
new_set = str_set.update(int_set)

print(t3, f"new_set {t1}=", new_set)

    # intersection_update()
print(n, t1, "> set.intersection_update(set)")

txt = f"""
		 > code;
                         # preserves duplicates
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 techs_set {t1}= {"google", "microsoft", "apple"}
			 
			 fruit_set.intersection_update(techs_set)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
techs_set = {"google", "microsoft", "apple"}
fruit_set.intersection_update(techs_set)

print(t3, f"fruit_set {t1}=", fruit_set)

    # intersection()
print(n, t1, "> set.intersection(set)")

txt = f"""
		 > code;

                         # preserves duplicates
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 techs_set {t1}= {"google", "microsoft", "apple"}
			 
			 new_set = fruit_set.intersection(techs_set)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
techs_set = {"google", "microsoft", "apple"}
new_set = fruit_set.intersection(techs_set)

print(t3, f"new_set =", new_set)

    # symmetric_difference_update()
print(n, t1, "> set.symmetric_difference_update(set)")

txt = f"""
		 > code;

                         # preserves all except duplicates
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 techs_set {t1}= {"google", "microsoft", "apple"}
			 
			 fruit_set.symmetric_difference_update(techs_set)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
techs_set = {"google", "microsoft", "apple"}
fruit_set.symmetric_difference_update(techs_set)

print(t3, f"fruit_set {t1}=", fruit_set)

    # symmetric_difference()
print(n, t1, "> set.symmetric_difference(set)")

txt = f"""
		 > code;
		 
                         # preserves all except duplicates
                         
			 fruit_set {t1}= {"apple", "banana", "cherry"}
			 techs_set {t1}= {"google", "microsoft", "apple"}
			 
			 new_set = fruit_set.symmetric_difference(techs_set)

		 >>> result:
"""
print(txt)

fruit_set = {"apple", "banana", "cherry"}
techs_set = {"google", "microsoft", "apple"}
new_set = fruit_set.symmetric_difference(techs_set)

print(t3, f"new_set {t1}=", new_set)
