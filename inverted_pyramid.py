'''
lets write a program which will print a inverted pyramid of stars.
*****
 ***
  *

  like this
  logic:
  loop 1 : iterate through rows
  loop 2 : print spaces form 1 to i-1 th index
  loop 3 : print srats from 1 to 2*n-(2*i-1)th index

'''


n  = int(input("enter the number of rows: "))

#iterate through rows
for i in range(1,n+1):

    for j in range(1,i):
        #print space from 1 to i-1 index
        print(" ", sep=" ", end=" ")


    for k in range(1, 2*n-(2*i-1)+1):
        #print stars from 1 to 2*n-(2*i-1) th index/column
        print("*", sep=" ", end=" ")


    print() #for printing new line

    '''
    if n= 3
    
    then in 1st iteration print 0 space and 2*3-(2*1-1)= 5 stars
    
    2nd iteration print 1 to 2(i) = 1 space and 2*3-(2*2-1)= 3 stars
    
    3rd iteration print 1 to 3(i) = 2 space and 2*3-(2*3-1)= 1 stars
    
    hope you got the logic thanks
    
    '''