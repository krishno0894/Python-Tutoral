#we will write a program to print a hollow triangle of stars


n = int(input("enter the numbe of rows: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if(i == 1 or i == n or j == 1 or j == i): #print stars only when last row(i=n) , 1st column(j=1) amd row(i=1) , last column of triangle(j=i)
            print("*",sep=" ",end=" ")
        else:
            print(" ",sep=" ",end=" ") #else print a space

    print() #new line


#thank you guys

