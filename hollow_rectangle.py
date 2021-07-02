#lets write a program to print a hollow recrangle of stars
'''
****
*  *
*  *
*  *
****

like this

'''



row = int(input("enter the number of rows: "))

column = int(input("enter the number of columns: "))

#traverse through rows
for i in range(1, row+1):

    #traverse through column
    for j in range(1, column+1):

        #print stars only if it is 1st row and column or last row or column
        if (i == 1 or i == row or j == 1 or j == column ):
            print("*", sep=" ", end=" ")
        else:
            #else print space this is very impoertant . i am a big dummy. dont make mistake i make
            print(" ",sep=" ", end=" ")

    print() #for printing new line after each row

#thank you guys
#see you in the next tutorial