# lets write a program which will print all possible combination
'''
str = 'sejuti'

#print(a[::-1])

print(len(str))
rev = ""
i = len(str) - 1
while (i >= 0):
    print(str[i])
    rev += str[i]
    i -= 1


print(rev)
'''
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fb(n):
    a = 0
    b = 1
    print(a)


    for i in range(n-1):

        a, b = b, a + b


        print(a)



a =fib(10)

print(fb(10))

'''





'''

n = 5

for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",sep=" ",end=" ")
    for k in range((n-i)+1, n+1):
        if (i == 1 or i == n or k == n or k == n-i+1):

            print("*",sep=" ",end=" ")
        else:

            print(" ", sep=" ", end=" ")

    print()
'''

''''




num = 9
n = num // 2
n += 1

space = n-1
star = 1

for i in range(1, 2*n):
    for j in range(1,space+1):
        print(" ", sep=" ", end=" ")

    for k in range(1,star*2):
        if k == 1 or k == star*2-1:
            print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")
    print()

    if( i < n):
        space -= 1
        star += 1
    else:
        space += 1
        star -= 1
'''



'''
n =5

for i in range(0, n):
     for j in range(0, n):

            if i == j or j == n-i-1:
                print("*", sep=" ", end=" ")
            else:
                print(" ", sep=" ", end=" ")
     print()
'''
'''
n =5

for i in range(1, n+1):
     for j in range(1, n+1):

            if i == n//2+1 or j == n//2+1:
                print("*", sep=" ", end=" ")
            else:
                print(" ", sep=" ", end=" ")
     print()

'''

str = 'sejutk'

str = str.replace('k','i')

print(str)

s = input("enter: ")


n = int(s)

print(len(s))

r = pow(n,len(s))

print(r)



