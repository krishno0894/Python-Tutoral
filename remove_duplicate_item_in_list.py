'''
lets write a program to remove duplicate elemnet in a list



'''

n = int(input("enter the size of the list: "))

list = []

for i in range(0, n):
    element = int(input("enter the element: "))
    list.append(element)

s = set()


new = []

for i in list:
    if i not in s:
        new.append(i)
        s.add(i)

print("non duplicate items: ", new)

'''
thanks for watching
'''

