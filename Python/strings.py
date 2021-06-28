# Strings behave MAINLY like lists 
### BUT ARE IMMUTABLE! CANNOT BE CHANGED! 

# There’s an even easier way than iterating through the entire 
# string to determine if a character is in a string. We can do 
# this type of check more efficiently using in. in checks if one 
# string is part of another string.

word = "Potato"

if "r" in word:
    print("Contains R")
else:
    print("No R")

sentence = "Potatoes are delicious"

### FORMATTING METHODS ###

word.lower() # potato
word.upper() # POTATO
word.title() # Potato Is Delicious

word.split() # [Potatoes, are, delicious]
word.split("o") # [P, tat, es are delici, us]

# We can use escape sequences to split a string:
# \n Newline
# \t Tab
word.split("\n") # would split the string by new lines

# Joining strings
sentence_list = ["My", "name", "is", "sadness", "boy"]
new_word = " ".join(sentence_list) # Joins list by using space as a delimiter
print(new_word)
new_csv_list = ",".join(sentence_list) # Joins list by using a comma, to create a CSV

# Strip function to clean
word.strip() # Clears all white space
word.strip("!") # Clears all "!" from either end of the string

# Replace elements of string
string_name.replace(character_to_be_replaced, character_to_be_replaced_with)
new_word = word.replace(" ", "_") # Replaces spaces with underscores

# Find
"Napoleon".find("N") # Will return index of "N", which is 0
"Iooana".find("oo") # Will return the index of the first "o", which is 1

### FORMAT, used to add variables into strings ###
def function_to_format(arg1, arg2):
    return "My name is {} and I was born in {}".format(arg1, arg2)
function_to_format("Dan", "Marghita") # will return My name is Dan and I was born in Marghita

def function_with_keywords(arg1, arg2):
    return "My name is still {name} and I was born in {city}".format(name=arg1, city=arg2)
# We can use keywords to eliminate any confusion regarding function arguments