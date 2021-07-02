'''

let's wrtie a program to print a pyramid of stars

--*
-***
*****
like
this
'''

n = int(input("enter the number of rows: "))

#iterate through rows
for i in range(1,n+1):
    for j in range(1, n-i+1):
        #print spaces from 1, till n-i th column
        print(" ", sep=" ", end=" ")

    for k in range(1, (2*i)):
        #print stars from 1 to 2*i -1 th column
        print("*", sep=" ", end=" ")


    print() #newline


#thank you for watching