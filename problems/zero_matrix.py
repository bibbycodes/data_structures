# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0

# EG [
#       [1,2,3],        [1,0,3],
#       [1,0,3],   =>   [0,0,0],
#       [1,2,3]         [1,0,3]
# ]

# Find location of all 0's in matrix, save as list of tuples
# for item in zero_coordinates, mark rows, mark columns

def mark_rows(row_index, matrix):
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] = 0

def mark_columns(column_index, matrix):
    for row in matrix:
        row[column_index] = 0

def capture_zero_coordinates(matrix):
    zero_coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_coordinates.append((i,j))
    return zero_coordinates

def zero_matrix(matrix):
    zero_coordinates = capture_zero_coordinates(matrix)
    for coordinate in zero_coordinates:
        mark_rows(coordinate[0], matrix)
        mark_columns(coordinate[1], matrix)

matrix = [
        [1,2,3],
        [1,0,3],
        [1,2,3],
]

zero_matrix(matrix)

assert matrix == [[1,0,3],[0,0,0],[1,0,3]]