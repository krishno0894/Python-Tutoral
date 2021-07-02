'''

let's write a program which will convert a decimal number into a binary number with recursion

logic:
    We are not going to use built in functions

    base of binary number system is 2

    we will write a function and inside that function
        if number is grater than 1 we call the function itself
                      or else we will print the modulus of that number

'''

def to_Binary(number):
    if number > 1:
        to_Binary(number // 2)

    print(number % 2, end=" ") #use end to the result in one line


number = int(input("enter the number: "))

to_Binary(number)

#thanks for watching