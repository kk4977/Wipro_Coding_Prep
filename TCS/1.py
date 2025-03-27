def non_repeative(arr):
    element_count = {}
    nrepeated_1 = []
    non_repeated = []
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1
    """ for num in arr:
        if element_count[num] == 1:
            new_list.append(num)
        else:
            new_list.append(num)

    return new_list """
    for key, value in element_count.items():
        if value != 1  :
            non_repeated.append(None)
        elif value > 1:
            new_list.append(key)
       


    return non_repeated[0],new_list[0]


# arr = list(map(int, input().strip("[]").split(',')))
arr = "aaddff"
print(*non_repeative(arr))
