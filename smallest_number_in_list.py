#lets write aprogram to find smallest number in a list


list = [10, 20, 5, 2, -20]

min = list[0]

for x in range(1,len(list)):
    if min > list[x]:
        min = list[x]

'''
#now lets use sort() function

list.sort() #sort the array in ascending order

#sorted list
print(list,"\n")
#print("Smallest Number : ",min) first element at index 0 wil be the smallest number in an sorted array

print(list[0])
'''
print(list,"\n")
print("Smallest Number : ",min)