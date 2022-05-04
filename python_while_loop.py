txt = """
Python While Loops!!!

    see: https://www.w3schools.com/python/python_while_loops.asp

Python Loops:
  Python has two primitive loop commands:

  while loops
  for loops

The While Loop:
  With the while loop we can execute a set of statements
  as long as a condition is true.

  The while loop requires relevant variables to be ready,
  in this example we need to define an indexing variable,
  i, which we set to 1.
"""

print(txt)

# Whlie
print("", "While")
txt = """
	 > code:
                 
             i = 1
             txt = ""
             
             while i < 6:
                 txt = txt + str(i) + " "
                 i += 1
                 
             print(txt)
"""
print(txt)
i = 1
txt = ""
while i < 6:
  txt = txt + str(i) + " "
  i += 1
print("\t", "> result:", txt)
print()

# Break
print("", "Break")
txt = """
	 > code:
	 
             i = 1
             txt = ""
             
             while i < 6:
                 txt = txt + str(i) + " "
                 if i == 3:
                     break
                 i += 1
                 
             print(txt)
"""
print(txt)
i = 1
txt = ""
while i < 6:
  txt = txt + str(i) + " "
  if i == 3:
    break
  i += 1
print("\t", "> result:", txt)
print()

# Continue
print("", "Continue")
txt = """
	 > code:
	 
             i = 1
             txt = ""
             
             while i < 6:
                 txt = txt + str(i) + " "
                 if i == 3:
                     continue
                 i += 1
                 
             print(txt)
"""
print(txt)
i = 0
txt = ""
while i < 6:
  i += 1
  if i == 3:
    continue
  txt = txt + str(i) + " "
print("\t", "> result:", txt)
print()

# Else
print("", "Else")
txt = """
	 > code:
	 
             i = 1
             txt = ""
             
             while i < 6:
                 txt = txt + str(i) + " "
                 if i == 3:
             else:
                 txt = txt + " - i is no longer less than 6"
             print(txt)
"""
print(txt)
i = 1
txt = ""
while i < 6:
  txt = txt + str(i) + " "
  i += 1
else:
  txt = txt + "(i is no longer less than 6)"
print("\t", "> result:", txt)
print()
