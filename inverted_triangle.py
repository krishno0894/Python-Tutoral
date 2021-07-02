'''
lets write a program to print a inverted triangle of stars

*****
****
***
**
*
like this


'''


n = int(input("enter the number of rows: "))

#traverse through rows
for i in range(1, n+1):

    for j in range(1, (n-i)+2):
        #print stars form 1 till n-i+1 th column
        print("*", sep=" ", end=" ")

    print() #for printing new line after each row

    #thanks for watching