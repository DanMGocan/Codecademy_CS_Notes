# Lists have methods

# Adds a single element to a list
listExample = [3, 4, 5, "Pepe"] 
listExample.append("Madona")
print(listExample)

# To add more than an element we can concatenate lists
listExample + ["To concatenate one element, it needs square brackets"]
concatExample = listExample + ["Test1", 4, False, 3, 54, "Pisica", False, True, 5, 5, 5] # The original list is not changed

# To insert items into a list, by index
listExample.insert(2, "ElementToBeInserter") # inserts element at index 2
# shifts all indexes / elements to the right

# To remove element at specific index
listExample.pop(3) # Takes an optional argument, the index to be removed. With no argument, removes last element
removedElement = listExample.pop(3) # Optional, you can save the removed value

### Consecutive lists
my_range = range(10) # creates a range OBJECT of consecutive numbers, from 0 to 9 (argument - 1)
my_specific_range = range (2, 12) # creates a range from 2 to 12, when called with two arguments
my_even_range = range(2, 12, 2) # will create a range from 2 to 12, skipping every second number [2, 4, 6, 8, 10]
my_list = list(my_range) # converts the range objects to a list of consecutive numbers

# We can use len() to find out the lenght of a list
listLen = len(listExample) # will output length of listExample
len(my_range) # will work, ranges don't have to be converted into lists to be read

### Slicing lists
sliced_list = listExample[1:5] # where 1 is the index we start at and 5 is the index we end at [it needs to be one HIGHER]
listExample[:5] # selects the first 4 elements of the list
listExample[-3:] # selects the last 3 elements of the list
listExample[:-2] # selects all but the last 2 elements of the list

# Count inside a list
timesOfFive = listExample.count(5) # will count occurences of five

# Sorting lists
listExample.sort() # will sort our list
listExample.sort(reverse=True) # will sort our list reversely(???)
# It modifies the list directly, so it mustn't be saved in a new variable
sorted_list = sorted(listExample) # creates a sorted copy of the list MAINTAINING THE ORIGINAL
# A two dimenstional list is sorted by the first element of the each individual list