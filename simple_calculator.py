'''
let's build a simple calculator with some basic logics

'''

print("select an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print() #for newline

choice = int(input("enter your choice: "))

num1 = float(input("enter the first number: "))

num2 = float(input("enter the second number: "))

if choice == 1:
    print(num1, " + ", num2, " = ", num1+num2)

elif choice == 2:
        print(num1, " - ", num2, " = ", num1 - num2)

elif choice == 3:
    print(num1, " * ", num2, " = ", num1*num2)

elif choice == 4:
    print(num1, " / ", num2, " = ", num1/num2)
else:
    print("invalid choice, enter currect choice")


'''
great we have built a simple calculator which can perform addition, subtraction, multiplication and division

thank you for watching

'''