txt = """
Python Classes and Objects!!!

    see: https://www.w3schools.com/python/python_classes.asp

Python Classes/Objects:
    Python is an object oriented programming language.
    Almost everything in Python is an object,
    with its properties and methods.

    A Class is like an object constructor,
    or a "blueprint" for creating objects.

he __init__() Function:
    The examples above are classes and objects in their simplest form,
    and are not really useful in real life applications.

    To understand the meaning of classes we have to
    understand the built-in __init__() function.

    All classes have a function called __init__(),
    which is always executed when the class is being initiated.

    Use the __init__() function to assign values to object properties,
    or other operations that are necessary to do when the object is being created

Object Methods:
    Objects can also contain methods.
    Methods in objects are functions that belong to the object.

The Self Parameter:
    The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class.

    It does not have to be named self , you can call it whatever you like,
    but it has to be the first parameter of any function in the class
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

# Creating a Class
print(n, "Creating a Class & Object")
txt = """
         > code:
         
		 class MyClass:
                     x = 5
            
                 mc = MyClass()
                 print(mc.x)
"""
print(txt)

class MyClass:
    x = 5
    
mc = MyClass()
print(t1, "> result:", mc.x)

# __init__() Function
print(n, "__init__() Function")
txt = """
         > code:
         
		 class Person:
                     def __init__(self, name, age):
                         self.name = name
                         self.age = age
            
                 person = Person("John", 36)
                 print(f"{person.name} ({person.age})")
"""
print(txt)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 36)

print(t1, f"> result: {person.name} ({person.age})")

# Object Methods
print(n, "Object Methods")
txt = """
         > code:
         
		 class Person:
                     def __init__(self, name, age):
                         self.name = name
                         self.age = age

                     def result(self):
                         print(f"{self.name} ({self.age})")
            
		 person = Person("John", 36)
                 perrson.result()
"""
print(txt)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def result(self):
    print(t1, f"> result: {self.name} ({self.age})")

perrson = Person("John", 36)
perrson.result()

# Self Parameter
print(n, "Self Parameter")
txt = """
         > code:
         
		 class Person:
                     def __init__(reference, name, age):
                         reference.name = name
                         reference.age = age

                     def result(inst):
                         print(f"{inst.name} ({inst.age})")
            
		 person = Person("John", 36)
                 perrson.result()
"""
print(txt)

class Person:
  def __init__(reference, name, age):
    reference.name = name
    reference.age = age

  def result(inst):
    print(t1, f"> result: {inst.name} ({inst.age})")

perrson = Person("John", 36)
perrson.result()

# Modify Object
print(n, "Modify Objects")
txt = """
         > Modify Object Properties
         
		 person.age = 40
		 
	 > Delete Object Properties
	 
                 del person.age
                 
         > Delete Objects

                 del player
"""
print(txt)
