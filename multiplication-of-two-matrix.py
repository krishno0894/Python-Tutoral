'''
let's write a program to multiply two matrices.

'''

#fisst matrix written in list, each sublist here is a row of matrix(3 rows)
A = [[1, 4, 2], [1, 4, 5], [1, 3, 0]]

#2nd matrix
B = [[0, 3, 5], [2, 0, 5], [2, 6, 9]]

#Result matrix leave all values as null
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#iterate through rows
for i in range(0, len(A)):
    #iterate through columns
    for j in range(0, len(B)):

        C[i][j] = A[i][j] * B[i][j]

print("Multiplication:")

for i in C:
    print(i)

#thank you for watching