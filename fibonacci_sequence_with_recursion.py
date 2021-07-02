'''
lets write a program to print fibonacci sequence using recursion

'''

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x-1) + fibonacci(x-2))  #calling the fibonacci() function recursively


n = int(input("how many terms you want to print: "))

if n > 0:
    print("fibonacci sequence is : ")
    for k in range(n):
        print(fibonacci(k))
else:
    print("enter a positive number")

'''
thanks for watching
'''



