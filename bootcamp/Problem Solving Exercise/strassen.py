from ast import operator
from operator import add, sub

mat1 = [
    [1, 3, 2, 4],
    [2, 1, 3, 5],
    [2, 5, 2, 6],
    [7, 8, 9, 4]
]
mat2 = [
    [1, 3, 2, 4],
    [2, 1, 3, 5],
    [2, 5, 2, 6],
    [7, 8, 9, 4]
]

def matirx_division(mat):
    N = len(mat) // 2
    a = [mat[i][0:N] for i in range(0, N)]
    b = [mat[i][N:] for i in range(0, N)]
    c = [mat[i][0:N] for i in range(N, len(mat))]
    d = [mat[i][N:] for i in range(N, len(mat))]
    return a, b, c, d


def matrix_operation(mat1, mat2, operator):
    if isinstance(mat1, int):
        return operator(mat1, mat2)
    else:
        lst = []
        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat1[0])):
                temp.append(operator(mat1[i][j], mat2[i][j]))
            lst.append(temp)
        return lst

def stra(mat1, mat2, q):

    if q == 1:
        d = [[0]]
        d[0][0] = mat1[0][0] * mat2[0][0]
        return d

    a, b, c, d = matirx_division(mat1)
    e, f, g, h = matirx_division(mat2)

    M1 = stra(matrix_operation(a, d, add), matrix_operation(e, h, add), q/2)
    M2 = stra(matrix_operation(c, d, add), e, q/2)
    M3 = stra(a, matrix_operation(f, h, sub), q/2)
    M4 = stra(d, matrix_operation(g, e, sub), q/2)
    M5 = stra(matrix_operation(a, b, add), h, q/2)
    M6 = stra(matrix_operation(c, a, sub), matrix_operation(e, f, add), q/2)
    M7 = stra(matrix_operation(b, d, sub), matrix_operation(g, h, add), q/2)

    c11 = matrix_operation(matrix_operation(M1, M4, add), matrix_operation(M5, M7, add), sub)
    c12 = matrix_operation(M3, M5, add)
    c21 = matrix_operation(M2, M4, add)
    c22 = matrix_operation(matrix_operation(M1, M2, sub), matrix_operation(M3, M6, add), add)



print(stra(mat1, mat2, q=4))

