'''
let's write a program which will perform decimal to hexa-decimal conversion with the help of recursion


logic:
    We are not going to use built in functions

    base of hexa-decimal number system is 16

    we will write a function and inside that function
        if number is grater than 1 we call the function itself
                      or else we will print the modulus of that number
'''


def to_Hexa_Decimal(num):
    if num > 1:
        to_Hexa_Decimal(num // 16)
    if num % 16 == 10:
        print("a", end=" ")
    elif num % 16 == 11:
        print("b", end=" ")
    elif num % 16 == 12:
        print("c", end=" ")
    elif num % 16 == 13:
        print("c", end=" ")
    elif num % 16 == 14:
        print("e", end=" ")
    elif num % 16 == 15:
        print("f", end=" ")
    else:
        print(num%16, end=" ")


n = int(input('enter the decimal number: '))

to_Hexa_Decimal(n)

'''
its working but we can do little more 
print a instead of 10
...
print f instead of 15

it's working

thank you for watching
'''
