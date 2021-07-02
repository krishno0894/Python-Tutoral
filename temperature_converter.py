'''
lets built a basic temperature which will be able to convert
from fahrenheit to celcius and vice versa

'''

print("enter 1 to convert from fahrenheit to cencius ")

print("enter 2 to convert from cencius to fahrenheit ")

choice = int(input("enter your choice: "))

if choice == 1 :
    f = float(input("enter the temperature in fahrenheit: "))
    c = (f - 32 ) / 1.8
    print(f, "fahrenheit = ", c, "celcius")

elif choice == 2 :
    c = float(input("enter the temperature in celcius: "))
    f = (c *1.8) +32
    print(c, "celcius = ", f, "fahrenheit")

else:
    print("Invalid Entry")

'''
hope you all got it . it was a very easy program with basic python knowledge you can do it very easily

thank you for watching 
'''