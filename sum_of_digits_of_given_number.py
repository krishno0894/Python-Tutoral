#lets write a program to find out the sum of a given number . let jump rihght into it


number = int(input("enter the number: "))
sum = 0 #intialize sum to 0
remainder = 0

while(number > 0):
    remainder = number % 10
    sum += remainder
    number //= 10


print("Sum = ", sum)

#keep coding guys .
#subscibe my channel for more videos