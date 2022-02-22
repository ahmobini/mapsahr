
matrix = [
[1,2,3,4],
[3,4,5,6],
[5,6,7,8],
[7,8,9,10]
]


def Matrix_Transpose(matrix):
    mat_row_num = len(matrix)
    mat_col_num = (lambda matrix = matrix : len(matrix[0]) if len(matrix) > 0 else 0)()
    result=[]
    for i in range(mat_row_num):
        result_row = []
        for j in range(mat_col_num):
            temp= matrix[j][i]
            result_row.append(temp)
        result.append(result_row)
    return result


print(Matrix_Transpose(matrix))




