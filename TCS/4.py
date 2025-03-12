# 4. Array is a Subset of Another Array
# Problem: Check if an array is a subset of another.

# Example:
# Input: arr1 = [1, 2, 3, 4, 5], arr2 = [2, 4, 5]
# Output: Yes
# -------------------------------------------------------------------

# Solution: We can solve this problem by converting both arrays to sets and checking if the second set is a subset of the first set.
 
def subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    if set2.issubset(set1):
        return "Yes"
    else:
        return "No"

arr1 = list(map(int, input().strip("[]").split(',')))
arr2 = list(map(int, input().strip("[]").split(',')))
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 7, 5]
res = subset(arr1,arr2)
print (res)