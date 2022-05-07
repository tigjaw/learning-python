txt = """
Python Functions!!!

    see: https://www.w3schools.com/python/python_functions.asp

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

In Python a function is defined using the def keyword.

Arguments & Parameters:
    Information can be passed into functions as arguments.

    Arguments are specified after the function name, inside the parentheses.
    You can add as many arguments as you want, just separate them with a comma.

    The following example has a function with one argument (fname).
    When the function is called, we pass along a first name,
    which is used inside the function to print the full name

    > Arbitrary Arguments, *args:
        If you do not know how many arguments that will be passed into your function,
        add a * before the parameter name in the function definition.

        This way the function will receive a tuple of arguments,
        and can access the items accordingly

    > Keyword Arguments:
        You can also send arguments with the key = value syntax.

        This way the order of the arguments does not matter.

    > Arbitrary Keyword Arguments, **kwargs:
        If you do not know how many keyword arguments that will be passed into your function,
        add two asterisk: ** before the parameter name in the function definition.

        This way the function will receive a dictionary of arguments,
        and can access the items accordingly.
        
    > Default Parameter Value:
        The following example shows how to use a default parameter value.

        If we call the function without argument, it uses the default value.
        
    > Passing a List as an Argument
        You can send any data types of argument to a function (string, number, list, dictionary etc.),
        and it will be treated as the same data type inside the function.

        E.g. if you send a List as an argument,
        it will still be a List when it reaches the function.

Return Values:
    To let a function return a value, use the return statement

The pass Statement:
    Function definitions cannot be empty,
    but if you for some reason have a function definition with no content,
    put in the pass statement to avoid getting an error.

Recursion:
    Python also accepts function recursion, which means a defined function can call itself.

    Recursion is a common mathematical and programming concept.
    It means that a function calls itself.
    This has the benefit of meaning that you can loop through data to reach a result.

    The developer should be very careful with recursion
    as it can be quite easy to slip into writing a function which never terminates,
    or one that uses excess amounts of memory or processor power.
    However, recursion can be a very efficient and elegant approach to programming.

    To a new developer it can take some time to work out how exactly this works,
    best way to find out is by testing and modifying it.
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Creating & Calling a Function
print(n, "Creating & Calling a Function")
txt = """
	 > Code
             
		 def my_function():
                     print("Hello from a function")
"""
print(txt)
print(t1, "> result:", n)

def my_function():
    print(t2, "Hello from a function")
my_function()

# Arguments
print(n, "Arguments")
txt = """
	 > Code
             
		 def my_function(first_name):
                     print(first_name, "Smith")

                 my_function("Agent")
"""
print(txt)
print(t1, "> result:", n)

def my_function(first_name):
    print(t2, first_name, "Smith")
my_function("Agent")

# Multiple Arguments
print(n, "Multiple Arguments")
txt = """
	 > Code
             
		 def my_function(first_name, age):
                     print(first_name, age)

                 my_function("Agent", 100)
"""
print(txt)
print(t1, "> result:", n)

def my_function(first_name, age):
    print(t2, f"name: {first_name}, age: {age}")
my_function("Agent", 100)

# Arbitrary Arguments
print(n, "Arbitrary Arguments")
txt = """
	 > Code
             
		 def my_function(*args):
                     print(f"number of arguments: {len(args)}")

                 my_function("args 1", "args 2", "args 3")
"""
print(txt)
print(t1, "> result:", n)

def my_function(*args):
    print(t2, f"number of arguments: {len(args)}")
my_function("arg 1", "arg 2", "args 3")

# Keyword Arguments kwargs
print(n, "Keyword Arguments (kwargs)")
txt = """
	 > Code
             
		 def my_function(arg1, arg2, arg3):
                     print("The order of the arguments does not matter!")

                 my_function(arg1 = 1, arg2 = 2, arg3 = 3)
"""
print(txt)
print(t1, "> result:", n)

def my_function(arg1, arg2, arg3):
    print(t2, "The order of the arguments does not matter!")

my_function(arg1 = 1, arg2 = 2, arg3 = 3)

# Arbitrary Keyword Arguments **kwargs
print(n, "Arbitrary Keyword Arguments (**kwargs)")
txt = """
	 > Code
             
		 def my_function(**child):
                     print("The child's last name is " + child["last_name"])

                 my_function(first_name = "Agent", last_name = "Smith")
"""
print(txt)
print(t1, "> result:", n)

def my_function(**child):
    print(t2, "The child's last name is " + child["last_name"])

my_function(first_name = "Agent", last_name = "Smith")

# Default Parameter Value
print(n, "Default Parameter Value")
txt = """
	 > Code
             
		 def my_function(country = "England"):
                     print("I am from", country)

                 my_function("Brazil")
                 my_function()
"""
print(txt)
print(t1, "> result:", n)

def my_function(country = "England"):
    print(t2, "I am from", country)

my_function("Brazil")
my_function()

# List as an Argument
print(n, "List as an Argument")
txt = """
	 > Code
             
		 def my_function(fruit):
                     for x in fruit:
                         print(x)

                 fruit_list = ["apple", "banana", "cherry"]
                 my_function(fruit_list)
"""
print(txt)
print(t1, "> result:", n)

def my_function(fruit):
    for x in fruit:
        print(t2, x)

fruit_list = ["apple", "banana", "cherry"]
my_function(fruit_list)

# Return Values
print(n, "Return Values")
txt = """
	 > Code
             
		 def my_function(x):
                     return 5 * x

                 print(my_function(3))
"""
print(txt)
print(t1, "> result:", n)

def my_function(x):
    return 5 * x

print(t2, my_function(3))

# Recursion
print(n, "Recursion")
txt = """
	 > Code
             
		 def tri_recursion(k):
                     print("k =", k)
                     result = k + tri_recursion(k - 1)
                     print("result =", result)
                 else:
                     result = 0
                 print(t2, "returning result")
                 return result

                 tri_recursion(6)
"""
print(txt)
print(t1, "> result:", n)

def tri_recursion(k):
    if(k > 0):
        print(t2, "k =", k)
        result = k + tri_recursion(k - 1)
        print(t3, "  result =", result)
    else:
        result = 0
    print(t2, "returning result")
    return result

tri_recursion(6)
