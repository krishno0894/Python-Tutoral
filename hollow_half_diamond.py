'''
let's write a program to print a hollow half diamond of stars
*
**
* *
*   *
* *
**
*
like this
logic
    loop 1: to iterate through rows(loop variable i)
    initalize variable star =1
    loop 2:(loop variable j)
        if 1st or last column then print star or else print spaces. (j == 1 or j == stars)


'''


row = int(input("entert the number of rows: "))
n = row // 2
n = n + 1

stars = 1

#iterate through rows
for i in range(1, 2*n):

    for j in range(1, stars+1):
        if j == 1 or j == stars: #print stars only if it is 1st or last column
            print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")
    if i < n:
        stars += 1
    else:
        stars -= 1


    print() #print new line
'''
we have a half diamond now lets make it hollow  
thank you for watching

 '''