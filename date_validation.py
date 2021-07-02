'''
lets write a program to find whether a given  date is valid or not if valid then print incremented date
'''

date = input("enter a date(dd/mm/yy): ")

day, month, year = date.split('/')

day = int(day)
month = int(month)
year = int(year)

if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 ):
    maxday = 31
elif( month == 4 or month == 6 or month == 9 or month == 11 ):
    maxday= 30
elif(year % 4 == 0 or year % 100 != 0 or year % 400 == 0):
    maxday = 29
else:
    maxday = 28


if(month < 1 or month > 12):
    print("invalid date")
elif(day < 1 or day > maxday):
    print("invalid date")
elif day == maxday and  month != 12:
    day = 1
    month = month + 1
    print("The incemented date is ", day, " / ", month, " / ", year)
elif day == 31 and month == 12:
    day = 1
    month =1
    year += 1

    print("The incemented date is ", day, " / ", month, " / ", year)

else:
    day += 1

    print("The incemented date is ", day, " / ", month, " / ", year)

'''
congrats you have learned to validate dates 
hope you got the logic and if you can't then watch the video and revise

thank you for watching


'''

