# def function_name():
#     print("DEF is the keyword for a function")

# # help("str") is a handy function to give us information about functions and methods

# # Assign return to variable 
# def assigning_value(param1):
#     return param1 + param1

# double_value = assigning_value(74) # will now be equal to 148

# ### MULTIPLE RETURNS
# def multiple_returns(param1, param2, param3):
#     monday = param1 + 10
#     tuesday = param2 + 20
#     friday = param3 * param3
#     return monday, tuesday, friday

# monday, tuesday, friday = multiple_returns(10, 20, 50)
# print(monday, tuesday, friday) # will print 20, 40, 2500

# #### str() can be used to convert integer and floate into string

# # lists (arrays) can be passed as arguments too
# def list_manipulation(lst):
#     print(lst[0])

# list_manipulation([1, 2, 3, 4]) #will print 1


cool_fruit = "Watermelon"
print(cool_fruit[len(cool_fruit) - 2])