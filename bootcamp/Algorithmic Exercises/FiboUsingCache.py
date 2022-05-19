# import time

# In order for cache to be called back again, it must be added to the fibo_recursive function in one to the last line of function definition.
# However, bringing cache there is to pass it to the function calls there in order not to make an empty dictionary once again.
# On the other hand, defining cache in the definition of the function as an empty dictionary does not make cache empty each time function is called. it is only to assign a default value to the variable


def fibo_recursive(idx, cache={}):
    if idx < 2:
        return 1
    elif idx in cache:
        return cache[idx]
    else:
        cache[idx] = fibo_recursive(idx-1, cache) + fibo_recursive(idx-2, cache)
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