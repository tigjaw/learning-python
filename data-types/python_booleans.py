txt = """
Python Booleans!!!

    see: https://www.w3schools.com/python/python_booleans.asp

In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python,
and get one of two answers, True or False.

When you compare two values, the expression is evaluated
and Python returns the Boolean answer.

Most Values are True
  Almost any value is evaluated to True if it has some sort of content.

  - Any string is True, except empty strings.
  - Any number is True, except 0.
  - Any list, tuple, set, and dictionary are True, except empty ones.
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

# Comparing and printing expressions
print(n, "Comparing and printing results", n)

print(t1, f"10 > 9 {t1}=", 10 > 9)
print(t1, f"10 == 9 {t1}=", 10 == 9)
print(t1, f"10 < 9 {t1}=", 10 < 9)

# evaluate values and variables
print(n, "Evaluating Values and Variables", n)

print(t1, f"bool('Hello'){t1}=", bool("Hello"))
print(t1, f"bool(15){t1}=", bool(15))

# false values
print(n, "False Values:", n)

print(t1, "bool(False)", f"{t1}=", bool(False))
print(t1, "bool(None)", f"{t1}=", bool(None))
print(t1, "bool(0)", f"{t1}=", bool(0))
print(t1, "bool("")", f"{t1}=", bool(""))
print(t1, "bool(())", f"{t1}=", bool(()))
print(t1, "bool([])", f"{t1}=", bool([]))
print(t1, "bool({})", f"{t1}=", bool({}))

# object with a _len_ function
print(n, "False Object with _len_ function:")

txt = """
	 > code:
	 
		 class myclass():
		 
                     def __len__(self):
                         return 0
                         
		 myobj = myclass()
		 bool(myobj)

	 >>> result:
"""
print(txt)

class myclass():
  def __len__(self):
    return 0
  
myobj = myclass()

print(t2, "bool(myobj) = ", bool(myobj))

# returning a boolean
print(n, "Returning a Boolean")

txt = """
	 > code:
	 
		 def returns_boolean() :
                     return True
                         
		 returns_boolean()

	 >>> result:
"""
print(txt)

def returns_boolean() :
  return True

print(t2, "returns_boolean() = ", returns_boolean())

# Boolean method checks
print(n, "Boolean method checks:")

txt = """
	 > code:
	 
		 x   = 200
                         
		 isinstance(x, int)

	 >>> result:
"""
print(txt)

x = 200

print(t2, "isinstance(x, int) = ", isinstance(x, int))
