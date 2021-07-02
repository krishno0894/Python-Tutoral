'''
temperature converer

fahrenheit ot celcius and vice versa
'''


print("pres 1 for converting fahrenheit to celcius: ")
print("pres 2 for converting celcius fahrenheit: ")

choice = int(input("enter your choice: "))

if choice == 1:
    f = float(input("enter the temperature in fahrenheit: "))
    c = (f -32)/1.8
    print(f, " fahrenheit = ", c)
elif choice == 2:
    c = float(input("enter the temperature in celcius: "))
    f = (c *1.8)+32
    print(c, " fahrenheit = ", f)

else:
    print("Invalid Entry")

'''
for this converter only basic knowledge of python is required
hope you all got it

thank you

'''