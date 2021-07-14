# In order to "present" a class / instance
# we can use the __repr__ method

# Inheritance is passing properties from
# one source class (parent class) to 
# children classes

class User:
    is_admin = False
    def __init__(self):
        self.username = "Potato Man"
    

class Admin(User):
    is_admin = True
# In this example, Admin class will inherit all the properties of
# User class while overwriting the is_admin property

### EXCEPTIONS (please see exceptions.py for details) ###
issubclass("first_argument", "second_argument")
# returns True if first_arg is a subclass of the second_arg
# if either are not classes will throw a TypeError 

# Overriding methods #
class Person:
    def __init__(self, age):
        self.age = age

    def is_human(self):
        print("This person belongs to the human species and is of {}".format(self.age))

class Alien(Person):
    def is_human(self):
        return False 

et = Alien()
et.is_human() # will return False as the is_human method is overwritten

### super() method
# can be called to invoke / use a method of a parent class

class Immigrant(Person):
    def is_human(self):
        print("This person was born in a different country")
        super().is_human()

daniel = Immigrant(45)
daniel.is_human
### ^ I've no clue of what in the fuck is this ##

### DUNDER METHODS ### 

def __init__(): pass #is a dunder method
def __repr__(): pass #is also a dunder method

def __add__():
    pass 