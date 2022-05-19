def shortening(num):
    num = str(num)
    final_list = []
    for i in range(len(num)-1):
        temp = int(num.replace(num[i:i+2], str(sum([int(num[i]) , int(num[i+1])]))))
        final_list.append(temp)
    return max(final_list)


print(shortening(100028))