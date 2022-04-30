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

# convert from int to complex:
a = complex(x)
print("\t", "converting from int to complex")

# convert from float to int:
b = int(y)
print("\t", "converting from float to int")

# convert from complex to float:
c = float(x)
print("\t", "converting from complex to float")

print("\t", "a = ", a, "\t", type(a))
print("\t", "b = ", b, "\t", type(b))
print("\t", "c = ", c, "\t", type(c))

print("\n", "Generating a random number between 1 and 10")
# python random module
import random

print("\t", random.randrange(1, 10))

X = int(1)   # x will be 1
Y = int(2.8) # y will be 2
Z = int("3") # z will be 3
