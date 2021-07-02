'''
lets write a program to print a holllow inverted triangle


*****
*  *
* *
**
*
like this
'''


n = int(input("enter the number of rows: "))


for i in range(0, n):

    for j in  range(0, n-i):

        if i == 0 or i == n or j == 0 or j == n-i-1:
            #print stars only if row is first and last or colmumn is first and n-ith. in this case n-i-1 as we stated loop from zero
            print('*',sep=" ", end= " ")

        else:
            print(" ", sep= " ", end=" ")


    print() #new line after eah line

    #thank you guys


    #lets make it hollow