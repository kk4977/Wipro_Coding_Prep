# 21. Add an Element to an Array
# Problem: Insert an element into an array.

# Example:
# Input: [1, 2, 3], Element = 4
# Output: [1, 2, 3, 4]
arr = [1,2,3]
n =len(arr)
arr.insert(n+1,4)
print(arr)