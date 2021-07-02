#hello guys today we are going to write a program that will print a rectangle of stars


row = int(input("enter the number of Rows: "))
column = int(input("enter the number of Columns: "))

#traverse through rows
for i in range(1,row+1):

    #print stars in each column
    for j in  range(1,column+1):
        print("*", sep=" ", end=" " )  #using sep and end is very important don't forget it

    print() #to print a newline after each row

    #thank you guys , keep coding byes. i will provide the code.