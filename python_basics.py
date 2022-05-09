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

# use for formatting code
n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# use for formatting snippets
"""
	 tab1
		 tab2
			 tab3
				 tab4
"""

# Variable Names
print(n, "Variable Names")

  # Variable names are case-sensitive
print(t1, "> Variables are case-sensitive")

txt = """
                 # these are different variables
                 
                 this    = "lower"
                 THIS    = "UPPER"
"""
print(txt)

this = "lower"
THIS = "UPPER"

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
print(n, t1, "> without Types")

txt = """
                 > code:
                 
			 X = "5"
			 Y = 2
			 Z = 7.0
			 
                 >>> result:
"""
print(txt)

X = "5"
Y = 2
Z = 7.0

print(t3, "X =", X, f"{t2}", type(X))
print(t3, "Y =", Y, f"{t2}", type(Y))
print(t3, "Z =", Z, f"{t1}", type(Z))

  # assign with type
print(n, t1, "> with Types")

txt = """
                 > code:
                 
			 X = str(5)
			 Y = int(2)
			 Z = float(7)
			 
                 >>> result:
"""
print(txt)

X = str(5)
Y = int(2)
Z = float(7)

print(t3, "X =", X, f"{t2}", type(X))
print(t3, "Y =", Y, f"{t2}", type(Y))
print(t3, "Z =", Z, f"{t1}", type(Z))

# assigning the same value to multiple variables in one line
print(n, "Assigning multiple Variables/Values")

  # assign one value to multiple variables
print(n, t1, "> assign one value to multiple variables")
txt = """
                 > code:
                 
			 a = b = c = "abc"
			 
                 >>> result:
"""
print(txt)

a = b = c = "abc"

print(t3, "a =", a)
print(t3, "b =", b)
print(t3, "c =", c)

  # assign iterable indices to individual variables
print(n, t1, "> assign iterable indices to individual variables")
txt = """
                 > code:
                 
			 # length of string must be equal to the number of variables

			 a, b, c = "abc"
			 x, y, z = "xxx", "yyy", "zzz"
			 i, j, k = 1, 2, 3
			 A, B, C = {"A", "B", "C"}
			 
                 >>> result:
"""
print(txt)

a, b, c = "abc"
x, y, z = "xxx", "yyy", "zzz"
i, j, k = 1, 2, 3
A, B, C = {"A", "B", "C"}

print(t3, "a =", a)
print(t3, "b =", b)
print(t3, "c =", c)
print()
print(t3, "x =", x)
print(t3, "y =", y)
print(t3, "z =", z)
print()
print(t3, "i =", i)
print(t3, "j =", j)
print(t3, "k =", k)
print()
print(t3, "A =", A)
print(t3, "B =", B)
print(t3, "C =", C)

# string concatenation
print(n, "String concatenation")

  # output multiple variables, separated by a comma
print(n, t1, "> with a comma")

txt = """
                 > code:

                         # doesn't require spaces
                         
                         comma1 = "Concatenate"
                         comma2 = "with"
                         comma3 = "COMMA"
                         
                         print(comma1, comma2, comma3)
			 
                 >>> result:
"""
print(txt)

comma1 = "Concatenate" 
comma2 = "with"
comma3 = "COMMA"

print(t3, comma1, comma2, comma3)

  # output multiple variables, separated by a plus sign
print(t1, "> with a plus")

txt = """
                 > code:

                         # does require spaces
                         
                         plus1 = "Concatenate"
                         plus2 = "with"
                         plus3 = "PLUS"
                         
                         print(plus1, plus2, plus3)
			 
                 >>> result:
"""
print(txt)

plus1 = "Concatenate" 
plus2 = "with"
plus3 = "PLUS"

print(t3, plus1 + plus2 + plus3)

# demonstration of global and local variables
print(n,"Local and Global Variables")

txt = """
	 > code:
         
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
                     
                 print_locals()
                 
                 print("global x:", py, x)

                 print_globals()
                 
                 print("global x:", py, x)
                 print("global y:", py, y)
                 
         >>> result:
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

print_locals()
print(t2, "global x:", py, x)

print_globals()
print(t2, "global x:", py, x)
print(t2, "global y:", py, y)

# IF functions and methods
print(n, "If functions and methods")

txt = """
         > code:
         
                 x = 5
                 y = 2
                 more_than = False
                 
                 def compare_xy():
                     if x > y:
                         global more_than
                         more_than = True
                         
                 compare_xy()
                 print(more_than)
                 
         >>> result:
"""
print(txt)

x = 5
y = 2
more_than = False

def compare_xy(): # define a function
    if x > y:
        global more_than
        more_than = True

compare_xy()

print(t2, "more_than =", more_than)
