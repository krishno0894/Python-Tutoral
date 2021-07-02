'''
lets write a programm to print a hollow mirrored rhombus

   ****
  *  *
 *  *
****
like this

'''

n = int(input("enter the number of rows: "))

#iterate through rows
for i in range(1,n+1):

    for j in range(1,n-i+1):
        #print spaces from 1 to n-i th column
        print(" ", sep=" ", end=" ")

    for k in range(1, n+1):

        if i == 1 or i == n or k == 1 or k == n:
            print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")


    print() #new line

    #we have the mirrored rhombus now let make it hollow

    #thank you for watching  keep coding

