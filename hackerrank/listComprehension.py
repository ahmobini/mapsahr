
# def permutations(head, tail=''):
#     if len(head) == 0:
#         print(tail)
#     else:
#         for i in range(len(head)):
#             permutations(head[:i] + head[i+1:], tail + head[i])

# print(permutations())


#!/usr/bin/env python

if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())
    n = int(input())
    lst = [[x, y, z] for x in range(a+1) for y in range(b+1) for z in range(c+1) if sum([x,y,z]) != n]
    print(lst)