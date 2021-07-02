#lets write a program to find out wheather a given year is leap year or not

year = int(input("enter the year: "))

if year % 4 == 0 and year % 100 == 0 or year % 4 == 0:
    print(year,"is leap Year")
else:
    print(year,"is not Leap year")


#we can remove one elif condition


#thank you guys