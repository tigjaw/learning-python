txt = """
Python Lambda!!!

    see: https://www.w3schools.com/python/python_lambda.asp

A lambda function is a small anonymous function.

A lambda function can take any number of arguments,
but can only have one expression.

Syntax
    lambda arguments : expression
    The expression is executed and the result is returned

Why Use Lambda Functions?
    The power of lambda is better shown when you use them as
    an anonymous function inside another function.
    Use lambda functions when an anonymous function
    is required for a short period of time.
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

# Syntax
print(n, "Lambda Syntax")

  # add 10 to argument a, and return the result
print(n, t1, "> add 10 to argument a")

txt = """
		 > code
	 
			 x = lambda a : a + 10
			 
                         print(x(5))

		 >>> result:
"""
print(txt)

x = lambda a : a + 10
print(t3, "x =", x(5))

  # any number of arguments
print(n, t1, "> using multiple arguments")

txt = """
		 > code
	 
			 x = lambda a, b : a * b
			 
                         print(x(5, 6))

		 >>> result:
"""
print(txt)

x = lambda a, b : a * b
print(t3, "x =", x(5, 6))

# Lambda Functions
print(n, "Lambda Functions")

txt = """
	 > code
	 
                 def lambda_function(n):
                     return lambda a : a * n

                 double_this = lambda_function(2)
                 triple_this = lambda_function(3)

                 print(double_this(11))
                 print(triple_this(11))

	 >>> result:
"""
print(txt)

def lambda_function(n):
    return lambda a : a * n

double_this = lambda_function(2)
triple_this = lambda_function(3)

print(t2, double_this(11))
print(t2, triple_this(11))
