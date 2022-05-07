txt = """
Python Inheritance!!!

    see: https://www.w3schools.com/python/python_inheritance.asp

Inheritance allows us to define a class that inherits
all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class,
also called derived class.

__init__() Function:
    The __init__() function is called automatically every time the class
    is being used to create a new object.

    The child's __init__() function overrides the
    inheritance of the parent's __init__() function.

super() Function:
    Python also has a super() function that will make the child
    class inherit all the methods and properties from its parent.

    If you add a method in the child class with the same name as a
    function in the parent class,
    the inheritance of the parent method will be overridden.
"""
print(txt)

n, t1, t2, t3, t4 = "\n", "\t", "\t\t", "\t\t\t", "\t\t\t\t"

# Parent Class
print(n, "Parent Class")
txt = """
	 > create a parent class
	 
             class Person:
                 def __init__(self, first_name, last_name):
                     self.first_name = first_name
                     self.last_name = last_name

                 def print_name(self):
                     print(self.first_name, self.last_name)

             person = Person("Parent", "Class")
             person.print_name()
"""
print(txt)

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(t1, f">>> result: {self.first_name} {self.last_name}")

person = Person("Parent", "Class")
person.print_name()

# Child Class
print(n, "Child Class")
txt = """
	 > create a child class
	 
             class Student(Person):
                 pass

             student = Student("Student", "Class")
             student.print_name()
"""
print(txt)

class Student(Person):
    pass

student = Student("Student", "Class")
student.print_name()

# __init__() Function
print(n, "__init__() Function")
txt = """
	 > don't inherit parent's __init__() function
	 
             class Student(Person):
                 def __init__(self, first_name, last_name):
                     pass
                 
             student = Student("Don't", "Inherit")
             student.print_name()
"""
print(txt)

class Student(Person):
    def __init__(student, first_name, last_name):
        pass

student = Student("Don't", "Inherit")
print(t1, f">>> AttributeError: 'Student' object has no attribute 'first_name'")

txt = """
	 > inherit parent's __init__() function
	 
             class Student(Person):
                 def __init__(self, first_name, last_name):
                     Person.__init__(self, first_name, last_name)
                     
             student = Student("Do", "Inherit")
             student.print_name()
"""
print(txt)

class Student(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

student = Student("Do", "Inherit")
student.print_name()

# super() Function
print(n, "super() Function")
txt = """
	 > super() inherits all methods and properties
	 
             class Student(Person):
                 def __init__(self, first_name, last_name):
                     super().__init__(first_name, last_name)

             student = Student("Super", "Function")
             student.print_name()
"""
print(txt)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

student = Student("Super", "Function")
student.print_name()
