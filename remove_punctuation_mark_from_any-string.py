'''
let's write a program which will remove punctuation marks from a given string

logic:
    take user input: a string

    create a string of punctuation marks(all punctuation marks)

    create a empty string to store the punctuation marks  string

    use a for loop to traverse through each character of the string and
        inside the for loop add each character to new string only if it doesn't contain any punctuation marks(use if condition)

'''

str = input("enter the string: ")

pun = "!@()[]{}-;:'`\,<>/?#$%^&_~"

new_str = ""

for i in str: #traverse through each characters
    if i not in pun: #check if punctuation mark exists or not
        new_str = new_str + i  #create new punctuation free string



print("Given String: ", str)
print()

print("Punctuation Free String: ", new_str)


'''
thanks for watching
'''
