'''
lets write a program to print moirrored triangle
   *
  **
 ***
****

like this

'''


row = int(input("enter the number of rows: "))

for i in range(1,row+1):

    for j in range(1,row-i+1):
        #print spaces from 1 to row-i positions
        print(" ", sep=" ", end=" ")

    for k in range(row-i+1,row + 1):
        #print stars from row-i+1 to row
        print("*" , sep=" ", end=" ") #dont forget sep and end

    print("") #print new line

    #thank you for watching bye guys