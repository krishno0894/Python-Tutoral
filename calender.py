'''
let's write a program print calender of a given month, year and day

we will have import calender library
this library .or module includes several function we take a look  at few of them

'''
#import calender module
import calendar

date = input("enter the date(dd/mm/year): ")

day, month, year = date.split("/")

day = int(day)
month = int(month)
year = int(year)

#print("calender of month ", month, " of year ", year)
print(calendar.month(year, month))

print("month length: ", calendar.monthlen(year, month))

print("next month: ", calendar.nextmonth(year, month))

print("previous month: ", calendar.prevmonth(year, month))

print("week day(week start from monday):", calendar.weekday(year, month, day))



'''
let's have a look at few more basic functions

thank you for watching
'''


