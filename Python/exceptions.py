# This is an example demonstrating how handy it is
# to have exception classes inheriting properties
# from one another. 

# Defining the exceptions
class KitchenException(Exception): # class kitchen inherits from class exceptions
  """
  Exception that gets thrown when a kitchen appliance isn't working
  """

class MicrowaveException(KitchenException): # inherits from KitchenExceptions
  """
  Exception for when the microwave stops working
  """
 
class RefrigeratorException(KitchenException):
  """
  Exception for when the refrigerator stops working
  """

# Take food from fridge
def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException # if refrigerator is not working, raise exception
  else:
    return food
 
 # Try to heat food
def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException # if microwave not working, raise exception
  else:
    microwave.cook(food)
    return food
 
try: # try both food processing functions, if both work and throw no exceptions, eat
  food = get_food_from_fridge()
  food = heat_food(food)
except: 
  KitchenException: # if any of the exceptions is raised, order takeout
  food = order_takeout()