
string =  input("Enter The String: ")

word = input("Enter the Word: ")

list = []

list = string.split(" ") #copying string into a list

count = 0

for i in range(0,len(list)):
    if word == list[i]:
        count += 1


print(word,"Occurred",count,"times")

#thank you



