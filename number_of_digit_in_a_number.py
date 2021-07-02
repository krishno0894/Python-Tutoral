'''
let's write a program to find number of digit in a given number
'''

number = int(input("enter the number: "))
temp = number #copy the number for future use

count = 0

while number > 0:
    remainder = number % 10
    count += 1
    number = number // 10


print(temp, " contains ", count, " digits")

'''
thanks for watching 
'''
