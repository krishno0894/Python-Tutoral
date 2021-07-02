#lets write aprogram to find largest divisor of a numebr

number = int(input("enter a number: "))

l = []

for i in range(2, number):
    if number % i == 0 :
        l.append(i)


l.sort()

print("Largest Divisor = ", l[-1])