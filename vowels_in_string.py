'''
let's write a program to find total number of vowels in a string

'''


str = input("enter the string: ")

count = 0

print("Vowels are: ")
for k in  str:
    if k == 'a' or k=='e' or k=='i' or k=='o'or k =='u' or k == 'A' or k=='E' or k=='I' or k=='O'or k =='U':
        count += 1
        print(k)


print("total vowels: ", count)

'''
hope you got it 

thank you
'''