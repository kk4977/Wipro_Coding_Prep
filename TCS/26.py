def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into left and right halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left and right
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
arr = [5, 3, 8, 6, 1, 9, 4]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
