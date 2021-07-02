'''
let's write a program to print a hollow inverted pyramid
like below
*******
 *   *
  * *
   *

  like this
  logic:
  let loop variable be i,j,k respectively
  loop 1 : iterate through rows
  loop 2 : print spaces form 1 to i-1 th index
  loop 3 : this loop will run  from 1 to 2*n-(2*i-1)th index
            print stars only if it is
            if 1st row(i=1) or first column(k = 1) or last column or index(k = 2*n -(2*i-1))

            else print spaces

 lets starts coding

'''

n = int(input("enter the number of rows: "))

#iterate  through rows
for i in range(1, n+1):

    for j in range(1, i):
        #print spaces form 1 to i-1 th index
        print(" ", sep=" ", end=" ")

    for k in range(1, 2*n-(2*i-1)+1):
        if i == 1 or k == 1 or k == 2*n-(2*i-1):
            # print stars only if it is if 1st row(i=1) or first column(k = 1) or last column or index(k = 2*n -(2*i-1))

            print("*", sep=" ", end=" ")
        else:
            #else print spaces
            print(" ", sep=" ", end=" ")


    print() #print newline after each row


'''
we have a inverted pyramid now lets make it hollow
    
    
    if n= 3
    
     1st iteration we have 0 spaces and 2*n-(2*1-1) = 5 stars(print all the stars as i==1 first row)
    2nd iteration we have 1 to 2-1 = 1  spaces and 2*n-(2*2-1) = 3 stars(print just 2 the stars as k == 1 or k == 2*n-(2*i-1) and 1 space)
    
    3rd iteration we have 1 to 3-1 = 2 spaces and 2*n-(2*3-1) = 1 stars(print just 1 the stars as k == 1 )
    
    thank you for watching
    
    
    '''