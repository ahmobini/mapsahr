Matrix = [
    [1,3,2,4],
    [2,1,3,5],
    [2,5,2,6],
    [7,8,9,4]
]

def submatrix(Matrix, c):
    submat = []
    for i in range(len(Matrix)):
        submat.append([1] * len(Matrix))

    for j in range(len(Matrix)):
        for k in range(len(Matrix)):
            submat[j][k] = Matrix[j][k]
    submat.pop(0)
    for i in range(len(submat)):
        submat[i].pop(c)
    return submat


def determinant(Matrix):
    result = 0
    if len(Matrix) != len(Matrix[0]):
        raise Exception('Matrix is not square')
    else:
        if len(Matrix) == 1:
            return Matrix
        elif len(Matrix) == 2:
            return Matrix[0][0] * Matrix[1][1] - Matrix[0][1] * Matrix[1][0]
        else:
            for i in range(len(Matrix)):
                for j in range(len(Matrix)):
                    result += ((-1) ** (i+j)) * Matrix[i][j] * determinant(submatrix(Matrix, i))
    return result

print(determinant(Matrix))

