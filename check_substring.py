#lets write a program to find out whether a substring is present in a string or not


string = input("enter the string: ")

substring = input("enter the substring: ")

#we will use find() built in function

if string.find(substring) == -1:
    print("Substring not found")
else:
    print("substring found")



#keep coding guys bye