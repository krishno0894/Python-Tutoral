#let's write a program to print identity matrix

row = int(input("enter the number of rows/colmumn: "))

for i in range(1,row+1):
    for k in range(1,row+1):
        if i == k:
            print("1", sep=" ",end=" ")
        else:
            print("0", sep=" ", end= " ")


    print( ) #to print new line


    #thank you for watching

