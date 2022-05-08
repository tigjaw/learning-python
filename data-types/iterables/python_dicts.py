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

# use for formatting code
n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# use for formatting snippets
"""
	 tab1
		 tab2
			 tab3
				 tab4
"""

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
print(n, "Printing a Dictionary:")

    # Print Dictionary
print(n, t1, "> Print the Dictionary Contents", n)
print(t2, f"print(car_dict) {t1}=", car_dict)

    # Print Data Type
print(n, t1, "> Print the Dictionary Data Type", n)
print(t2, f"type(car_dict) {t1}=", type(car_dict))

    # Print Dictionary Length
print(n, t1, "> Print the Dictionary Length", n)
print(t2, f"len(car_dict) {t2}=", len(car_dict))

    # Print a key value
print(n, t1, "> Print the Value at a specified Key", n)
print(t2, f"thisdict['brand'] {t1}=", car_dict["brand"])

    # Duplicates aren't allowed
print(n, t1, "> Duplicate values will overwrite existing values")

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

print(t2, f"print(car_dict) {t1}=", car_dict)

    # Data Types
print(n, t1, "> Dict items can be of any data type")

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

print(t2, f"print(car_dict) {t1}=", car_dict)

# Accessing Items
print(n, "Access Dictionary Items")

print(n, t1, f"car_dict {t2}=", car_dict)

    # with dict['key']
print(n, t1, "> with dict['key']")

txt = f"""
		 > code:
		 
			 brand {t1}= car_dict["brand"]

		 >>> result:
"""
print(txt)

brand = car_dict["brand"]

print(t3, f"brand {t1}=", brand)

    # with dict.get('key')
print(n, t1, "> with dict.get('key')")

txt = f"""
		 > code:
		 
			 brand {t1}= car_dict.get("brand")

		 >>> result:
"""
print(txt)

brand = car_dict.get("brand")

print(t3, f"brand {t1}=", brand)

    # keys()
print(n, t1, "> Get Dictionary Keys")

txt = f"""
		 > code:
		 
			 keys {t1}= car_dict.keys()

		 >>> result:
"""
print(txt)

keys = car_dict.keys()

print(t3, f"keys {t1}=", keys)

    # values()
print(n, t1, "> Get Dictionary Values")

txt = f"""
		 > code:
		 
			 vals {t1}= car_dict.values()

		 >>> result:
"""
print(txt)

vals = car_dict.values()

print(t3, f"vals {t1}=", vals)

    # items()
print(n, t1, "> Get Dictionary Items")

txt = f"""
		 > code:
		 
			 items {t1}= car_dict.items()

		 >>> result:
"""
print(txt)

items = car_dict.items()

print(t3, f"itms {t1}=", items)

    # check if key exists
print(n, t1, "> Check if key exists")

txt = """
		 > code:
		 
			 if "brand" in car_dict:
                             print("Yes, 'brand' is one of the keys in car_dict!")

		 >>> result:
"""
print(txt)

if "brand" in car_dict:
    print(t3, "Yes, 'brand' is one of the keys in car_dict!")

# Changing Values
print(n, "Changing Dictionary Values")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(n, t1, f"car_dict {t3}=", car_dict)

    # with Key
print(n, t1, "> with dict['key'] = value")

txt = """
		 car_dict["year"] = 2018

	 >>> result:
"""
print(txt)

car_dict["year"] = 2018

print(t2, f"car_dict {t1}=", car_dict)

    # update({key:value})
print(n, t1, "> with dict.update({key:value})")

txt = """
		 car_dict.update({"year": 2020})

	 >>> result:
"""
print(txt)

car_dict.update({"year": 2020})

print(t2, f"car_dict {t1}=", car_dict)

# Adding Items
print(n, "Adding Dictionary Items")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(n, t1, f"car_dict {t3}=", car_dict)

    # with Key
print(n, t1, "> with dict['key'] = value")

txt = """
		 car_dict["colour"] = "red"

	 >>> result:
"""
print(txt)

car_dict["colour"] = "red"

print(t2, f"car_dict {t1}=", car_dict)

    # update({key:value})
print(n, t1, "> with dict.update({key:value})")

txt = """
		 car_dict.update({"colour": "red"})

	 >>> result:
"""
print(txt)

car_dict.update({"colour": "red"})

print(t2, f"car_dict {t1}=", car_dict)

# Removing Items
print(n, "Removing Dictionary Items")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(n, t1, "car_dict", t3, car_dict)

    # pop()
print(n, t1, "> with dict.pop('key')")

txt = """
		 car_dict.pop("brand")

	 >>> result:
"""
print(txt)

car_dict.pop("brand")

print(t2, f"car_dict {t1}=", car_dict)

    # update({key:value})
print(n, t1, "> with dict.popitem()")

txt = """
		 car_dict.popitem()

	 >>> result:
"""
print(txt)

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.popitem()

print(t2, f"car_dict {t1}=", car_dict)

    # del dict['key']
print(n, t1, "> with del dict['key']")

txt = """
		 del car_dict["model"]

	 >>> result:
"""
print(txt)

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict["model"]

print(t2, f"car_dict {t1}=", car_dict)

    # del dict
print(n, t1, "> with del dict")

txt = """
		 del car_dict

	 >>> result:
"""
print(txt)

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dict

print(t2, f"car_dict {t1}= no longer exists!")

    # clear()
print(n, t1, "> with dict.clear()")

txt = """
		 car_dict.clear()

	 >>> result:
"""
print(txt)

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_dict.clear()

print(t2, f"car_dict {t1}=", car_dict)

# Loop Through Dictionary
print(n, "Loop Through Dictionary")

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

    # for i in dict
print(n, t1, "> for i in dict")

txt = """
		 > code:
	 
			 for i in car_dict:
                             print(i)
                     
		 >>> result:
"""
print(txt)

for i in car_dict:
    print(t3, i)
    
txt = """
		 > code:
	 
			 for i in car_dict:
                             print(car_dict[i])
                     
		 >>> result:
"""
print(txt)

for i in car_dict:
    print(t3, car_dict[i])
    
    # for i in dict.values()
print(n, t1, "> for i in dict.values()")

txt = """
		 > code:
	 
			 for i in car_dict.values():
                             print(i)
                     
		 >>> result:
"""
print(txt)

for i in car_dict.values():
    print(t3, i)

    # for i in dict.keys()
print(n, t1, "> for i in dict.keys()")

txt = """
		 > code:
	 
			 for i in car_dict.keys():
                             print(i)
                     
		 >>> result:
"""
print(txt)

for i in car_dict.keys():
    print(t3, i)
    
    # for i, j in dict.items()
print(n, t1, "> for i, j in dict.items()")

txt = """
		 > code:
	 
			 for i, j in car_dict.items():
                             print(i, j)
                     
		 >>> result:
"""
print(txt)

for i, j in car_dict.items():
    print(t3, i, j)
