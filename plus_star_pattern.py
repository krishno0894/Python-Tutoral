'''
let's write  a program to print plus star pattern or plus of stars

    *
    *
* * * * *
    *
    *
    like this

    logic:
    loop1(variable i): iterate through rows
    loop2(varivable j ): print stars or space

    we will first print a squre and then make that into a plus

    we will print star only if i == row//2+1 or j == row//2+1 else print spaces


'''


row = int(input("enter the number of rows: "))

for i in range(1, row+1):
    for j in range(1, row+1):
        #print stars only if this logic  is true
        if i == row//2+1 or j == row//2+1:
            print("*",sep=" ", end=" ")
        else:
            #else print spaces
            print(" ", sep=" ", end=" ")
    print() #new line

'''
we have a square now let make it into plus pattern


thank you for watching 

'''

