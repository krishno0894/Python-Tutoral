'''

today we are going to implement insertion sort, lets first see the logic/concept of insertion sort

hope the concept is clear now.

'''

def insertion_Sort(list, n):
    for i in  range(1, n):
        element = list[i]
        hole = i

        while hole > 0 and list[hole - 1] > element:
            list[hole] = list[hole - 1]
            hole = hole - 1
        list[hole] = element





n = int(input("enter the size of the list: "))

list = []

for i in range(0 , n):
    element = int(input("enter the list element: "))
    list.append(element)
print("unsorted list: ",list)
print()
insertion_Sort(list, n)
print("sorted list: ",list)


'''
i hope it helped. thank you for watching
'''