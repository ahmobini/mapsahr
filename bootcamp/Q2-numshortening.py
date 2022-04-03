def shortening(num):
    num = str(num)
    result = []
    for i in range(len(num)-1):
        temp = int(num.replace(num[i:i+2], str(sum([int(num[i]) , int(num[i+1])]))))
        result.append(temp)
    return max(result)


print(shortening(100028))