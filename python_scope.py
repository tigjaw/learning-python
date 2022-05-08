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

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Local scope
print(n, "Local scope")
txt = f"""

"""
print(txt)

def myfunc():
    x = 300
    print(t2, x)

myfunc()

# Comment
print(n, "Heading")
txt = f"""

"""
print(txt)

# Comment
print(n, "Heading")
txt = f"""

"""
print(txt)

# Comment
print(n, "Heading")
txt = f"""

"""
print(txt)

# Comment
print(n, "Heading")
txt = f"""

"""
print(txt)
