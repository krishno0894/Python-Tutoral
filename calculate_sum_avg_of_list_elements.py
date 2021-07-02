n = int(input("enter the list size: "))

l = []

for i in range(0,n):
    e = int(input("enter the element: "))
    l.append(e)

sum = 0
for i in range(0,n):
    sum += l[i]


print("Sum = ",sum,"\n","Avg = ",sum/n)

#thanks for watching keep coding