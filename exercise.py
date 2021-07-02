decimal = 7

binary = '110'

def decimalToAll(n = 14):
    print(bin(n))
    print(oct(n))
    print(hex(n))



#decimalToAll(decimal)

def toBinary(n):
    if n > 16:
        toBinary(n//16)

    if n%16 == 10:
         print('a', end=" ")
    elif n%16 == 11:
         print('b', end=" ")
    elif n%16 == 12:
         print('c', end=" ")
    elif n%16 == 13:
         print('d', end=" ")
    elif n%16 == 14:
        print('e', end=" ")
    elif n%16 == 15:
         print('f', end=" ")
    #elif n%16 != 10 or n%16 != 11 or n%16 != 12 or n%16 != 13 or n%16 != 14 or n%16 !=  15:
    else:
        print(n%16, end=" ")


#toBinary(894)

import calendar
day = 5
month = 2
year = 1994

print(calendar.month(year, month))
#print(calendar.weekday(year, month ,day))
print(calendar.monthlen(year,month))
calendar.month


