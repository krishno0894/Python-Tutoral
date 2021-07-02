'''

we ll write a program to print a rhombus

****
 ****
  ****
   ****
   like this


'''

n = int(input("enter the number of rows: "))

#iterate through rows
for i in range(1,n+1):

    for j in range(1,i):
        #print space from 1 to i-1
        print(" ", sep=" ", end=" ")

    for k in range(1, n):
        #print stars for 1 to n
        print("*", sep=" ", end=" ")

    print() #new line after each row

    #thanks for watching