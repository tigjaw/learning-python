txt = """
Python Booleans!!!

    see: https://www.w3schools.com/python/python_booleans.asp

In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python,
and get one of two answers, True or False.

When you compare two values, the expression is evaluated
and Python returns the Boolean answer:
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Comparing and printing expressions
print("", "Comparing and printing results")
print(t1, "10 > 9", "\t=", 10 > 9)
print(t1, "10 == 9", "\t=", 10 == 9)
print(t1, "10 < 9", "\t=", 10 < 9)

# evaluate values and variables
print(t1, "bool('Hello')\t=", bool("Hello"))
print(t1, "bool(15)\t=", bool(15))
"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
# false values
print(n, "False Values:")
print(t1, "Any string is True, except empty strings")
print(t1, "Any number is True, except 0")
print(t1, "Any list, tuple, set, and dictionary are True, except empty ones")
print()
print(t1, "bool(False)", "\t=", bool(False))
print(t1, "bool(None)", "\t=", bool(None))
zero = 0
txt = "bool({})"
print(t1, txt.format(zero), "\t=", bool(None))
print(t1, "bool("")", "\t=", bool(""))
print(t1, "bool(())", "\t=", bool(()))
print(t1, "bool([])", "\t=", bool([]))
print(t1, "bool({})", "\t=", bool({}))

# object with a _len_ function
print(n, "False Object with _len_ function:")
print(t1, "class myclass():")
print(t2, "def __len__(self):")
print(t3, "return 0")
print(t1, "myobj = myclass()")
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(t1, "bool(myobj) = ", bool(myobj))

# returning a boolean
print(n, "Returning a Boolean")
print(t1, "def returns_boolean() :")
print(t2, "return True")
def returns_boolean() :
  return True
print(t1, "returns_boolean() = ", returns_boolean())

# Boolean method checks
print(n, "Boolean method checks:")
x = 200
txt = "x = {}"
print(t1, txt.format(x))
print(t2, "isinstance(x, int) = ", isinstance(x, int))
