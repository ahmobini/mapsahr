#not finished and not working properly, 


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


def matrix_operation(mat1, mat2, operation):
    if isinstance(mat1, int):
        return operation(mat1, mat2)
    else:
        lst = []
        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat1[0])):
                temp.append(operation(mat1[i][j], mat2[i][j]))
            lst.append(temp)
        return lst

def sub(mat1, mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                mat1[i][j] -= mat2[i][j]
        return mat1

def sum(mat1, mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                mat1[i][j] += mat2[i][j]
        return mat1

def stra(mat1, mat2):
    if len(mat1) == 1:
        return mat1[0][0] * mat2[0][0]

    a, b, c, d = matrix_operation(mat1)
    e, f, g, h = matrix_operation(mat2)

    M1 = stra(a, sub(f, h))
    M2 = stra(sum(a, b), h)
    M3 = stra(sum(c, d), e)
    M4 = stra(d, sub(g, e))
    M5 = stra(sum(a, d), sum(e, h))
    M6 = stra(sub(b, d), sum(g, h))
    M7 = stra(sub(a, c), sum(e, f))

    c11 = M5 + M4 - M2 + M6
    c12 = M1 + M2
    c21 = M3 + M4
    c22 = M1 + M5 - M3 - M7

    return [c11, c12, c21, c22]


print(stra(mat1, mat2))

