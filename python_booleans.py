txt = """
Python Booleans!!!

    see: https://www.w3schools.com/python/python_booleans.asp
"""

print(txt)

# Comparing and printing expressions
print("", "Comparing and printing results")
print("\t", "10 > 9", "\t=", 10 > 9)
print("\t", "10 == 9", "\t=", 10 == 9)
print("\t", "10 < 9", "\t=", 10 < 9)

# evaluate values and variables
print("\t", "bool('Hello')\t=", bool("Hello"))
print("\t", "bool(15)\t=", bool(15))
"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
# false values
print("\n", "False Values:")
print("\t", "Any string is True, except empty strings")
print("\t", "Any number is True, except 0")
print("\t", "Any list, tuple, set, and dictionary are True, except empty ones")
print()
print("\t", "bool(False)", "\t=", bool(False))
print("\t", "bool(None)", "\t=", bool(None))
zero = 0
txt = "bool({})"
print("\t", txt.format(zero), "\t=", bool(None))
print("\t", "bool("")", "\t=", bool(""))
print("\t", "bool(())", "\t=", bool(()))
print("\t", "bool([])", "\t=", bool([]))
print("\t", "bool({})", "\t=", bool({}))

# object with a _len_ function
print("\n", "False Object with _len_ function:")
print("\t", "class myclass():")
print("\t\t", "def __len__(self):")
print("\t\t\t", "return 0")
print("\t", "myobj = myclass()")
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print("\t", "bool(myobj) = ", bool(myobj))

# returning a boolean
print("\n", "Returning a Boolean")
print("\t", "def returns_boolean() :")
print("\t\t", "return True")
def returns_boolean() :
  return True
print("\t", "returns_boolean() = ", returns_boolean())

# Boolean method checks
print("\n", "Boolean method checks:")
x = 200
txt = "x = {}"
print("\t", txt.format(x))
print("\t\t", "isinstance(x, int) = ", isinstance(x, int))
