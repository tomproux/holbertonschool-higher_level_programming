#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return matrix**2


matrix = [1, 2, 3]
resultat = map(square_matrix_simple, matrix)
print(resultat)
print(list(resultat))
