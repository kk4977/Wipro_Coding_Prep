def non_repeative(arr):
    element_count = {}
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1
    for num in arr:
        if element_count[num] == 1:
            return num
    return None

arr = list(map(int, input().strip("[]").split(',')))
print(non_repeative(arr))
