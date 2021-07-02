#today we are going to write a program which will search for a number/elements in list
#we wil use linear seach approach
#it is not the most effective not good good way to learn about searching
#we will iterate through all the element of the list lets begin


def linearSearch(list, num):
    flag = 0
    index = 0
    while index < len(list):
        if list[index] == num:
            flag = 1
            break

        else:
            index += 1

    return  flag



#driver code for above function

list = []

n = int(input("enter the size of the list: "))

for i in range(0, n):
    p =int(input("Enter the element: "))
    list.append(p)

number = int(input("enter the number to be searched: "))

result =  linearSearch(list,number)
print("\n")
print(list)



print("\n")
if result == 0:
    print(number,"not Found in the list")
else:
    print(number,"is found int the list")

    #thank you for watcching #keep coding

    #i'll put the code in the description box so dont worry