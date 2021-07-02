'''
lets print a mirrored rhombus like below

    ******
   ******
  ******
 ******
******

'''


n = int(input("Enter the number of rows: "))

#traverse the rows
for i in range(1,n+1):

    for j in range(1, n-i+1):
        #print space fron 1 to n-i column
        print(" ", sep=" ", end=" ")

    for k in range(1,n+1):
        #print star from 1 to nth column
        print("*", sep=" ", end=" ")

    print() #newline

    #thank you for watching


