txt = """
Python Iterators!!!

    see: https://www.w3schools.com/python/python_iterators.asp

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon,
meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which
implements the iterator protocol, which consist of the methods
__iter__() and __next__().

Iterator vs Iterable:
    Lists, tuples, dictionaries, and sets are all iterable objects.
    They are iterable containers which you can get an iterator from.

    All these objects have a iter() method which is used to get an iterator

    Even strings are iterable objects, and can return an iterator.

    We can also use a for loop to iterate through an iterable object.

Create an Iterator:
    To create an object/class as an iterator you have to implement the
    methods __iter__() and __next__() to your object.

    All classes have a function called __init__(),
    which allows you to do some initializing when the object is being created.

    The __iter__() method acts similar, you can do operations (initializing etc.),
    but must always return the iterator object itself.

    The __next__() method also allows you to do operations,
    and must return the next item in the sequence.

StopIteration:
    To prevent the iteration to go on forever,
    we can use the StopIteration statement.

    In the __next__() method, we can add a terminating condition to raise an error
    if the iteration is done a specified number of times
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

# Iterator vs Iterable
print(n, "Iterator vs Iterable")
txt = """
	 > code:
            
                 mu_tuple = ("apple", "banana", "cherry")
                 my_iterator = iter(mu_tuple)

                 print(next(my_iterator))
		 print(next(my_iterator))
		 print(next(my_iterator))
		 
	 >>> result:
"""
print(txt)

mu_tuple = ("apple", "banana", "cherry")
my_iterator = iter(mu_tuple)

print(t2, next(my_iterator))
print(t2, next(my_iterator))
print(t2, next(my_iterator))

# String Iterator
print(n, "String Iterator")
txt = """
	 > code:
            
                 my_string = "abc"
                 my_iterator = iter(my_string)

                 print(next(my_iterator))
		 print(next(my_iterator))
		 print(next(my_iterator))

	 >>> result:
"""
print(txt)

my_string = "abc"
my_iterator = iter(my_string)

print(t2, next(my_iterator))
print(t2, next(my_iterator))
print(t2, next(my_iterator))

# Create an Iterator
print(n, "Create an Iterator")
txt = """
	 > code:
        
                 class MyNumbers:
                     def __iter__(self):
                         self.a = 1
                         return self

                     def __next__(self):
                         x = self.a
                         self.a += 1
                         return x

                 myclass = MyNumbers()
                 myiter = iter(myclass)

                 print(next(myiter))
                 print(next(myiter))
                 print(next(myiter))

	 >>> result:
"""
print(txt)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(t2, next(myiter))
print(t2, next(myiter))
print(t2, next(myiter))

# StopIteration
print(n, "StopIteration")
txt = """
	 > code:
	 
		 class MyNumbers:
                     def __iter__(self):
                         self.a = 1
                         return self

                     def __next__(self):
                         if self.a <= 3:
                             x = self.a
                             self.a += 1
                         return x
                         else:
                             raise StopIteration

                     myclass = MyNumbers()
                     myiter = iter(myclass)

                     for x in myiter:
                         print(x)

	 >>> result:
"""
print(txt)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(t2, x)
