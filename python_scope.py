txt = """
Python Scope!!!

    see: https://www.w3schools.com/python/python_scope.asp

A variable is only available from inside the region it is created.
This is called scope.

Local Scope:
    A variable created inside a function belongs
    to the local scope of that function,
    and can only be used inside that function.

Global Scope:
    A variable created in the main body of the Python code
    is a global variable and belongs to the global scope.

    Global variables are available from within any scope, global and local.

Global Keyword:
    If you need to create a global variable,
    but are stuck in the local scope, you can use the global keyword.

    The global keyword makes the variable global.
    Also, use the global keyword if you want to make a change
    to a global variable inside a function.

Naming Variables:
    If you operate with the same variable name inside and outside of a function,
    Python will treat them as two separate variables,
    one available in the global scope (outside the function)
    and one available in the local scope (inside the function)
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

# Local scope
print(n, "Local scope")

    # inside a function
print(n, t1, "> Inside a Function")

txt = """
		 > code:
		 
			 def my_function():
			 
                             x = 777
                             print(x)

                         my_function()
			 
		 >>> result:
"""
print(txt)

def my_function():
    
    x = 777
    print(t3, x)

my_function()

    # function inside function
print(n, t1, "> Function inside Function")

txt = """
		 > code:
		 
			 def my_function():
			 
                             x = 777
                             
                             def my_inner_function():
                                 print(x)
                                 
                             my_inner_function()
                             
                         my_function()
			 
		 >>> result:
"""
print(txt)

def my_function():
    x = 777
  
    def my_inner_function():
        print(t3, x)
    my_inner_function()

my_function()

# Comment
print(n, "Global Scope")

    # global scope
print(n, t1, "> Global variable")

txt = """
		 > code:
		 
			 x = 777
			 
                         def my_function():
                             print(x)
                             
                         my_function()
                         print(x)
			 
		 >>> result:
"""
print(txt)

x = 777

def my_function():
    print(t3, x)

my_function()
print(t3, x)

    # naming variables
print(n, t1, "> Maming variables")

txt = """
		 > code:
		 
			 x = 777
			 
                         def my_function():
                             x = 444
                             print(x)
                             
                         my_function()
                         print(x)
			 
		 >>> result:
"""
print(txt)

x = 777

def my_function():
    x = 1
    print(t3, x)

my_function()
print(t3, x)

# Comment
print(n, "Global keyword")

    # create global variable, within in the local scope
print(n, t1, "> create global variable, within in the local scope")

txt = """
		 > code:
		 
			 def my_function():
                             global x
                             x = 777
                             
                         print(x)
			 
		 >>> result:
"""
print(txt)

def my_function():
    global x
    x = 777

my_function()

print(t3, x)

    # use global keyword to change global variable
print(n, t1, "> use global keyword to change global variable")

txt = """
		 > code:
		 
			 x = 777
			 
                         def my_function():
                             global x
                             x = 1
                             
                         my_function()
                         print(x)
			 
		 >>> result:
"""
print(txt)

x = 300

def my_function():
    global x
    x = 200

my_function()

print(t3, x)
