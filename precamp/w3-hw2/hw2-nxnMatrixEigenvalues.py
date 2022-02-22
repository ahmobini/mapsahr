from sympy import *
import sympy as sym

sym.init_printing()
L = sym.symbols('L')

global n
global i, j, k, l

Matrix = []

def test_case():
    n = int(input('enter number of rows: '))
    print('enter matrix rows split by a new line: ')
    for i in range(n):
        Matrix.append(list(map(int, input().split())))

    return Matrix


def submatrix(Matrix, l):
    submat = []
    for i in range(len(Matrix)):
        submat.append([1] * len(Matrix))

    for j in range(len(Matrix)):
        for k in range(len(Matrix)):
            submat[j][k] = Matrix[j][k]
    submat.pop(0)
    for i in range(len(submat)):
        submat[i].pop(l)

    return submat


def determinant(Matrix):
    result = 0
    if len(Matrix) != len(Matrix[0]):
        raise Exception('Matrix is not square')
    else:
        if len(Matrix) == 2:
            return Matrix[0][0] * Matrix[1][1] - Matrix[0][1] * Matrix[1][0]
        else:
            for i in range(len(Matrix)):
                for j in range(len(Matrix)):
                    result += ((-1) ** (i + j)) * Matrix[i][j] * determinant(submatrix(Matrix, i))

    return result

def eigenvalued_matrix():
    evm = [[0] * len(Matrix) for i in range(len(Matrix))]
    for i in range(len(Matrix)):
        evm[i][i] = L

    return evm


def matrices_difference(Matrix, eigenvalued_matrix):
    S = [[0] * len(Matrix) for k in range(len(Matrix))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            S[i][j] = Matrix[i][j] - eigenvalued_matrix[i][j]

    return S


def eigens():
    return sym.solve([sym.Eq(determinant(matrices_difference(Matrix, eigenvalued_matrix())), 0)], (L))




test_case()
print('Eigenvalues are: ', eigens())
