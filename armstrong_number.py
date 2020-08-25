'''
let's write a program which will be able to find armstrong number

armstrong number is number whose sum of cube of all digit is equal to the number itself
ex. 153, 370, 371

i.e.
153 = 1^3 + 5^3 + 3^3 = 153 so armstrong number

'''

number = int(input("enter the number: "))

temp = number #copying the entered number in a variable for future use
sum = 0

while number > 0:
    remainder = number % 10
    sum = sum + pow(remainder, 3) # or you can just use (remainder**3) it will also give us the cube of a number
    number = number // 10


if temp == sum:
    print(temp," is a armstrong number")
else:
    print(temp, " is not a armstrong number")

'''
hope you understood 

thank you for watching
'''

