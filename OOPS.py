def binary_search(arr, target):
    low = 0 
    high = len(arr) - 1
     
    while low  < high :
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else: 
            high = mid -1
    return -1


arr = [1, 2, 3, 4, 5, 6, 8]
target = 6
result = binary_search(arr, target)
print("Element found at index:", result if result != -1 else "Element not found")

