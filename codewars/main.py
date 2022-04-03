def digitize(n):
    return [int(x) for x in str(n)[::-1]]
print(digitize(134567))