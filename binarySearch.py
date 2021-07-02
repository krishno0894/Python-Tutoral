#in this video we ll implement binary search. i hope your concept is clear.



def binarySearch(list, num):
    first = 0
    last = len(list)-1
    flag = 0

    while first <= last :
        mid = (first + last) // 2
        if list[mid] == num:
            flag =1
        else:
            if num < list[mid]:
                last = mid -1
            else:
                first = mid + 1

    return flag


#driver code

n = int(input("enter the size of the list: "))

list = []

for i in range(0, n):
    p =int(input("enter the element: "))
    list.append(p)

#we need a sorted list for binary search so lets use sort() function

number = int(input("enter the number to be searched: "))

list.sort()
print("\n",list,"\n")






result = binarySearch(list,number)

if result == 0:
    print(number," not found the list")
else:
    print(number,"is found in the list")

#thank you for watching