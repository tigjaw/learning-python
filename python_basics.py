txt = """
Python Basics!!!

    see: https://www.w3schools.com/python/default.asp
         https://www.w3schools.com/python/python_intro.asp

Python is a popular programming language.
It was created by Guido van Rossum, and released in 1991.

It is used for:
    web development (server-side)
    software development
    mathematics
    system scripting

Python syntax can be executed by writing directly in the Command Line.
Or by creating a python file on the server,
using the .py file extension, and running it in the Command Line.

Python Indentation:
    Indentation refers to the spaces at the beginning of a code line.

    Where in other programming languages the indentation in code
    is for readability only, the indentation in Python is very important.

    Python uses indentation to indicate a block of code.

Python Variables:
    In Python, variables are created when you assign a value to it.
    Python has no command for declaring a variable.

Comments:
    Python has commenting capability for the purpose of in-code documentation.

    Comments start with a #,
    Multi-line comments start and end with a \"\"\"
    and Python will render the rest of the line as a comment.

Variable Names:
    A variable can have a short name (like x and y),
    or a more descriptive name (age, carname, total_volume).

    Rules for Python variables:
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Variable Names
print(n, "Variable Names")
  # Variable names are case-sensitive
print(t1, "> Variables are case-sensitive")
this = "lower"
THIS = "UPPER"
txt = """
                 this    = "lower"
                 THIS    = "UPPER"
                    so   : this is not the same as THIS
"""
print(txt)
  # Legal Variable Names
print(t1, "> Legal variable names")
txt = """
                 myvar   = "legal"
                 my_var  = "legal"
                 _my_var = "legal"
                 myVar   = "legal"
                 MYVAR   = "legal"
                 myvar2  = "legal"
"""
print(txt)
  # Illegal Variable Names
print(t1, "> Illegal variable names")
txt = """
                 2myvar = "illegal"
                 my-var = "illegal"
                 my var = "illegal"
"""
print(txt)
  # Multi-word Variable names
print(t1, "> Multi-word Variable names")
txt = """
                 Camel Case:
                     myVariableName   = "Camel"
                     
                 Pascal Case:
                     MyVariableName   = "Pascal"
                     
                 Snake Case:
                     my_variable_name = "Snake"

"""
print(txt)
# applying types
print("", "Assigning and Printing Types")
  # assign without type
print(t1, "> without Types")
print()
X = "5"         # x will be "5"
Y = 2           # y will be 2
Z = 7.0         # z will be 7.0
print(t2, "X = '5'")
print(t3, "result : X =", type(X), "\t=", X)
print(t2, "Y = 2")
print(t3, "result : Y =", type(Y), "\t=", Y)
print(t2, "Z = 7.0")
print(t3, "result : Z =", type(Z), "\t=", Z)
print()
  # assign with type
print(t1, "> with Types")
print()
X = str(5)      # x will be "5"
Y = int(2)      # y will be 2
Z = float(7)    # z will be 7.0
print(t2, "X = str(5)")
print(t3, "result : X =", type(X), "\t=", X)
print(t2, "Y = int(2)")
print(t3, "result : Y =", type(Y), "\t=", Y)
print(t2, "Z = float(7)")
print(t3, "result : Z =", type(Z), "\t=", Z)

# assigning the same value to multiple variables in one line
print(n, "Assigning multiple Variables/Values")
print()
a = b = c = "abc"
print(t1, "> a = b = c = 'abc'")
print(t2, "result : a =", a, ", b =", b, ", c =", c)
print()
# assigning a to a, b to b, and c to c
a, b, c = "abc" # length of string must be equal to the number of variables
print(t1, "> a,  b,  c = 'abc'")
print(t2, "result : a =", a, ", b =", b, ", c =", c)
print()
# assigning values to multiple variables in one line
fruit1, fruit2, fruit3 = "Orange", "Banana", "Cherry"
print(t1, "> fruit1, fruit2, fruit3  = 'Orange', 'Banana', 'Cherry'")
print(t2, "result : fruit1 =", fruit1, ", fruit2 =", fruit2, ", fruit3 =", fruit3)

# string concatenation
print(n, "String concatenation")
print()
  # output multiple variables, separated by a comma
print(t1, "> String concatenation with a comma")
comma1 = "Concatenate" # doesn't require spaces
comma2 = "with"
comma3 = "a COMMA"
txt = """
                 comma1 = "Concatenate" # doesn't require spaces
                 comma2 = "with"
                 comma3 = "a COMMA"
                 print(comma1, comma2, comma3)
"""
print(txt)
print(t3, "result :", comma1, comma2, comma3)
print()
  # output multiple variables, separated by a plus sign
print(t1, "> String concatenation with a comma")
plus1 = "Concatenate " # must add spaces
plus2 = "with "
plus3 = "a PLUS"
txt = """
                 plus1 = "Concatenate " # must add spaces
                 plus2 = "with "
                 plus3 = "a PLUS"
                 print(comma1, comma2, comma3)
"""
print(txt)
print(t3, "result :", plus1 + plus2 + plus3)
# demonstration of global and local variables
print(n,"Local and Global Variables")
txt = """
         > the code
         
                 # global variables
                 py = "Python is"
                 x = "awesome"

                 def print_locals():
                     # local variable
                     x = "fantastic"
                     print("local  x:", py, x)

                 def print_globals():
                     global y
                     y = "excellent"
                     global x
                     x = "wonderful"

         > run the code
         
                 print_locals()
                 print("global x:", py, x)

                 print_globals()
                 print("global x:", py, x)
                 print("global y:", py, y)
"""
print(txt)
py = "Python is"
x = "awesome" # global x variable

def print_locals():
  x = "fantastic" # local x variable
  print(t2, "local  x:", py, x)

def print_globals():
  global y
  y = "excellent"
  global x
  x = "wonderful"

print(t1, "> result:")
print()
print_locals()
print(t2, "global x:", py, x)

print_globals()
print(t2, "global x:", py, x)
print(t2, "global y:", py, y)

# IF functions and methods
print(n, "If functions and methods")
txt = """
         > define a function
         
                 x = 5
                 y = 2
                 more_than = False
                 
                 def compare_xy():
                     if x > y:
                         global more_than
                         more_than = True
                         
         > run the above function
         
                 compare_xy()
"""
print(txt)
x = 5
y = 2

  # define a function
more_than = False
def compare_xy():    
    if x > y:
        global more_than
        more_than = True

  # run the above function
compare_xy()
print(t1, "> result:")
print()
print(t2, "more_than =", more_than)
