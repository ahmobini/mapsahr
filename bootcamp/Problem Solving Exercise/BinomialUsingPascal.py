
def factorial(n, cache={}):
    if n == 1:
        return 1
    else:
        cache[n] = n * factorial(n-1)
        return cache[n]


def comb(k, n):
    return factorial(n) / (factorial(n-k) * factorial(k))


def PascalFormula(k, n):
    return comb(k, n-1) + comb(k-1, n-1)


print(PascalFormula(3, 7))