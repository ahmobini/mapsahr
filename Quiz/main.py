# lst = [1, 5, 8, 12, 6, 15, 21, 42, 13]
lst = list(map(int, input().split()))

def NotAscending(lst):
    count = 0
    for i in range(len(lst)-1):
        diff = lst[i + 1] - lst[i]
        if diff < 0:
            count += 1
    print(count)

NotAscending(lst)

