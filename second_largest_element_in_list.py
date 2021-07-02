'''
lets write a program to find second largest element in a list

logic:
    take a lsit as input or use defined list

    sort the list using  sort() finction
    sort() --> sort the list in ascending order
    then element of the index before the last index will be the second largest element

'''


n = int(input("enter the size of the list: "))

list = []

for i in range(0, n):
    element = int(input("enter the element: "))
    list.append(element)

list.sort()

print("secornd largest element = ", list[n - 2])

'''
#as we have the length of the list we can directly use it or we use len() function to find the length of list

list[lenght - 2 ] will be the second largest element 

i hope you understood the logic
thank you for watching 


'''