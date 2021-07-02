'''
let's write a program to find total number of lower case and upper case letters in a string

'''

str = input("enter the string: ")

upperCount = 0
lowerCount = 0

for x in str:
    if x.isupper():
        upperCount += 1
    elif x.islower():
        lowerCount += 1


print("total upper case letters:  ", upperCount)
print()

print("total lower case letters:  ", lowerCount)


'''
thank you for watching
'''
