A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [4,5,6],
    [7,8,9],
    [10,11,12],
]

C = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

print(C)