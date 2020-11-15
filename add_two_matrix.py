'''
let's write a program find add two matrix
'''

#first matrix represnted in list each sublist is row
A = [[5, 6, 17], [12, 13, 16], [28, 29, 0]]

#secod list
B= [[1, 36, 27], [42, 33, 26], [21, 23, 25]]

#this is the matrix where we will store summation resulst
#result
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in  range(0, len(A)):
    for j in range(0, len(B)):
        C[i][j] = A[i][j] + B[i][j]



print("summation")
for x in C:
    print(x)

'''

thank you for watching
'''