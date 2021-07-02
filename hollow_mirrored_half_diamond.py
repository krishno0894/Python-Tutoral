'''
lets write a program to print a hollow morrored half diamond
    *
   **
  * *
*   *
  * *
   **
    *
  like this

  logic:

  loop1(i): iterate through rows
  loop2(j): print spaces
  loop(k): print spaces
    inside this loop
    we will only print stars if it is 1st column(k==1) or last column (k == star)

  initialize two variable
    stars = 1
    space = row/2 -1
    if i < row/2
    increase stars and decrease spaces
    else
    do opposite
'''



row = int(input("enter the number of rows: "))

n = row // 2
n += 1
stars = 1
spaces = n-1

for i in range(1, 2*n):

    for j in range(1, spaces+1):
        print(" ", sep=" ", end=" ")

    for k in range(1, stars+1):
        if k == 1 or k == stars:
            print("*", sep=" ", end= " ")
        else:
            print(" ", sep=" ", end=" ")

    if i < n:
        stars += 1
        spaces -= 1
    else:
        stars -= 1
        spaces += 1

    print() #print new line

'''
now we have a mirrored half diamond lets make it hollow
thank you for watching
'''
