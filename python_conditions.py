txt = """
Python Conditions and If Statements!!!

    see: https://www.w3schools.com/python/python_conditions.asp

Python supports the usual logical conditions from mathematics:

    Equals:                    a == b
    Not Equals:                a != b
    Less than:                 a < b
    Less than or equal to:     a <= b
    Greater than:              a > b
    Greater than or equal to:  a >= b
    
    These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
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

# IF
print(n, "IF - keyword")
txt = """
	 > the code
        
		 a = 200
                 b = 1
                 is_greater = False
             
                 if a > b:
                     is_greater = True

	 >>> result:
"""
print(txt)

a = 200
b = 1
is_greater = False

if a > b:
    is_greater = True
    
print(t2, "is_greater", "=", is_greater)

# ELIF
print(n, "ELIF - keyword")
txt = """
	 > the code
        
		 a = 33
                 b = 33
                 is_equal = False
             
                 if a > b:
                     is_equal = False
                 elif a == b:
                     is_equal = True

	 >>> result:
"""
print(txt)

a = 33
b = 33
is_equal = False

if b > a:
    is_equal = False
elif a == b:
    is_equal = True
    
print(t2, "is_equal =", is_greater)

# ELSE
print(n, "ELSE - keyword")
txt = """
	 > the code
        
		 a = 33
                 b = 33
                 is_equal = False
                 
                 if b > a:
                     is_equal = False
                 elif b < a:
                     is_equal = False
                 else:
                     is_equal = True

	 >>> result:
"""
print(txt)

a = 33
b = 33
is_equal = False

if b > a:
    is_equal = False
elif b < a:
    is_equal = False
else:
    is_equal = True

print(t2, "is_equal =", is_greater)

# Short-hand statements
print(n, "Short-hand if Statements")

    # IF - short-hand statement
print(n, t1, "> IF - short-hand statement")
txt = """
                 > the code
                 
			 a = 200
                         b = 1
                         is_greater = False
                     
                         if a > b: is_greater = True

                 >>> result:
"""
print(txt)

a = 200
b = 1
is_greater = False

if a > b: is_greater = True

print(t3, "is_greater =", is_greater)

    # IF_ELSE - short-hand statement
print(n, t1, "> IF...ELSE - short-hand statement")

txt = """
                 > the code
                     
                         a = 200
                         b = 1
                         
                         print("A") if a > b else print("B")

                 >>> result:
"""
print(txt)

a = 200
b = 1

print(t3, "A") if a > b else print(t3, "B")

    # IF...ELSE - short-hand statement w/ 3 conditions
print(n, t1, "> IF...ELSE - short-hand statement w/ 3 conditions")

txt = """
                 > the code
                     
                         a = 33
                         b = 33
                         
                         print("A") if a > b else print("a == b") if a == b else print("B")
                     
                 >>> result:
"""
print(txt)

a = 33
b = 33

print(t3, "A") if a > b else print(t3, "a == b") if a == b else print(t3, "B")

# AND - keyword
print(n, "AND keyword")

txt = """
	 > the code
             
                 a = 200
                 b = 33
                 c = 500

                 if a > b and c > a:
                     print("Both conditions are True")

	 >>> result:
"""
print(txt)

a = 200
b = 33
c = 500

if a > b and c > a:
    print(t2, "Both conditions are True")

# OR - keyword
print(n, "OR keyword")

txt = """
	 > the code
             
                 a = 200
                 b = 33
                 c = 500

                 if a > b or a > c:
                     print("At least one of the conditions is True")

	 >>> result:
"""
print(txt)

a = 200
b = 33
c = 500
if a > b or a > c:
    print(t2, "At least one of the conditions is True")

# Nested if - statements
print(n, "Nested if statements")

txt = """
	 > the code
             
                 a = 100

                 if x > 10:
                     print("Above ten,")
                     if x > 20:
                         print("and also above 20!")
                     else:
                         print("but not above 20.")

	 >>> result:
"""
print(txt)

x = 100

if x > 10:
    print(t2, "Above ten,")
    if x > 20:
        print(t2, "and also above 20!")
    else:
        print(t2, "but not above 20.")

# Pass - statements
print(n, "Pass statements")

txt = """
	 > the code
             
                 a = 33
                 b = 200

                 if b > a:
                     pass

	 >>> result:
"""
print(txt)

a = 33
b = 200

if b > a:
    pass
