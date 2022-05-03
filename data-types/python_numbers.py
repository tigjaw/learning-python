txt = """
Python Numbers!!!

    see: https://www.w3schools.com/python/python_numbers.asp
"""

print(txt)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print("", "Number types: int, float, complex")
print("\t", "x = ", x, "\t", type(x))
print("\t", "y = ", y, "\t", type(y))
print("\t", "z = ", z, "\t", type(z))

print("\n", "Converting types")

# convert to complex:
a = complex(x)
print("\t", "converting to complex")
print("\t\t", "a = complex(x)")
print("\t\t", "a = ", a, "\t", type(a))

# convert to int:
b = int(y)
print("\t", "converting to int")
print("\t\t", "b = int(y)")
print("\t\t", "b = ", b, "\t", type(b))

# convert to float:
c = float(x)
print("\t", "converting to float")
print("\t\t", "c = float(x)")
print("\t\t", "c = ", c, "\t", type(c))

print("\n\t", "converting from complex is not possible")

print("\n", "Generating a random number between 1 and 10")
# python random module
import random

print("\t", random.randrange(1, 10))

X = int(1)   # x will be 1
Y = int(2.8) # y will be 2
Z = int("3") # z will be 3
