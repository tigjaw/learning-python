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

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Syntax
print(n, "Lambda Syntax")
  # add 10 to argument a, and return the result
print(t1, "> add 10 to argument a")
txt = """
		 x = lambda a : a + 10
                     print("x =", x(5))
"""
print(txt)
x = lambda a : a + 10
print(t2, "x =", x(5))
  # any number of arguments
print(t1, "> using multiple arguments")
txt = """
		 x = lambda a, b : a * b
                     print("x =", x(5, 6))
"""
print(txt)
x = lambda a, b : a * b
print(t2, "x =", x(5, 6))

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
"""
print(txt)
def lambda_function(n):
    return lambda a : a * n

double_this = lambda_function(2)
triple_this = lambda_function(3)

print(t1, "> result:")
print(t2, double_this(11))
print(t2, triple_this(11))
