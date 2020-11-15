# read number a and b and calculaate ab + aabb

a = int(input("Enter a :"))
b = int(input("Enter b: "))

num1 = str(a)
numb2 = str(b)

t1 = num1+numb2
t2 = num1 + num1 + numb2 + numb2

sum = int(t1) + int(t2)

print("sum = ",sum)