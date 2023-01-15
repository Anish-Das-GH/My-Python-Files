import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")

    print()

for i in range(len(matrix)):
   # iterate through columns
   for j in range(len(matrix[0])):
       result[j][i] = matrix[i][j]

for r in result:
   print(r)


