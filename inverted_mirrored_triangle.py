'''
we'll write a program to print a inverted mirrored triangle

*****
 ***
  **
   *

   like this

'''

n = int(input("enter the number of rows: "))

for i in  range(1,n+1):

    for j in range(1, i):
        #print space from column 1 to i-1
        print(" " , sep=" ", end=" ")

    for k in range(i, n+1):
        #print stars form ith column  to nth column
        print("*", sep=" ", end=" ")

    print() #print new line after each row

    #thank you for watchin



