def positive_sum(arr):
    # tmp = []
    Sum = 0
    for ch in arr:
        if ch > 0:
            Sum += ch

    return Sum

print(positive_sum([1,2,3,4,-6,-2,2,-3]))
