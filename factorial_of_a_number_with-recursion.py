#lets wtrite a program to find factorial of a numebr with recursion

def Factorial(x):
    if x == 1:
        return  1
    else:
        return x * Factorial(x-1)



#driver code for above function

number =  int(input("enter  a number: "))


print(number,"! = ",Factorial(number))

#see you guys in the next video till then bye