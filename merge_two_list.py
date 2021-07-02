'''

let's write a program which will merge two list

logic:
    take two as user input or any defined list
    and then merge them and create a new list


'''

n1 = int(input("enter the size of 1st list: "))
list1 = []
list2 = []
new = []
for i in range(0,n1):
    element = int(input("enter the element: "))
    list1.append(element)

n2 = int(input("\nenter the size of 2nd list: "))

for i in range(0, n2):
    element = int(input("enter the element: "))
    list2.append(element)


new = list1 + list2


print('mergerd list: ')
print(new)

'''
so we have merged two list........

thank you for watchin'
'''


