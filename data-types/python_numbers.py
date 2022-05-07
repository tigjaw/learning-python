txt = """
Python Numbers!!!

    see: https://www.w3schools.com/python/python_numbers.asp
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(n, "Number types: int, float, complex")
print(t1, "x = ", x, t1, type(x))
print(t1, "y = ", y, t1, type(y))
print(t1, "z = ", z, t1, type(z))

print(n, "Converting types")

# convert to complex:
a = complex(x)
print(t1, "converting to complex")
print(t2, "a = complex(x)")
print(t2, "a = ", a, t1, type(a))

# convert to int:
b = int(y)
print(t1, "converting to int")
print(t2, "b = int(y)")
print(t2, "b = ", b, t1, type(b))

# convert to float:
c = float(x)
print(t1, "converting to float")
print(t2, "c = float(x)")
print(t2, "c = ", c, t1, type(c))

print(n, t1, "converting from complex is not possible")

print(n, "Generating a random number between 1 and 10")
# python random module
import random

print(t1, random.randrange(1, 10))

X = int(1)   # x will be 1
Y = int(2.8) # y will be 2
Z = int("3") # z will be 3
