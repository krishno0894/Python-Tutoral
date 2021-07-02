#today we are going to write a program which will show the smallest divisor of a number

n = int(input("enter the number: "))

list = []

for i in range(2, n+1):
    if(n % i == 0 ):
        list.append(i)

#now sort the array

list.sort()

print("Smallest Divisor: ",list[0])


#thank you