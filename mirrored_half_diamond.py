'''
let's write a program to print a mirrored half diamond
  *
 **
***
 **
  *
  like this

  logic:

  loop1(i): iterate through rows
  loop2(j): print spaces
  loop(k): print spaces

  initialize two variable
    stars = 1
    space = row/2 -1
    if i < row/2
    increase stars and decrease spaces
    else
    do opposite
'''

row = int(input("Enter the number of rows: "))

n = row // 2
n = n + 1

stars = 1
spaces = n - 1

for i in range(1,2*n):

    for j in range(1,spaces+1):
        #print space from 1 to space th column
        print(" ", sep=" ", end=" ")

    for k in range(1,stars+1):
        #print stars form 1 to stars th column
        print("*", sep=" ",  end=" ")

    if i < n:
        stars += 1
        spaces -= 1
    else:
        stars -= 1
        spaces += 1

    print() #print newline

#thank you for watching
#the following video will be more interesting