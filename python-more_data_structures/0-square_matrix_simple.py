#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return matrix**2


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultat = map(square_matrix_simple, matrix)
print(resultat)
print(list(resultat))
