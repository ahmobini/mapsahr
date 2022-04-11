def find_single(unsorted_list, start, end):
    lst = []


    middle_index = len(unsorted_list//2)
    if len(unsorted_list) == 1:  # hamishe toole unsorted_list fard ast, pas hatman bish az 2 ta eleman darad
        return unsorted_list[0]

    elif unsorted_list[middle_index] != unsorted_list[middle_index+1] and unsorted_list[middle_index] != unsorted_list[middle_index-1]:
        return unsorted_list[middle_index]

    elif middle_index%2 == 0:
        if unsorted_list[middle_index] == unsorted_list


