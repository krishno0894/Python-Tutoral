'''
lets write a program to print a heart of stars

we will print the heart in two half
'''

n = int(input("enter the number of rows: "))

#first half
for i in range(n//2, n+1 , 2):
    for j in range(1,n-i,2):
        print(" ", sep=" ", end=" ")
    for k in range(1,i+1):
        print("*", sep=" ", end=" ")
    for l in range(1,n-i+1):
        print(" ", sep=" ", end=" ")
    for m in range(1,i+1):
        print("*", sep=" ", end=" ")
    print() #new line after each row

    '''
    we have already created first half of the heart pattern
   lets make the rest of it    
    '''

for i in  range(n, 0, -1):
    for j in range(i, n):
        print(" ", sep=" ", end=" ")
    for k in range(1,2*i):
        print("*", sep=" ", end=" ")

    print()   #newline

'''
thank you for watching 

keep coding guys
'''


