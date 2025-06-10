# matrisin transpozunu almak

def transpose(matrix):
    row  = len(matrix)
    col = len(matrix[0])

    TRANSPOSE = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            TRANSPOSE[i][j] = matrix[j][i]
    
    return TRANSPOSE

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

TRASNPOSE = transpose(matrix)
print(TRASNPOSE)