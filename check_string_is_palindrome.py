#lets wirte a code to see whether a string is palindrome of not

str = input("enter the string: ")

#str[::-1] actually revese the current string. its way better methed than checking every character wih loop. so time complexity is better in this approach
if(str == str[::-1]):
    print(str,"is Palindrome")
else:
    print(str,"is not Palindrome")


    #thank you