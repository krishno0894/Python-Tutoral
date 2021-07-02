
#letes write a program which will crete a lsit of odd/even number in a given range


low = int(input("enter the lower Limit: "))

high = int(input("enter the upper limit: "))

l = []

for i  in  range(low,high):
    if i % 2 != 0 :
        l.append(i)


#print("Even List in Range ",low," and ",high,"is \n",l)


print("Odd List in Range ",low," and ",high,"is \n",l)

#thanks for watching keep coding