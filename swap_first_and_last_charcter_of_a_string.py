'''
lets write a program to swap first and last character of string

'''

str = input("enter the string: ")

newstr = ""

newstr = str[-1:] + str[1:-1] + str[:1]



'''
thanks for watching
'''

print("Modified String: ", newstr)