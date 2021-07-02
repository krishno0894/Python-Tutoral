'''
let's write a program which wil convert a decimal to binary, octal and hecxa-decimal numbers respectively

logic:
    python have built in function to convert into binary(bin()), octal(oct()) and hexa-decimal(hex()) functions

    we will create a function which will take number as parameter and convert that number into all number system mentioned above.

'''

def Decimal_To_All(number):
    print(bin(number))
    print(oct(number))
    print(hex(number))


#lets take user input

decimal = int(input("enter the decimal number: "))

Decimal_To_All(decimal)

