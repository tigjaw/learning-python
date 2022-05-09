txt = """
Python Strings!!!

    see: https://www.w3schools.com/python/python_strings.asp

Escape Characters:

    Escape Key      Description
     \'	            Single Quote
     \\	            Backslash
     \\n	    New Line
     \\r	    Carriage Return
     \\t	    Tab
     \\b	    Backspace
     \\f	    Form Feed
     \\ooo	    Octal value
     \\xhh	    Hex value


String Methods:

    All string methods returns new values. They do not change the original string
    
    see: https://www.w3schools.com/python/python_strings_methods.asp

    Method	            Description
     capitalize()	    Converts the first character to upper case
     casefold()	            Converts string into lower case
     center()	            Returns a centered string
     count()	            Returns the number of times a specified value occurs in a string
     encode()	            Returns an encoded version of the string
     endswith()	            Returns true if the string ends with the specified value
     expandtabs()	    Sets the tab size of the string
     find()	            Searches the string for a specified value and returns the position of where it was found
     format()	            Formats specified values in a string
     format_map()	    Formats specified values in a string
     index()	            Searches the string for a specified value and returns the position of where it was found
     isalnum()	            Returns True if all characters in the string are alphanumeric
     isalpha()	            Returns True if all characters in the string are in the alphabet
     isdecimal()	    Returns True if all characters in the string are decimals
     isdigit()	            Returns True if all characters in the string are digits
     isidentifier()	    Returns True if the string is an identifier
     islower()	            Returns True if all characters in the string are lower case
     isnumeric()	    Returns True if all characters in the string are numeric
     isprintable()	    Returns True if all characters in the string are printable
     isspace()	            Returns True if all characters in the string are whitespaces
     istitle()	            Returns True if the string follows the rules of a title
     isupper()	            Returns True if all characters in the string are upper case
     join()	            Joins the elements of an iterable to the end of the string
     ljust()	            Returns a left justified version of the string
     lower()	            Converts a string into lower case
     lstrip()	            Returns a left trim version of the string
     maketrans()	    Returns a translation table to be used in translations
     partition()	    Returns a tuple where the string is parted into three parts
     replace()	            Returns a string where a specified value is replaced with a specified value
     rfind()	            Searches the string for a specified value and returns the last position of where it was found
     rindex()	            Searches the string for a specified value and returns the last position of where it was found
     rjust()	            Returns a right justified version of the string
     rpartition()	    Returns a tuple where the string is parted into three parts
     rsplit()	            Splits the string at the specified separator, and returns a list
     rstrip()	            Returns a right trim version of the string
     split()	            Splits the string at the specified separator, and returns a list
     splitlines()	    Splits the string at line breaks and returns a list
     startswith()	    Returns true if the string starts with the specified value
     strip()	            Returns a trimmed version of the string
     swapcase()	            Swaps cases, lower case becomes upper case and vice versa
     title()	            Converts the first character of each word to upper case
     translate()	    Returns a translated string
     upper()	            Converts a string into upper case
     zfill()	            Fills the string with a specified number of 0 values at the beginning
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

# Hello World
hello_world = "HELLO, WORLD!"

print("hello_world =", hello_world)

# strings are arrays
print(n, "Strings are arrays")

txt = """
	 > code:

		 hello_world = "HELLO, WORLD!"

		 print(hello_world[0])

	 >>> result:
"""
print(txt)

print(t2, hello_world[0])

# loop through each character of the string
print(n, "Loop through String (array)", n)

txt = """
	 > code:

		 for x in hello_world:
                     print(x)

	 >>> result:
"""
print(txt)

for x in hello_world:
    print(t2, x)

# print string length
print(n, "Print String length via len(hello_world)")

txt = """
	 > code:

		 hello_world = "HELLO, WORLD!"

		 print(len(hello_world))

	 >>> result:
