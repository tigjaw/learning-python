txt = """
Python Dictionaries!!!

    see: https://www.w3schools.com/python/python_dictionaries.asp

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered*
In Python 3.6 and earlier, dictionaries are unordered*

A Dict is a collection which is:
    - ordered*
    - changeable
    - does not allow duplicates

Tuple items are indexed:
    - the first item has index [0]
    - the second item has index [1] etc...

Dictionary Methods:

Method	    Description
Python has a set of built-in methods that you can use on dictionaries.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

Dictionaries are written with {curly brackets}, and have keys and values.
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Creating a Dictionary
print(n, "Creating a Dictionary:")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

txt = """
         car_dict = {
             "brand": "Ford",
             "model": "Mustang",
             "year": 1964
         }
"""
print(txt)

# Printing a Dictionary
print(n, "Printing a Dictionary:", n)

    # Print Dictionary
print(t1, "> Print the Dictionary Contents")
print(t2, "print(car_dict)", "\t=", car_dict, n)

    # Print Data Type
print(t1, "> Print the Dictionary Data Type")
print(t2, "type(car_dict)", "\t=", type(car_dict), n)

    # Print Dictionary Length
print(t1, "> Print the Dictionary Length")
print(t2, "len(car_dict)", "\t\t=", len(car_dict), n)

    # Print a key value
print(t1, "> Print the Value at a specified Key")
print(t2, "thisdict['brand']", "\t=", car_dict["brand"], n)

    # Duplicates aren't allowed
print(t1, "> Duplicate values will overwrite existing values")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2002
}
txt = """
                 car_dict = {
                     "brand": "Ford",
                     "model": "Mustang",
                     "year": 1964,
                     "year": 2002
                 }
"""
print(txt)

print(t2, "print(car_dict)", "\t=", car_dict, n)

    # Data Types
print(t1, "> Dict items can be of any data type")
car_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white"]
}
txt = """
                 car_dict = {
                     "brand": "Ford",
                     "electric": False,
                     "year": 1964,
                     "colors": ["red", "white"]
                 }
"""
print(txt)

print(t2, "print(car_dict)", "\t=", car_dict)

# Accessing Items
print(n, "Access Dictionary Items")

    # with dict['key']
print(t1, "> with dict['key']", n)

brand = car_dict["brand"]

print(t2, "brand = car_dict.get('brand')")
print(t3, "brand", "\t\t=", brand, n)

    # with dict.get('key')
print(t1, "> with dict.get('key')", n)

brand = car_dict.get("brand")

print(t2, "brand = car_dict.get('brand')")
print(t3, "brand", "\t\t=", brand, n)

    # keys()
print("\t", "> Get Dictionary Keys", n)

keys = car_dict.keys()

print(t2, "keys = car_dict.keys()")
print(t3, "keys", "\t\t=", keys, n)

    # values()
print(t1, "> Get Dictionary Values", n)

values = car_dict.values()

print(t2, "values = car_dict.values()")
print(t3, "values", "\t=", values, n)

    # items()
print(t1, "> Get Dictionary Items", n)

items = car_dict.items()

print(t2, "items = car_dict.items()")
print(t3, "items", "\t\t=", items, n)

    # check if key exists
print(t1, "> Check if key exists", n)

print(t2, "if 'brand' in car_dict:")

if "brand" in car_dict:
    print(t3, "Yes, 'brand' is one of the keys in car_dict!")

# Changing Values
print(n, "Changing Dictionary Values")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(t1, "car_dict", "\t\t\t=", car_dict, n)

    # with Key
print(t1, "> with dict['key'] = value", n)

car_dict["year"] = 2018

print(t2, "car_dict['year'] = 2018")
print(t3, "car_dict", "\t=", car_dict, n)

    # update({key:value})
print(t1, "> with dict.update({key:value})", n)

car_dict.update({"year": 2020})

print(t2, "car_dict.update({'year': 2020})")
print(t3, "car_dict", "\t=", car_dict, n)

# Adding Items
print(n, "Adding Dictionary Items")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(t1, "car_dict", "\t\t\t=", car_dict, n)

    # with Key
print(t1, "> with dict['key'] = value", n)

car_dict["colour"] = "red"

print(t2, "car_dict['colour'] = 'red'")
print(t3, "car_dict", "\t=", car_dict, n)

    # update({key:value})
print(t1, "> with dict.update({key:value})", n)

car_dict.update({"colour": "red"})

print(t2, "car_dict.update({'colour': 'red'})")
print(t3, "car_dict", "\t=", car_dict, n)

# Removing Items
print(n, "Removing Dictionary Items")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(t1, "car_dict", t3, car_dict)

    # pop()
print(t1, "> with dict.pop('key')")

car_dict.pop("brand")

print(t2, "car_dict['colour'] = 'red'")
print(t3, "car_dict", "\t=", car_dict, n)

    # update({key:value})
print(t1, "> with dict.popitem()")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.popitem()

print(t2, "car_dict.popitem()")
print(t3, "car_dict", "\t=", car_dict, n)

    # del dict['key']
print(t1, "> with del dict['key']")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict["model"]

print(t2, "del car_dict['model']")
print(t3, "car_dict", "\t=", car_dict, n)

    # del dict
print(t1, "> with del dict")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict

print(t2, "del car_dict")
print(t3, "car_dict", "\t=", "no longer exists!", n)

    # clear()
print(t1, "> with dict.clear()")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.clear()

print(t2, "car_dict.clear()")
print(t3, "car_dict", "\t=", car_dict, n)

# Loop Through Dictionary
print(n, "Loop Through Dictionary")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

    # for i in dict
print(t1, "> for i in dict")

txt = """
                 for i in car_dict:
                     print(i)
"""
print(txt)

for i in car_dict:
    print(t3, i)
    
txt = """
                 for i in car_dict:
                     print(car_dict[i])
"""
print(txt)

for i in car_dict:
    print(t3, car_dict[i])
    
    # for i in dict.values()
print(n, t1, "> for i in dict.values()")

txt = """
                 for i in car_dict.values():
                     print(i)
"""
print(txt)

for i in car_dict.values():
    print(t3, i)

    # for i in dict.keys()
print(n, t1, "> for i in dict.keys()")

txt = """
                 for i in car_dict.keys():
                     print(i)
"""
print(txt)

for i in car_dict.keys():
    print(t3, i)
    
    # for i, j in dict.items()
print(n, t1, "> for i, j in dict.items()")

txt = """
                 for i, j in car_dict.items():
                     print(i)
"""
print(txt)

for i, j in car_dict.items():
    print(t3, i, j)
