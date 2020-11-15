#lets write a program to print a seris till nth number
#take n as input and print 1+2+3+....+n = SUM

#lets begin

n = int(input("enter a Number: "))

l = []

for i in range(1,n+1):
    print(i, sep=" ", end= " ")

    if i < n:
        print("+", sep = " ", end = " ")

    l.append(i)


print(" = ", sum(l))



#thank you for watching