"""
print(txt)

print(t2, len(hello_world))

# use the keyword in to check if certain characters are present
print(n, "Check String with 'in' keyword")

txt = """
	 > code:

                 hello_world = "HELLO, WORLD!"

		 if "WORLD" in hello_world:
                     print("'WORLD' IS IN 'HELLO, WORLD!'")
                     
                 if "world" not in hello_world:
                     print("'world' IS NOT IN 'HELLO, WORLD!'")
                 
                 if "planet" not in hello_world:
                     print("'planet' IS NOT IN 'HELLO, WORLD!'")

	 >>> result:
"""
print(txt)

if "WORLD" in hello_world:
    print(t2, f"'WORLD' {t1} IS IN {t2} 'HELLO, WORLD!'")
if "world" not in hello_world:
    print(t2, f"'world'  {t1} IS IN {t2} 'HELLO, WORLD!'")
if "planet" not in hello_world:
    print(t2, f"'planet' {t1} IS NOT IN {t1} 'HELLO, WORLD!'")

# String Slicing
print(n, f"String slicing")

txt = """
	 > code:

                 hello_world = "HELLO, WORLD!"

                 # slicing from start

			 # index 2 (inc.) to index 5 (not inc.)
			 
			 print(hello_world[2:5])

                         # from start to index 5 (not inc.)
                         
                         print(hello_world[:5])

                         # from index 2 (inc.) to the end
                         
                         print(hello_world[2:])

                 # slicing from end

                         # from index -5 (inc.) to index -2 (not inc.)
                         
                         print(hello_world[-5:-2])

	 >>> result:
"""
print(txt)

print(t3, hello_world[2:5])
print(t3, hello_world[:5])
print(t3, hello_world[2:])
print(t3, hello_world[-5:-2])

# Modifying Strings
print(n, "Modifying Strings")

    # upper() and lower()
print(n, t1, "> Convert String to upper or lower case")

txt = """
                 > code:

                         lower_case = "lower"
                         upper_case = "UPPER"

                         lower_case.upper()
                         upper_case.lower()

                 >>> result:
"""
print(txt)

lower_case = "lower"
upper_case = "UPPER"

print(t3, lower_case.upper())
print(t3, upper_case.lower())

    # strip() method
print(n, t1, "> Strip white space")

txt = """
                 > code:

                         strip_me = " strip "

                         strip_me.strip()

                 >>> result:
"""
print(txt)

strip_me = " strip "

print(t3, "" + strip_me.strip())

    # replace() method
print(n, t1, "> Replace characters")

txt = """
                 > code:

                         replace_me = "this"

                         replace_me.replace('is', 'at')

                 >>> result:
"""
print(txt)

replace_me = "this"

print(t3, replace_me.replace('is', 'at'))

    # split() method
print(n, t1, "> Split string")

txt = """
                 > code:

                         split_me = "split_me"

                         split_me.split('_')

                 >>> result:
"""
print(txt)

split_me = "split_me"

print(t3, split_me.split('_'))

# String Concatenation
print(n, "String Concatenation")

  # output multiple variables, separated by a comma
print(t1, "> String concatenation with a comma")

txt = """
                 > code:

                         # doesn't require spaces at the end
                         
                         comma1 = "Concatenate"
                         comma2 = "with"
                         comma3 = "COMMA"
                         
                         print(comma1, comma2, comma3)

                 >>> result:
"""
print(txt)

comma1 = "Concatenate"
comma2 = "with"
comma3 = "COMMA"

print(t3, comma1, comma2, comma3)

  # output multiple variables, separated by a plus sign
print(n, t1, "> String concatenation with a comma")

txt = """
                 > code:

                         # requires spaces at the end
                         
                         plus1 = "Concatenate"
                         plus2 = "with"
                         plus3 = "PLUS"
                         
                         print(plus1, plus2, plus3)

                 >>> result:
"""
print(txt)

plus1 = "Concatenate"
plus2 = "with"
plus3 = "PLUS"

print(t3, plus1 + plus2 + plus3)

# Formatting Strings
print(n, "Formatting Strings")

txt = """
 	 > code:

                 name = "Joshua"
                 age = 12
                         
                 txt = "My name is {} and I am {}"

                 print(txt.format(name, age))

 	 >>> result:
"""
print(txt)

name = "Joshua"
age = 12
txt = "My name is {} and I am {}"

print(t2, txt.format(name, age))
