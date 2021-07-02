low = int(input("enter the lower limit: "))
high = int(input("enter the upper limit: "))

for s in range(low, high):
    flag = 0
    for k in range(2, s//2+1):
        if(s % k == 0):
            flag += 1
    if flag <= 0:
        print(s)


#thanks for watching