class Number:

    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return (self - other)
        # now the + operator returns the diference between the two operators 

number1 = Number(5)
number2 = Number(10)

number1 + number2 # will return -5