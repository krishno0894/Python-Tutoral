'''
let's write a program which will print a half diamond of stars
*
**
***
**
*
like this
logic
    loop 1: to iterate through rows(loop variable i)
    initalize variable star =1
    loop 2:(loop variable j)
        if i < row/2 then increse star else decrease star

'''

row = int(input("enter the rows: "))

n = row // 2
n = n + 1

stars = 1
#iterate through rows
for i in range(1, 2*n):

    for j in range(1, stars+1):
        #print stars from 1 to star column
        print("*", sep=" ", end=" ")
    print()
    if i < n:
        # check weather to increment or decrement the stars variables
        stars += 1
    else:
        stars -= 1


    #print new line after each row

    #thank you for watching