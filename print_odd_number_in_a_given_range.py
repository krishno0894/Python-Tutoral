#lets write a program to print all the odd number in agiven number

lowerLimit = int(input("enter the lower limit: "))
upperLimit = int(input("enter the upper limit: "))

for x in range(lowerLimit,upperLimit+1):
    if x % 2 != 0:
        print(x)


        #thank you for watchin'