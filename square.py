#finding area of rectangle using class

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#lets take user input for width and length

len = float(input("Enter the Length: "))

wid = float(input("Enter the width: "))

object = Rectangle(len,wid)

print("Area:", object.area())

#you could use float instead of intege

#keep coding guys bye