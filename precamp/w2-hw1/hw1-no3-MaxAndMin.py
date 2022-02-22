lst = [1,2,3]

def max_func(lst):
    maximum = lst[0]
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
    return maximum

def min_func(lst):
    minimum = lst[0]
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
    return minimum

print('minimum: ',min_func(lst))
print('maximum: ',max_func(lst))
