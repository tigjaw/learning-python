txt = """
Python Conditions and If Statements!!!

    see: https://www.w3schools.com/python/python_conditions.asp

Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.

    An "if statement" is written by using the if keyword.
"""
print(txt)

# IF
print("\n", "IF - keyword")
txt = """
	 > the code
        
             a = 200
             b = 1
             is_greater = False
             
             if a > b:
                 is_greater = True
"""
print(txt)
a = 200
b = 1
is_greater = False
if a > b:
    is_greater = True
print("\t", "> result:")
print()
print("\t\t", "is_greater", "=", is_greater)

# ELIF
print("\n", "ELIF - keyword")
txt = """
	 > the code
        
             a = 33
             b = 33
             is_equal = False
             
             if a > b:
                 is_equal = False
             elif a == b:
                 is_equal = True
"""
print(txt)
a = 33
b = 33
is_equal = False
if b > a:
    is_equal = False
elif a == b:
    is_equal = True
print("\t", "> result:")
print()
print("\t\t", "is_equal", "=", is_greater)

# ELSE
print("\n", "ELSE - keyword")
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
print("\t", "> result:")
print()
print("\t\t", "is_equal", "=", is_greater)

# Short-hand statements
print("\n", "Short-hand if Statements")
print()
    # IF - short-hand statement
print("\t", "> IF - short-hand statement")
txt = """
                 > the code
                 
                     a = 200
                     b = 1
                     is_greater = False
                     
                     if a > b: is_greater = True
"""
print(txt)
a = 200
b = 1
is_greater = False
if a > b: is_greater = True
print("\t\t", "> result:")
print()
print("\t\t\t", "is_greater", "=", is_greater)
print()
    # IF_ELSE - short-hand statement
print("\t", "> IF_ELSE - short-hand statement")
txt = """
                 > the code
                     
                     a = 200
                     b = 1
                         
                     print("A") if a > b else print("B")
"""
print(txt)
print("\t\t", "> result:")
print()
a = 200
b = 1
print("\t\t\t", "A") if a > b else print("\t\t\t", "B")
print()
    # IF...ELSE - short-hand statement w/ 3 conditions
print("\t", "> IF...ELSE - short-hand statement w/ 3 conditions")
txt = """
                 > the code
                     
                     a = 33
                     b = 33
                         
                     print("A") if a > b else print("a == b") if a == b else print("B")
"""
print(txt)
print("\t\t", "> result:")
print()
a = 33
b = 33
print("\t\t\t", "A") if a > b else print("\t\t\t", "a == b") if a == b else print("\t\t\t", "B")

# AND - keyword
print("\n", "AND - keyword")
txt = """
	 > the code
             
                 a = 200
                 b = 33
                 c = 500

                 if a > b and c > a:
                     print("Both conditions are True")
"""
print(txt)
print("\t", "> result:")
print()
a = 200
b = 33
c = 500
if a > b and c > a:
    print("\t\t", "Both conditions are True")

# OR - keyword
print("\n", "OR - keyword")
txt = """
	 > the code
             
                 a = 200
                 b = 33
                 c = 500

                 if a > b or a > c:
                     print("At least one of the conditions is True")
"""
print(txt)
print("\t", "> result:")
print()
a = 200
b = 33
c = 500
if a > b or a > c:
    print("\t\t", "At least one of the conditions is True")

# Nested if - statements
print("\n", "Nested If - Statements")
txt = """
	 > the code
             
                 a = 100

                 if x > 10:
                    print("Above ten,")
                        if x > 20:
                            print("and also above 20!")
                        else:
                            print("but not above 20.")
"""
print(txt)
print("\t", "> result:")
print()
x = 100
if x > 10:
    print("\t\t", "Above ten,")
    if x > 20:
        print("\t\t", "and also above 20!")
    else:
        print("\t\t", "but not above 20.")

# Pass - statements
print("\n", "Pass - Statements")
txt = """
	 > the code
             
                 a = 33
                 b = 200

                 if b > a:
                     pass
"""
a = 33
b = 200

if b > a:
    pass
