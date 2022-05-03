txt = """
Python Data Types!!!

    see: https://www.w3schools.com/python/python_datatypes.asp

Variable name must start with a letter or the underscore character
Variable name cannot start with a number
Variable name can only contain (A-z, 0-9, and _ )
Variable names are case-sensitive

List:
    Text            str
    Numeric	    int, float, complex
    Sequence	    list, tuple, range
    Mapping	    dict
    Set             set, frozenset
    Boolean         bool
    Binary          bytes, bytearray, memoryview
"""

print(txt)

x = "Hello World"	                        # str
x = 20	                                        # int
x = 20.5	                                # float
x = 1j	                                        # complex
x = ["apple", "banana", "cherry"]               # list
x = ("apple", "banana", "cherry")               # tuple
x = range(6)	                                # range
x = {"name" : "John", "age" : 36}               # dict
x = {"apple", "banana", "cherry"}               # set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	                                # bool
x = b"Hello"	                                # bytes
x = bytearray(5)	                        # bytearray
x = memoryview(bytes(5))	                # memoryview

x = str("Hello World")	                        # str
x = int(20)	                                # int
x = float(20.5)	                                # float
x = complex(1j)                                 # complex
x = list(("apple", "banana", "cherry"))         # list
x = tuple(("apple", "banana", "cherry"))        # tuple
x = range(6)	                                # range
x = dict(name="John", age=36)	                # dict
x = set(("apple", "banana", "cherry"))	        # set
x = frozenset(("apple", "banana", "cherry"))	# frozenset
x = bool(5)                                     # bool
x = bytes(5)	                                # bytes
x = bytearray(5)	                        # bytearray
x = memoryview(bytes(5))	                # memoryview

txt = """Usage:
    x = "Hello World"	                            # str
    x = 20	                                    # int
    x = 20.5	                                    # float
    x = 1j	                                    # complex
    x = ["apple", "banana", "cherry"]               # list
    x = ("apple", "banana", "cherry")               # tuple
    x = range(6)	                            # range
    x = {"name" : "John", "age" : 36}               # dict
    x = {"apple", "banana", "cherry"}               # set
    x = frozenset({"apple", "banana", "cherry"})    # frozenset
    x = True	                                    # bool
    x = b"Hello"	                            # bytes
    x = bytearray(5)	                            # bytearray
    x = memoryview(bytes(5))	                    # memoryview

    x = str("Hello World")	                    # str
    x = int(20)	                                    # int
    x = float(20.5)	                            # float
    x = complex(1j)                                 # complex
    x = list(("apple", "banana", "cherry"))         # list
    x = tuple(("apple", "banana", "cherry"))        # tuple
    x = range(6)	                            # range
    x = dict(name="John", age=36)	            # dict
    x = set(("apple", "banana", "cherry"))	    # set
    x = frozenset(("apple", "banana", "cherry"))    # frozenset
    x = bool(5)                                     # bool
    x = bytes(5)	                            # bytes
    x = bytearray(5)	                            # bytearray
    x = memoryview(bytes(5))	                    # memoryview
"""
print(txt)
