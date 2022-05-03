txt = """
Python Strings!!!

    see: https://www.w3schools.com/python/python_strings.asp

Escape Characters:
\'	Single Quote
\\	Backslash
\\n	New Line
\\r	Carriage Return
\\t	Tab
\\b	Backspace
\\f	Form Feed
\\ooo	Octal value
\\xhh	Hex value
"""

print(txt)

# Hello World
hello_world = "HELLO, WORLD!"
print("hello_world =", hello_world)

# strings are arrays
print("\t", "Strings are arrays, so hello_world[0] =", hello_world[0])

# loop through each character of the string
print("\n", "Loop through String (array)")
for x in hello_world:
    print("\t", x)

# print string length
print("\n", "Print String length via len(hello_world)")
print("\t", len(hello_world))

# use the keyword in to check if certain characters are present
print("\n", "Check String with 'in' keyword")
if "world" in hello_world:
    print("\t", "'world'", "\tIS IN\t\t", "'HELLO, WORLD!'")
if "WORLD" in hello_world:
    print("\t", "'WORLD'", "\tIS IN\t\t", "'HELLO, WORLD!'")
if "planet" not in hello_world:
    print("\t", "'planet'", "\tIS NOT IN\t", "'HELLO, WORLD!'")

# String Slicing
print("\n", "String slicing from start of", "\t'" + hello_world + "'")
print("\t", "hello_world[2:5]\t:", "index 2 (inc.) to index 5 (not inc.)")
print("\t\t", hello_world[2:5])
print("\t", "hello_world[:5]\t:", "from start to index 5 (not inc.)")
print("\t\t", hello_world[:5])
print("\t", "hello_world[2:]\t:", "from index 2 (inc.) to the end")
print("\t\t", hello_world[2:])

print("\n", "String slicing from end of", "\t'" + hello_world + "'")
print("\t", "hello_world[-5:-2]\t:", "from index -5 (inc.) to index -2 (not inc.)")
print("\t\t", hello_world[-5:-2])

# Modifying Strings
print("\n", "Modifying Strings")
# Convert String to upper or lower case
lower_case = "lower"
upper_case = "UPPER"
print("\t", "lower_case =", lower_case)
print("\t\t", "lower_case.upper() =", lower_case.upper())
print("\t", "upper_case =", upper_case)
print("\t\t", "upper_case.lower() =", upper_case.lower())

# Removing Whitespace from start and end of String with strip() method
strip_me = " strip "
print("\t", "strip_me = '" + strip_me + "'")
print("\t\t", "strip_me.strip() = '" + strip_me.strip() + "'")

# Replacing parts of a String with another with replace() method
replace_me = "this"
print("\t", "replace_me = '" + replace_me + "'")
print("\t\t", "replace_me.replace('is', 'at')")
print("\t\t", "replace_me = '" + replace_me.replace('is', 'at') + "'")

# Split String with split() method
split_me = "split_me"
print("\t", "split_me = '" + split_me + "'")
print("\t\t", "split_me.split('_') returns ", split_me.split('_'))

# String Concatenation
print("\n", "String Concatenation")
  # output multiple variables, separated by a comma
print("\t", "> String concatenation with a comma")
comma1 = "Concatenate" # doesn't require spaces
comma2 = "with"
comma3 = "a COMMA"
txt = """
                 comma1 = "Concatenate" # doesn't require spaces
                 comma2 = "with"
                 comma3 = "a COMMA"
                 print(comma1, comma2, comma3)
"""
print(txt)
print("\t\t\t", "result :", comma1, comma2, comma3)
print()
  # output multiple variables, separated by a plus sign
print("\t", "> String concatenation with a comma")
plus1 = "Concatenate " # must add spaces
plus2 = "with "
plus3 = "a PLUS"
txt = """
                 plus1 = "Concatenate " # must add spaces
                 plus2 = "with "
                 plus3 = "a PLUS"
                 print(comma1, comma2, comma3)
"""
print(txt)
print("\t\t\t", "result :", plus1 + plus2 + plus3)
print()

# Formatting Strings
print("\n", "Formatting Strings")
age = 12
age_text = "age = {}"
txt = "My name is Joshua and I am {}"
print("\t", "age = '"+ age_text.format(age) +"', txt = '"+ txt +"'")
print("\t\t", "txt.format(age) = '"+ txt.format(age) +"'")

print()

item_id = 320
price = 49.95
quantity = 3
txt = "item_id = {}, price = {}, quantity = {}"
print("\t", txt.format(item_id, price, quantity))
my_order = "I want to pay £{2} for {0} pieces of item {1}"
print("\t", "my_order = '"+ my_order +"'")
print("\t\t", "my_order.format(quantity, item_id, price)")
print("\t\t\t", "'"+ my_order.format(quantity, item_id, price) +"'")

# String Methods
"""
All string methods returns new values. They do not change the original string
https://www.w3schools.com/python/python_strings_methods.asp

Method	            Description
capitalize()	    Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
"""
