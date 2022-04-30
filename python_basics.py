txt = """
Python Basics!!!

    see: https://www.w3schools.com/python/python_intro.asp

Python is a popular programming language.
It was created by Guido van Rossum, and released in 1991.

It is used for:
    web development (server-side)
    software development
    mathematics
    system scripting
"""

print(txt)

hello_world = "hello_world = HELLO, WORLD!"
print("", hello_world)
print("\t", "Strings are arrays, so hello_world[0] =", hello_world[0])

this = "this"
THIS = "THIS"
print("\t", "Variables are case-sensitive, so:")
print("\t", this, "is not the same as", THIS)

print("\n", "Assigning and Printing Types")
# applying types
X = str(5)      # x will be "5"
Y = int(2)      # y will be 2
Z = float(7)    # z will be 7.0

# printing types
print("\t", "X:", type(X), "=", X)
print("\t", "Y:", type(Y), "=", Y)
print("\t", "Z:", type(Z), "=", Z)

print("\n", "Assigning multiple Variables/Values")
# assigning the same value to multiple variables in one line
a = b = c = "abc"
print("\t", "a = b = c = 'abc' \t: a =", a, ", b =", b, ", c =", c)

# assigning a to a, b to b, and c to c
a, b, c = "abc" # length of string must be equal to the number of variables
print("\t", "a, b, c = 'abc' \t: a =", a, ", b =", b, ", c =", c)

# assigning values to multiple variables in one line
fruit1, fruit2, fruit3 = "Orange", "Banana", "Cherry"
print("\t", fruit1, fruit2, fruit3)

print("\n","Lists, Tuples, and Dicts")
# creating and unpacking a list
fruit_list = ["Apple", "Peach", "Plum"]
print("\t", "fruit_list:")
print("\t\t", "type:", type(fruit_list))
print("\t\t", "content:", fruit_list)
fruit1, fruit2, fruit3 = fruit_list
print("\t", "fruit_list unpacked:")
print("\t\t", "fruit1 = ", fruit1)
print("\t\t", "fruit2 = ", fruit2)
print("\t\t", "fruit3 = ", fruit3)

# creating and unpacking a tuple
fruit_tuple = ("Grapes", "Strawberry", "Pineapple")
print("\t", "fruit_tuple:")
print("\t\t", "type:", type(fruit_tuple))
print("\t\t", "content:", fruit_tuple)
fruit1, fruit2, fruit3 = fruit_tuple
print("\t", "fruit_tuple unpacked:")
print("\t\t", "fruit1 = ", fruit1)
print("\t\t", "fruit2 = ", fruit2)
print("\t\t", "fruit3 = ", fruit3)

# unpacking a dict
fruit_dict = {"Fruit" : "Lemon", "Sourness" : 75}
print("\t", type(fruit_dict))

print("\n", "String concatenation")
# output multiple variables, separated by a comma
comma1 = "Concatenate" # doesn't require spaces
comma2 = "with"
comma3 = "a COMMA"
print("\t", comma1, comma2, comma3)

# output multiple variables, separated by a plus sign
plus1 = "Concatenate " # must add spaces
plus2 = "with "
plus3 = "a PLUS"
print("\t", plus1 + plus2 + plus3)

print("\n","Local and Global Variables")
# demonstration of global and local variables
py = "Python is "
x = "awesome" # global x variable

def print_locals():
  x = "fantastic" # local x variable
  print("\t", "local x:", py + x)

def print_globals():
  global y
  y = "excellent"
  global x
  x = "wonderful"

print_locals()
print("\t", "global x:", py + x)

print_globals()
print("\t", "global x:", py + x)
print("\t", "global y:", py + y)

print("\n", "If functions and methods")
x = 5
y = 2
print("\t", "x =", x, ", y =", y)
# define a function
def compare_xy():
    print("\t", "x =", x, ", y =", y)
    print("\t", "FUNCTION - is ", x, "(x) more than", y, "(y) ?")
    if x > y:
        print("\t", "YES, ", x, "is more than", y)
# run the above function
compare_xy()
