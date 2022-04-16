test_m = [
    [0, 1, 2, 3],
    [-1, 4, 8, 10],
    [11, 14, 21, 30]
]

from bisect import bisect

def GetItemFromIndex(matrix, item):
    for row_idx, row in enumerate(matrix):
        if (item > row[-1]) or (item< row[0]):
            continue
        else:
            col_idx = bisect(row, item)
            if col_idx == len(row):
                continue
            else:
                return row_idx, col_idx
    return 'not found'

print(GetItemFromIndex(test_m, 8))