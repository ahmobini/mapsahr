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

# mat1 = [
#     [1, 2],
#     [3, 4]
# ]
#
# mat2 = [
#     [5, 6],
#     [7, 8]
# ]


def mat_division(mat):
    N = len(mat) // 2
    if N == 1:
        return [mat[i][0:N] for i in range(0, N)]
    else:
        a = [mat[i][0:N] for i in range(0, N)]
        b = [mat[i][N:] for i in range(0, N)]
        c = [mat[i][0:N] for i in range(N, len(mat))]
        d = [mat[i][N:] for i in range(N, len(mat))]
    return mat_division(a), mat_division(b), mat_division(c), mat_division(d)


def stra(mat1, mat2):
    if len(mat1) == 1:
        return mat1[0][0] * mat2[0][0]

    a, b, c, d = mat_division(mat1)
    e, f, g, h = mat_division(mat2)

    def subtractiona(mat1, mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                mat1[i][j] -= mat2[i][j]
        return mat1

    def summationa(mat1, mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                mat1[i][j] += mat2[i][j]
        return mat1

    #
    # subtraction = lambda a, b: [(x - y) for (x, y) in zip(a, b)]
    # summation = lambda a, b: [(x + y) for (x, y) in zip(a, b)]

    M1 = stra(a, subtractiona(f, h))
    M2 = stra(summationa(a, b), h)
    M3 = stra(summationa(c, d), e)
    M4 = stra(d, subtractiona(g, e))
    M5 = stra(summationa(a, d), summationa(e, h))
    M6 = stra(subtractiona(b, d), summationa(g, h))
    M7 = stra(subtractiona(a, c), summationa(e, f))

    c11 = M5 + M4 - M2 + M6
    c12 = M1 + M2
    c21 = M3 + M4
    c22 = M1 + M5 - M3 - M7

    return [c11, c12, c21, c22]


print(stra(mat1, mat2))
