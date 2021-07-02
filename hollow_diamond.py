'''
let's write a program to print a hollow diamond of stars
  *
 * *
*   *
 * *
  * like this

  logic :
    intialize
        space = row/2 - 1
        star = 1
        space will decrease and star will increase untill i < row/2
        if i> row/2 space will increase and star will decrease

    loop 1: to iterate through rows
    loop 2 : print spaces
    loop 3 :
            if 1st or last column
            then print stars or
            else print spaces

'''




num = int(input("enter the number of rows: "))

n = num // 2

n = n + 1

spaces = n - 1
stars = 1

#iterate throuh rows
for i in range(1, 2*n):

    for j in  range(1, spaces+1):
        #print space from 1 to space th column
        print(" ", sep=" ", end=" ")

    for k in range(1, 2*stars):
        #print stars only if it is first column j==1 or last column j == 2*star-1
        if k == 1 or k == 2*stars-1:
            print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")

    print() #print new line

    if i < n:
        spaces -= 1
        stars += 1
    else:
        spaces += 1
        stars -= 1

'''
we have adiamond now lets make it hollow
thank you for watchin'

bye guys
'''

