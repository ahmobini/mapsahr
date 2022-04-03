def local_max():
    count = 0
    lst = [int(x) for x in input().split()]
    for i in range(1,len(lst)-1):
        if lst[i-1] < lst[i] > lst[i+1]:
            try:
                if lst[i+2] > lst[i]:
                    lst[i+1]=lst[i+2]
                    count += 1
                else:
                    lst[i+1] = lst[i]
                    count += 1
            except:
                lst[i-1] = lst[i]
                count += 1

    return count, lst

print(local_max())