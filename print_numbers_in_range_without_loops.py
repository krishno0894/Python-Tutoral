
def printNumbers(num):
    if(num > 0):
        printNumbers(num - 1)
        print(num)


n = int(input("enter a upper limit: "))
printNumbers(n)

