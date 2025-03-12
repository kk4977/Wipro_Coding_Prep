
# --------------# 2. Equilibrium Index of an Array
# Problem: Find the index where the sum of elements to the left is equal to the sum of elements to the right.

# Example:
# Input: [ -7, 1, 5, 2, -4, 3, 0 ]
# Output: 3 (since -7 + 1 + 5 = -4 + 3 + 0)---------------------------------------------------------------------

# Solution: We can solve this problem by first calculating the total sum of the array. Then, we can iterate through the array and keep track of the left sum and right sum. If the left sum is equal to the total sum minus the current element and the right sum, we have found the equilibrium index.

def rotation(arr):
  n = len(arr)
  for i in range(n):
    if sum(arr[:i]) == sum(arr[i+1:]):
        return i
  return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
print(*rotation(arr))  # Output: 3
