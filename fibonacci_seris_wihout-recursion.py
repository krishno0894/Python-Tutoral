#lets write a program to print fibonacci seris nth times.

n = int(input("enter the number: "))

a = 0
print(a)
b = 1

for i in range(n-1):

    a, b = b, a + b
    print(a)

print("fibonacci seris printed ",n," times")

#thank you have a good day