'''
let's write a program to find all armstrong numbers in an specific interval or range

a number is called armstrong number if sum of all digit of a number is equal to the number itself

i.e.
 153 = 1^3 + 5^3 + 3^3 = 153 so armstrong number

'''

lower = int(input("enter the lower limit: "))
upper = int(input("enter the upper limit: "))

print("armstrong number in interval ", lower, " to ", upper, "is: ")

for number in range(lower, upper+1):
    temp = number # copy the number for future use, value of number variable  will ber altered during calculations
    sum = 0

    while number > 0:
        remainder = number % 10
        sum += remainder ** 3 #we can also use instead of pow() function
        number //= 10


    if temp == sum:
        print(temp)


'''
thank you for watching
'''