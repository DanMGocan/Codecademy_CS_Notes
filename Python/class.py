print(type(5)) # int
my_dict = {}
my_list = []
print(type(my_dict)) # dict
print(type(my_list)) # list

class ClassName:
    def __init__(self, phrase):
        print(phrase)

    pass # we put pass here to mark it as an empty class and not get an Indentation Error
    test_variable = "class variable" # this is available to all instances
    def method_test(self):
        print(self.test_variable)

cool_instance = ClassName() # this is an instance of the ClassName class
# a class instance is called an Object
cool_instance.test_variable # "class variable"

type(cool_instance) # <class "__main__.CoolClass">
# main here means that the class is defined in here

# Methods # 
# Methods inside classes are always called with the object calling the method as a first argument
cool_instance.method_test

### CONSTRUCTORS ###
__function__ # <= this is a special / magic / dunder method
cool_instance_2 = ClassName("Greetings!")
# Greetings is passed to the __init__ method, which is the constructor
# As a general rule is is best to initiate all class variables in the constructor method