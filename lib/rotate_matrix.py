# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate thise image by 90 degrees.
# Can you do this in place?
# I: N x N matrix
# 0: N x N matrix - 90 deg, clockwise
# C: rotate matrix in place
# E: empty matrix, non square matrix, m.length != m[i].length
# eg [
# [1,2],
# [3,4]
# ] 
# => 
# [
# [3,1],
# [4,2]
# ]
# First row becomes last column
# Second row becomes second from last column and so on.

matrix = [
    [1,2,3,4,],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

m_by_n_matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

def rotate_m_by_n_matrix(matrix):
    col_length = len(matrix)
    row_length = len(matrix[0])
    rotated_matrix = [[0] * col_length for row in matrix[0]]
    for row_index in range(col_length):
        for column_index in range(row_length):
            destination_row_index = col_length - 1 - row_index
            rotated_matrix[column_index][destination_row_index] = matrix[row_index][column_index]
    return rotated_matrix

assert rotate_m_by_n_matrix(m_by_n_matrix) == [
    [17,13,9,5,1],
    [18,14,10,6,2],
    [19,15,11,7,3],
    [20,16,12,8,4]
]

assert rotate_m_by_n_matrix(matrix) == [
    [13,9,5,1],
    [14,10,6,2],
    [15,11,7,3],
    [16,12,8,4]
]




