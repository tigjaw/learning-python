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

# use for formatting code
n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# use for formatting snippets
"""
	 tab1
		 tab2
			 tab3
				 tab4
"""

# While
print(n, "While")

txt = """
	 > code:
                 
		 i = 1
                 txt = ""
             
                 while i < 6:
                     txt = txt + str(i) + " "
                     i += 1
                 
                 print(txt)

	 >>> result:
"""
print(txt)

i = 1
txt = ""

while i < 6:
  txt = txt + str(i) + " "
  i += 1

print(t2, txt)

# Break
print(n, "Break")

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

	 >>> result:
"""
print(txt)

i = 1
txt = ""

while i < 6:
  txt = txt + str(i) + " "
  if i == 3:
    break
  i += 1

print(t2, txt)

# Continue
print(n, "Continue")

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

	 >>> result:
"""
print(txt)

i = 0
txt = ""

while i < 6:
  i += 1
  if i == 3:
    continue
  txt = txt + str(i) + " "

print(t2, txt)

# Else
print(n, "Else")

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

	 >>> result:
"""

print(txt)

i = 1
txt = ""
while i < 6:
  txt = txt + str(i) + " "
  i += 1
else:
  txt = txt + "(i is no longer less than 6)"

print(t2, txt)
