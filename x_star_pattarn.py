'''
lets write a program to print a X star pattern

*    *
 *  *
   *
  * *
*    *



like this

logic:
loop1: variable i(iterate through row)
loop2: variable j(print stars or spaces)

    first print a square of star as we have learned before
    then print star only if  i ==j or j == n-i+1 else print stars

'''

n = int(input("enter the number of rows: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or j == n-i+1:
            print("*", sep=" ", end=" ")
        else:
            print(" ", sep=" ", end=" ")
    print() #newline

'''
now we have a square of star let make it x shape star
thank you for watching

see you in the next video

'''