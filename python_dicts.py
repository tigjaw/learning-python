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

# Creating a Dictionary
print("\n", "Creating a Dictionary:")
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
print("", "Printing a Dictionary:")
print()
    # Print Dictionary
print("\t", "> Print the Dictionary Contents")
print("\t\t", "print(car_dict)", "\t=", car_dict)
print()
    # Print Data Type
print("\t", "> Print the Dictionary Data Type")
print("\t\t", "type(car_dict)", "\t=", type(car_dict))
print()
    # Print Dictionary Length
print("\t", "> Print the Dictionary Length")
print("\t\t", "len(car_dict)", "\t\t=", len(car_dict))
print()
    # Print a key value
print("\t", "> Print the Value at a specified Key")
print("\t\t", "thisdict['brand']", "\t=", car_dict["brand"])
print()
    # Duplicates aren't allowed
print("\t", "> Duplicate values will overwrite existing values")
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
print("\t\t", "print(car_dict)", "\t=", car_dict)
print()
    # Data Types
print("\t", "> Dict items can be of any data type")
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
print("\t\t", "print(car_dict)", "\t=", car_dict)

# Accessing Items
print("\n", "Access Dictionary Items")
    # with dict['key']
print("\t", "> with dict['key']")
print()
brand = car_dict["brand"]
print("\t\t", "brand = car_dict.get('brand')")
print("\t\t\t", "brand", "\t\t=", brand)
print()
    # with dict.get('key')
print("\t", "> with dict.get('key')")
print()
brand = car_dict.get("brand")
print("\t\t", "brand = car_dict.get('brand')")
print("\t\t\t", "brand", "\t\t=", brand)
print()
    # keys()
print("\t", "> Get Dictionary Keys")
print()
keys = car_dict.keys()
print("\t\t", "keys = car_dict.keys()")
print("\t\t\t", "keys", "\t\t=", keys)
print()
    # values()
print("\t", "> Get Dictionary Values")
print()
values = car_dict.values()
print("\t\t", "values = car_dict.values()")
print("\t\t\t", "values", "\t=", values)
print()
    # items()
print("\t", "> Get Dictionary Items")
print()
items = car_dict.items()
print("\t\t", "items = car_dict.items()")
print("\t\t\t", "items", "\t\t=", items)
print()
    # check if key exists
print("\t", "> Check if key exists")
print()
print("\t\t", "if 'brand' in car_dict:")
if "brand" in car_dict:
    print("\t\t\t", "Yes, 'brand' is one of the keys in car_dict!")

# Changing Values
print("\n", "Changing Dictionary Values")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("\t", "car_dict", "\t\t\t=", car_dict)
print()
    # with Key
print("\t", "> with dict['key'] = value")
print()
car_dict["year"] = 2018
print("\t\t", "car_dict['year'] = 2018")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()
    # update({key:value})
print("\t", "> with dict.update({key:value})")
print()
car_dict.update({"year": 2020})
print("\t\t", "car_dict.update({'year': 2020})")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()

# Adding Items
print("\n", "Adding Dictionary Items")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("\t", "car_dict", "\t\t\t=", car_dict)
print()
    # with Key
print("\t", "> with dict['key'] = value")
print()
car_dict["colour"] = "red"
print("\t\t", "car_dict['colour'] = 'red'")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()
    # update({key:value})
print("\t", "> with dict.update({key:value})")
print()
car_dict.update({"colour": "red"})
print("\t\t", "car_dict.update({'colour': 'red'})")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()

# Removing Items
print("\n", "Removing Dictionary Items")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("\t", "car_dict", "\t\t\t=", car_dict)
    # pop()
print("\t", "> with dict.pop('key')")
car_dict.pop("brand")
print("\t\t", "car_dict['colour'] = 'red'")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()
    # update({key:value})
print("\t", "> with dict.popitem()")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.popitem()
print("\t\t", "car_dict.popitem()")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()
    # del dict['key']
print("\t", "> with del dict['key']")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict["model"]
print("\t\t", "del car_dict['model']")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()
    # del dict
print("\t", "> with del dict")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict
print("\t\t", "del car_dict")
print("\t\t\t", "car_dict", "\t=", "no longer exists!")
print()
    # clear()
print("\t", "> with dict.clear()")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.clear()
print("\t\t", "car_dict.clear()")
print("\t\t\t", "car_dict", "\t=", car_dict)
print()

# Loop Through Dictionary
print("\n", "Loop Through Dictionary")
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
    # for i in dict
print("\t", "> for i in dict")
txt = """
                 for i in car_dict:
                     print(i)
"""
print(txt)
for i in car_dict:
    print("\t\t\t", i)
txt = """
                 for i in car_dict:
                     print(car_dict[i])
"""
print(txt)
for i in car_dict:
    print("\t\t\t", car_dict[i])
print()
    # for i in dict.values()
print("\t", "> for i in dict.values()")
txt = """
                 for i in car_dict.values():
                     print(i)
"""
print(txt)
for i in car_dict.values():
    print("\t\t\t", i)
print()
    # for i in dict.keys()
print("\t", "> for i in dict.keys()")
txt = """
                 for i in car_dict.keys():
                     print(i)
"""
print(txt)
for i in car_dict.keys():
    print("\t\t\t", i)
print()
    # for i, j in dict.items()
print("\t", "> for i, j in dict.items()")
txt = """
                 for i, j in car_dict.items():
                     print(i)
"""
print(txt)
for i, j in car_dict.items():
    print("\t\t\t", i, j)
print()
