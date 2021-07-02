'''
lets write a program to print a hollow inverted mirrored trianlge

*****
 *  *
  * *
   **
    *

    like this

'''

n = int(input("enter the number of rows: "))

for i in range(1, n+1):

    for j in range(1, i):
        #print space fron 1 to i-1 th column
        print(" ", sep=" ", end=" ")

    for k in range(i, n+1):


        if i == 1 or i == n  or k == i or k == n:
            # print stars only in first row and last row and lat column and ith colmn
             print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")



    print() #new line


    #thank you for  watching

    #lets make it hollow with if else conditions
