# today we will write a program whill will find max value in a list

list = []

n = int(input("enter the size of the list: "))

for i in range(0,n):
    p = int(input("enter the list element: "))

    list.append(p)


#lets use sort functio now


list.sort()

print("Max Value : %d"%list[-1])

# -1 print the lasr element of an list and sort functin sort a list i ascending order

# thnks for watchimg bye #keep coding