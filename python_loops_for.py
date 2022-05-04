txt = """
Python While Loops!!!

    see: https://www.w3schools.com/python/python_for_loops.asp

Python Loops:
  Python has two primitive loop commands:

  while loops
  for loops

Python For Loops
  A for loop is used for iterating over a sequence
  (that is either a list, a tuple, a dictionary, a set, or a string).

  This is less like the for keyword in other programming languages,
  and works more like an iterator method as found in
  other object-orientated programming languages.

  With the for loop we can execute a set of statements,
  once for each item in a list, tuple, set etc.

  The for loop does not require an indexing variable to set beforehand.

The range() Function
  To loop through a set of code a specified number of times,
  we can use the range() function,
  The range() function returns a sequence of numbers,
  starting from 0 by default, and increments by 1 (by default),
  and ends at a specified number.
"""

print(txt)

# For
print("", "For")
txt = """
	 > code:
                     
                 fruits = ["apple", "banana", "cherry"]
                 txt = ""
                 
                 for x in fruits:
                     txt = "" + x + " "
                     
                 print(txt)
"""
print(txt)

fruits = ["apple", "banana", "cherry"]
txt = ""
for x in fruits:
  txt = txt + x + " "

print("\t", "> result:", txt)
print()

# Looping Through a String
print("", "Looping Through a String")
txt = """
	 > code:
             
                 txt = ""
                 
                 for x in "banana":
                     txt = txt + x + " "
                     
                 print(txt)
"""
print(txt)

txt = ""

for x in "banana":
  txt = txt + x + " "

print("\t", "> result:", txt)
print()

# Break
print("", "Break")
txt = """
	 > code:
	 
                 fruits = ["apple", "banana", "cherry"]
                 txt = ""
                 
                 for x in fruits:
                     txt = txt + str(i) + " "
                     if x == "banana":
                         break
                     
                 print(txt)
"""
print(txt)

fruits = ["apple", "banana", "cherry"]
txt = ""
for x in fruits:
  txt = txt + x + " "
  if x == "banana":
    break

print("\t", "> result:", txt)
print()

# Continue
print("", "Continue")
txt = """
	 > code:
	 
                 fruits = ["apple", "banana", "cherry"]
                 txt = ""
                 
                 for x in fruits:
                     if x == "banana":
                         continue
                     txt = txt + x + " "
                 
                 print(txt)
"""
print(txt)

fruits = ["apple", "banana", "cherry"]
txt = ""
for x in fruits:
  if x == "banana":
    continue
  txt = txt + x + " "

print("\t", "> result:", txt)
print()

# Range
print("", "Range")
  # Range
print("\t", "> Basic Range")
txt = """
		 > code:
                         
                         txt = ""
                         
                         for x in range(6):
                             txt = txt + str(x) + " "
                             
                         print(txt)
"""
print(txt)

txt = ""

for x in range(6):
  txt = txt + str(x) + " "

print("\t\t", "> result:", txt)
print()
  # Range with starting point
print("\t", "> Range with starting point")
txt = """
		 > code:
                     
                         txt = ""
                         
                         for x in range(2, 6):
                             txt = txt + str(x) + " "
                             
                         print(txt)
"""
print(txt)

txt = ""

for x in range(2, 6):
  txt = txt + str(x) + " "

print("\t\t", "> result:", txt)
print()
  # Range with increment
print("\t", "> Range with increment")
txt = """
		 > code:
                     
                         txt = ""
                         
                         for x in range(2, 30, 3):
                             txt = txt + str(x) + " "
                             
                         print(txt)
"""
print(txt)

txt = ""

for x in range(2, 30, 3):
  txt = txt + str(x) + " "

print("\t\t", "> result:", txt)
print()

# Else
print("", "Else")
txt = """
	 > code:
	 
                 fruits = ["apple", "banana", "cherry"]
                 txt = ""
                 
                 for x in range(6):
                     txt = txt + str(x) + " "
                 else:
                     txt += "(finally finished)"
                 
                 print(txt)
"""
print(txt)

fruits = ["apple", "banana", "cherry"]
txt = ""
for x in range(6):
  txt = txt + str(x) + " "
else:
  txt += "(finally finished)"

print("\t", "> result:", txt)
print()

# Nested Loops
print("", "Nested Loops")
txt = """
	 > code:
	 
                 adj = ["red", "big", "tasty"]
                 fruits = ["apple", "banana", "cherry"]
                 
                 for x in adj:
                     for y in fruits:
                         print(x, y)
                 
                 print(txt)
"""
print(txt)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
print("\t", "> result:")

for x in adj:
  for y in fruits:
    print("\t\t", x,y)


print()
