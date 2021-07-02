'''
let us print a hollow mirrored triangle of stars like this

    *
   **
  * *
 *  *
*****

like this
'''

n = int(input("enter the number of rows:  "))

for i in range(1,n+1):

    for j in  range(1,n-i+1):
        #print spaces
            print(" ", sep=" ", end=" ")


    for k in range(n-i+1,n+1):


        if i == 1 or i == n or k == n - i + 1 or k == n:
            # print stars if 1st row or lsat row or last column or n-i+1 column
            print("*", sep=" ", end=" ")
        else:
            #else print stars
            print(" ", sep=" ", end=' ')

    print() #to print newline after each row

    #okay now lets make it hollo using if else condition

    #hope this helped you . thank you for watching

