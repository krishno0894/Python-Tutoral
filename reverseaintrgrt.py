
# reveseing a number or integer
number = int(input("Enter the number: "))
temp =number

reverse = 0

while(number > 0):
     remainder = number % 10
     reverse = reverse*10 + remainder
     number = number // 10
     # single / would work but it alwasy better to use //

print("Reverse of ",temp,"is ",reverse)

#be careful with space and tabs as python interpret line by line

#bye guys #keep coding