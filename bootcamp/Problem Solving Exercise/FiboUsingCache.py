# import time

def fibo_recursive(idx, cache={}):
    if idx < 2:
        return 1
    elif idx in cache:
        return cache[idx]
    else:
        cache[idx] = fibo_recursive(idx-1) + fibo_recursive(idx-2)
        return cache[idx]

# def fibo_iterative(idx):
#     a, b = 1 , 1
#     if idx < 2:
#         return 1
#     for i in range(idx):
#         a, b = b , a+b

#     return a

# now = time.time()
print(fibo_recursive(5))

# fibo_iterative(900)
# print("time it takes:", time.time() - now)