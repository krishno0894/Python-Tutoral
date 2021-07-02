#let's write a program to print hollow rectangel of stars


n = int(input("enter number of rows: "))

for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1): #print star only in 1st columun or row =0, last column or row = n-1 as index started from 0
            print("*", sep=" ", end=" ")
        else:
            print(" ",sep=" ",end= " ")
    print( ) #to print new line

    #thank you guys