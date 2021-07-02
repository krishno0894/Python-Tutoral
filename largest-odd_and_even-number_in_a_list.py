'''
let's write a program to find largest odd and even number in a given list

logic:
    take a list as input.
    create two new liset oddlist and evenlist

    check if list element is odd add that to oddlist
        if list element is even add that to evenlist
'''

n =  int(input("Enter the size of the list: "))
list = []
for s in range(0, n):
    element = int(input("enter the element: "))
    list.append(element)


odd = []
even = []

for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


odd.sort()
even.sort()

print('largest odd number', odd[-1])


print('largest even number', even[-1])

'''
thanks for watching
'''