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

### EXCEPTIONS ###
issubclass("first_argument", "second_argument")
# returns True if first_arg is a subclass of the second_arg
# if either are not classes will throw a TypeError 