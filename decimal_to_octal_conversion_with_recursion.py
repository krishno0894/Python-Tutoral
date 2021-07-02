'''
let's write a program which will perform decimal to octal conversion with the help of recursion


logic:
    We are not going to use built in functions

    base of octal number system is 8

    we will write a function and inside that function
        if number is grater than 1 we call the function itself
                      or else we will print the modulus of that number
'''

def to_Octal(num):
    if num > 1:
        to_Octal(num // 8)
    print(num % 8, end="") #you must use end in order to avoid printing each digit in newlines



n = int(input("enter the decimal number: "))

to_Octal(n)
#thanks for watching