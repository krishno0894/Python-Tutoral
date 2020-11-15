p = int(input("enter the first number:  "))
q = int(input("enter the second number: "))
l = int(input("enter the third number:  "))

list = []
list.append(p)
list.append(q)
list.append(l)


for i in range(0,3):
    for s in range(0,3):
        for b in range(0,3):
            if i != s and s != b and b != i :
                print(list[i],list[s],list[b])




#thaks for watching keep coding