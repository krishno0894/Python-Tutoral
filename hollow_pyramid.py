'''
lets write a program to print hollow pyramid
   *
  * *
 *   *
*******


'''

n =  int(input("enter the number of rows: "))

#iterate through rows
for i in range(1, n+1):

    for j in range(1,n-i+1):
        #print spaces form 1 to n-i th column
        print(" ", sep=" ", end=" ")

    for k in range(1,2*i):
        if i == 1 or i == n or k == 1 or k == 2*i-1:
            print("*", sep=" ", end=" ")

        else:
            print(" ", sep=" ", end=" ")

    print() #newline after each row
#now we have the pyramid lets make it hollow

#thank you for watching
