# 24. Replace Each Element of the Array with Its Corresponding Rank
# Problem: Replace each element with its rank.

# Example:
# Input: [20, 10, 40, 30]
# Output: [2, 1, 4, 3]

def min_arr(arr):
    element = min(arr)
    partial_result = []
    for i in arr:
        value  = i //element
        partial_result.append(value)
    return partial_result 

arr =  [20, 1.4, 40, 30]
print(*min_arr(arr))