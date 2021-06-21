### FOR loop ###
# for <temporary variable> in <collection>
#   <action>

# We can also write simple loops on one line
    for element in listOfElements: print(element)
# is the same with 
    for element in listOfElements:
        print(element)

# When we do not have a list to itierate through we can use range() function

six_steps = range(6)

for element in range(6): # we can use six_steps too
    print("Testing use of range()") # it will print the input text 6 times
    # element here can be used to track iterations, like below
    print("This is iteration number", element + 1)


### WHILE loop ###
# while <conditional statement>:
#   <action>

count = 0
while count <= 3:
    print(count)
    count += 1

# Elegant option: 
while count <= 3: print(count); count += 1

### BREAK statement ###
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

### CONTINUE statement ###
# It is used to skip an iteration
for i in big_number_list:
  if i == 3:
    continue
  print(i) # it will print 0, 1, 2, 4, 5, 6, 7

### NESTED LOOPS ###
for element in first_list: 
    for sales in element:
        print(sales)

### LIST COMPREHENSION ###
originalList = [3, 4, 5, 6, 7]
doubled = [num * 2 for num in originalList]
doubled = [num * 2 for num in range(6)]
# new_list = [<expression> for <element> in <collection>]

doubled_with_condition = [num * 2 for num in originalList if num > 2]
# using comprehension with an IF
doubled = [num * 2 if num < 0 else num * 3 for num in originalList ]
# or even with an IF / ELSE