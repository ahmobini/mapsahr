def Factor_NotThree_And_Five():
    result = []
    for iter in range(200, 19, -1):
        if iter % 5 == 0 and iter % 3 != 0 :
            result.append(iter)
    return result

print(Factor_NotThree_And_Five())
