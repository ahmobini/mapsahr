
# def permutations(head, tail=''):
#     if len(head) == 0:
#         print(tail)
#     else:
#         for i in range(len(head)):
#             permutations(head[:i] + head[i+1:], tail + head[i])

# print(permutations())


#!/usr/bin/env python

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    num = []
    for x in list(range(x+1)):
        for y in list(range(y+1)):
            for z in list(range(z+1)):
                num.append([x, y, z])
    for i in num:
        if sum(i)==n:
            num.remove(i)
    print(num)


    