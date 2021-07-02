#lets write a program to identify prime numbers


n = int(input("enter the number: "))
flag = 0
for i in range (2,n):
    if n % i == 0:
        flag += 1



if flag <= 0 :
    print(n,"is Prime")
else:
    print(n,"is not Prime")


#thanks guys keep coding