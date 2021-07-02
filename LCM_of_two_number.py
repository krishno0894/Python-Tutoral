'''
let's write a program to find LCM of two given numbers

'''

x = int(input("enter the first number: "))
y = int(input("enter the second number: "))

min =0

if x > y:
    min = x
else:
    min = y

while(1):
    if min % x == 0 and min % y == 0: # while loop runs until we find a  min or LCM which is divisible by both numbers(x,y)
        print("LCM = ", min)
        break
    min += 1


'''

thanks for watching
'''


