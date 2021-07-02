'''

we will print a hollow rhombus like this

****
 *  *
  *  *
   ****

'''


n = int(input("enter the number of rows: "))

for i in range(1, n+1):

    for j in  range(1, i):
        #print trailing spaces from 1 to i-1th column
        print(" ", sep=" ", end=" ")

    for k in range(1, n+1):
        if i == 1 or i == n or k == 1 or k == n:
            #print start at 1st and last row and columns only
            print("*", sep=" ", end=" ")
        else:                                               #else print space
            print(" ", sep=" ", end=" ")

    print() #for new line

    #we hava rhombus now let make it hollow

    #thnk you for watching