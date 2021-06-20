# zip() can be used to combine two sets of data

names = ["Dan", "Maria", "Gibilan", "Vasile"]
heights = [179, 163, 201, 174]

names_and_heights = zip(names, heights)
### ^^^ This will convert the two lists in a ZIP OBJECTS which points towards memory location 

converted_list = list(names_and_heights)
### ^^^ This will convert the ZIP object into a list 

print(converted_list) # Will print:
[("Dan", 179), ("Maria", 163), ("Gibilan", 201), ("Vasile", 174)]
# which is a list of tuples 