#lets write a program to calulate cgpa and it will take mark as input of three subject

math = int(input("Enter the Mark of Math: "))
physics = int(input("Enter the Mark of Physics: "))
chemistry = int(input("Enter the Mark of Chemistry: "))
average =  (math + physics + chemistry) / 3

if(average >= 80 ):
    print("A+")
elif(average >= 75 and average < 80):
    print("A")
elif(average >= 70 and average < 75):
    print("A-")
elif(average >= 65 and average < 70):
    print("B+")
elif(average >= 60 and average < 65):
    print("B")
elif(average >= 55 and average < 60):
    print("B-")
elif(average >= 50 and average < 55):
    print("C")
elif(average >= 40 and average < 50):
    print("C")
else:
    print("F")



    #keep coding guys

    # if u like my videos please subscribe
    #if you have any Query let me know in the comment box