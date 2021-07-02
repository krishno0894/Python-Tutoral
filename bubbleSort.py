from pythonds.basic.stack import Stack

#today we will implement bubble sort


def bubbleSort(list):

    for i in range(len(list)-1, 0, -1):

        for j in range(i):
            if list[j] < list[j+1]:
                temp = list[j]
                list[j] = list [j +1]
                list[j + 1] = temp




#driver code

l = [10, 2, 214, -23 , 25, -9 -40, 10,-290]

bubbleSort(l)
print("Sorted in descening order")
print(l)

#lets sort in descending order

#keep codn' bye


