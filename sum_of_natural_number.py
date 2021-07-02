'''
lets write a program to find sum of first n natural numbers

natural number are number  positive and without decimal place number, like 1,2,3............

'''

N = int(input("enter the upper limit of natural number: "))

temp = N

sum = 0

while N > 0:
    sum += N
    N -= 1

print("sum of first ", temp, " numbers is : ", sum)

'''
thank you for watching
'''