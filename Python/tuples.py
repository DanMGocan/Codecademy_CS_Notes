# Tuples are a way of storing data but, as opposed to LISTS, they are immutable and non-modifiable
my_info = ("Dan", 24, "Wanker") # Tuple
my_info[0] # outputs Dan
### We can interact with a tuple as we do with a list ### 

### Unpacking a tuple
name, age, occupation = my_info # stores data from Tuple into the variables

### One element tuple
one_element_tuple = (4, ) # without the comma, the 4 is an expression surrounded by paranthesis 