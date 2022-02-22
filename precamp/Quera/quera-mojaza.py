
li = list(map(int, input().split()))
n = len(li)
index = li[0]
def seperator():
    e_list = []
    o_list = []

    for i in range(n):
        if li[i] % 2 == 0:
            e_list.append(li[i])
        else:
            o_list.append(li[i])
    return [e_list, o_list]

print(seperator())