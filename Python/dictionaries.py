# Unordered set of key : value pairs
# It is important that keys are unchangeable. This is why we cannot use a list as a key

# To add a key
menu = {}
menu["potato"] = "12 Euro"

#To add multiple keys
menu.update({"merdenele": 13, "chelneri": 4, "location": "poverty_land"})

# Assignment methods can be used to update the dictionary as well

### COMBINING TWO LISTS INTO A DICTIONARY
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)} # zip() is a one-time-use only method and gets exhausted after one use

###########################
# How to use dictionaries #
###########################
dictionary_name = {
    "Key_name": "Value_name"
}
dictionary_name["Key_name"] # will return "Value_name"

# Check if key in dictionary
if "Key_name" in dictionary_name:
    print(dictionary_name["Key_name"]) # will print the key:value pair

# Another way to check for keys is to use try / except: 
try:
    print(dictionary_name["Inexistent_key"])
except KeyError:
    print("Key does not exist")

### HOW TO SAFELY GET A KEY BY USING THE .GET() METHOD ###
dictionary_name.get("Existent_Key", "Value to return if the key doesn't exist")
european_capitals.get("Belgium", "Capital not found")

# Delete a key / value from dictionary #
dictionary_name.pop("Key_name", "Value to return if value not found")

### GETTING THE KEYS OFF A DICTIONARY ###
list(dictionary_name) # will store a muttable list
dictionary_name.keys() # will return a view only `dict_keys` object
for element in dictionary_name.keys():
    print(element) # will print all keys of an object

### GETTING THE VALUES OFF A DICTIONARY ###
dictionary_name.values() 
list(dictionary_name.values())

### GET BOTH: ###
# it returns a tuple, consisting of (key, value)

for key, value in dictionary_name.items():
    print(key, value)
