
string = input("enter the String: ")
'''
rev = "" #will be used to store reverse string

i = len(string) - 1 #intializing the index for while loop

#while loop will run from last index of the string to the first index = 0

while i >= 0:
    rev += string[i]

    i -= 1


print("Reverse String : ",rev)
'''

#lets look at another approach to reverse a string in python


print("Reverse String: ",string[::-1]) #string_name[::-1] reverse a string


#hope you have good day , bye