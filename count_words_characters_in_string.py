'''
lets write a program to count total number of words and characters

logic:
    iterate through the string using a for loop untill string ends
    then use a counter and counter is incremented each time for loop runs i.e. runs untill las charactes

    use a if conditon inside the for loop

    if we find space then  use another counter and increment it.
    we will have to add 1 to counter at the  end to count the last word


    lets implement it
'''

str = input("enter the string: ")

count1 = 0
count2 = 0

for k in str:
    count1 += 1
    if k == ' ':
        count2 += 1


print("total number of words: ", count2+1)

print('total number of charactes: ', count1 )

'''

thank you for watching
'''