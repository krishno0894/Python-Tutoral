'''
let's write a program which will sort words alphabeatically

logic:
    1) take user input
    2) convert string into a list
    3) sort the list using sort() function
    4) print the list using a for loop

'''

str = input("enter the string: ")

list = str.split() #create list from string

list.sort() #sort the list

print("after sorting alphabetically: ")

#print the list using a for loop
for word in list:
    print(word, end=" ")

#thanks for watching

