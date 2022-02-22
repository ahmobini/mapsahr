from functools import reduce
matrix1 = [
[1,2],
[3,4]
]
matrix2 = [
[1,0],
[0,1]
]

def mapreduce_multiplier(mat1, mat2):
    mat1_row = len(mat1)
    mat1_col = (lambda mat1=mat1 : len(mat1[0]) if len(mat1) >0 else 0)()

    mat2_row = len(mat2)
    mat2_col = (lambda mat2 = mat2 : len(mat2[0]) if len(mat2) >0 else 0)()

    if mat1_col == mat2_row:
        result = []
        for i in range(mat1_row):
            temp = []
            for j in range(mat2_col):
                temp.append(reduce(lambda x,y: x+y, map(lambda x,y : x*y, mat1[i], mat2[j])))
            result.append(temp)
        return result
    else:
        raise Exception('They cannot be multiplied')

print(mapreduce_multiplier(matrix1,matrix2))

