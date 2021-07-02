'''
let's write a program which will swap first and last value/element of a list
lets do it

'''

list = []
n =int(input("enter the size of the list: "))

for i in range(0, n):
    element = int(input("enter the element: "))
    list.append(element)

print("Before Swap")
print(list)
print()

temp = list[0]
list[0] = list[n-1]
list[n-1] = temp

print("After Swap")
print(list)


'''
thank you for watching
'''
