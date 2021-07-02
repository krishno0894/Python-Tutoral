'''
lets write a program to print a diamond of stars
  *
 ***
*****
 ***
  * like this

  logic :
    intialize
        space = row/2 - 1
        star = 1
        space will decrease and star will increase untill i < row/2
        if i> row/2 space will increase and star will decrease

'''

row = int(input("enter the number of rows: "))

n = row // 2
n = n + 1 #you cold use ceil function instead

spaces = n-1
stars = 1
for i in range(1, 2*n):

    for j in range(1, spaces+1):
        #print spaces from 1, to spaces
        print(" ", sep=" ", end=" ")

    for k in range(1, 2*stars):
        #print stars from  1 to 2*stars-1
        print("*", sep=" ",end=" ")
    print() #print new line after each row

    if i < n: #check wheather to increase or decrease spaces and stars
        spaces -= 1
        stars += 1
    else:
        spaces += 1
        stars -= 1

#thank you for watching