'''
let's write a program to find larger string between two string

first we will do it without built in functions
then we ll also do it with built in functions
logic:
 use two for loops to iterate through two string and use two counters to count total characters or length of the string


'''

str1 = input("enter the first string: ")


str2 = input("enter the second string: ")
'''
c1 = 0
c2 = 0

for i in  str1:
    c1 += 1

for j in str2:
    c2 += 1

print()
if c1 > c2:
    print("'",str1, "' is larger")
else:

    print("'",str2, "' is larger")
'''

'''
now lets do the same thing with built in function len()
'''

if len(str1) > len(str2):
    print("'", str1, "' is larger")
else:

    print("'", str2, "' is larger")

'''
thank you for watching
'''

