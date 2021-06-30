# Basic syntax is
from module_name import object_name


from datetime import datetime # Imports class datetime from module datetime
print(datetime.now())

import math # imports the whole module
math.log(45) # to use the log function
from math import log # imports just the function we need
log(45) # to use the function


#Creating a list of random integers by using the
import random # module
random_list = [random.randint(0, 100) for element in range(0, 101)]

### TO FIND OUT ALL THE CLASSES IN A MODULE WE
### CAN USE PRINT(DIR(MODULE_NAME))

# We can import Python modules with an alias
import module_with_very_long_and_annoying_name as simplemath

### Will create a plot 
from matplotlib import pyplot as plt
import random
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()
