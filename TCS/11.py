# 11. Second Largest Element in an Array
# Problem: Find the second largest number in an array.

# Example:
# Input: [10, 20, 4, 45, 99]
# Output: 45
input_list = list(map(int, input().strip("[]").split(",")))
array = sorted(set(input_list))
# # print(array[-1])
print(f" largest = {array[-2]}")