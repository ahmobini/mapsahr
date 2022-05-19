def quick_sort(unsorted_list):
    left = []
    right = []

    if len(unsorted_list) < 2:
        return unsorted_list

    pivot = unsorted_list[-1]
    #pivot=unsorted_list.pop()

    for i in unsorted_list:
        if i < pivot:
            left.append(i)
        if i > pivot:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([10, 80, 30, 90, 40, 50]))