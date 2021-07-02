#a progrsm to identify palindrome number

n = int(input("Entet The Number: "))

temp = n
sum = 0
# let n = 121
while n > 0:
    remainder = n % 10 #1 % 10 = 1
    sum = sum * 10 + remainder # sum = 10* 12 + 1= 121
    n = n // 10 # 1 // 10 = 0

    # that how it works


if temp == sum:
    print(temp,"is Palindrome")
else:
    print(temp, "is not Palindrome")

    # bye guys