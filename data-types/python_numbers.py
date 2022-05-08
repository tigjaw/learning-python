txt = """
Python Numbers!!!

    see: https://www.w3schools.com/python/python_numbers.asp
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

# Number types
print(n, "Number types: int, float, complex")

txt = f"""
	 x {t1}= 1
         y {t1}= 2.8
         z {t1}= 1j
	 
"""
print(txt)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(t1, f"x {t1}= ", type(x))
print(t1, f"y {t1}= ", type(y))
print(t1, f"z {t1}= ", type(z))

# Converting Types
print(n, "Converting types")

    # Convert to complex:
print(n, t1, "Convert to complex")

txt = f"""
                 > code:
                 
			 x {t2}= 1
			 a {t2}= complex(x)
		 
		 >>> result:
"""
print(txt)

a = complex(x)

print(t3, f"a {t2}= ", a)
print(t3, f"type(a) {t1}= ", type(a))

    # Convert to int:
print(n, t1, "Convert to int")

txt = f"""
                 > code:
                 
			 y {t2}= 2.8
			 b {t2}= int(y)
		 
		 >>> result:
"""
print(txt)

b = int(y)

print(t3, f"b {t2}= ", b)
print(t3, f"type(b) {t1}= ", type(b))

    # Convert to float:
print(n, t1, "Convert to float")

txt = f"""
                 > code:
                 
			 x {t2}= 1
			 c {t2}= float(x)
		 
		 >>> result:
"""
print(txt)

c = float(x)

print(t3, f"c {t2}= ", c)
print(t3, f"type(c) {t1}= ", type(c))

    # Convert from Complex
print(n, t1, "Converting from complex is not possible")

# Random module
print(n, "Random module")

txt = f"""
	 > code:
	 
                 # generating a random number between 1 and 10
                 
                 import random
                 
                 random.randrange(1, 10)
		 
	 >>> result:
"""
print(txt)

import random

print(t2, random.randrange(1, 10))
