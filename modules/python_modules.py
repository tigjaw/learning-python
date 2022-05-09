txt = """
Python Template!!!

    see: https://www.w3schools.com/python/python_modules.asp

What is a Module?
    Consider a module to be the same as a code library.

    A file containing a set of functions you want to include in your application.
    There are several built-in modules in Python.

Using the dir() Function
    There is a built-in function to list all the function names
    (or variable names) in a module. The dir() function.
    The dir() function can be used on all modules,
    also the ones you create yourself.

Create a Module
    To create a module, save the code in a file with the file extension .py

Use a Module
    Use the module by using the import statement

    When using a function from a module,
    use the syntax: module_name.function_name.

Variables in Module
    The module can contain functions, as already described,
    but also variables of all types (arrays, dictionaries, objects etc)

Naming a Module
    Must have the file extension .py

Re-naming a Module
    You can create an alias when you import a module,
    by using the 'as' keyword (e.g. import mymodule as mx)

Import From Module
    Import only parts from a module, by using the from keyword.
    e.g. from mymodule import person

    When importing using the from keyword,
    do not use the module name when referring to elements in the module.
    Example: person1["age"], not mymodule.person1["age"]
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
txt = """
	 > code:
	 
		 tab2

	 >>> result:
"""

txt = """
		 > code:
		 
			 tab3
			 
		 >>> result:
"""

txt = """
			 > code:

				 tab4

			 >>> result:
"""

# Comment
print(n, "Heading")
txt = """
	 > code:

	 >>> result:
"""
print(txt)

# Comment
print(n, "Heading")
txt = """
	 > code:

	 >>> result:
"""
print(txt)

# Comment
print(n, "Heading")
txt = """
	 > code:

	 >>> result:
"""
print(txt)

# Comment
print(n, "Heading")
txt = """
	 > code:

	 >>> result:
"""
print(txt)

# Comment
print(n, "Heading")
txt = """
	 > code:

	 >>> result:
"""
print(txt)
