def Factor_Four():
    result = []
    for iter in range(22, 105):
        if iter % 4 == 0:
            result.append(iter)

    return result

print(Factor_Four())