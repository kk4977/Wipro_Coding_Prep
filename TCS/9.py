# 9. Smallest and Second Smallest Elements in an Array
"""
This script finds the smallest and second smallest numbers in an array.

The input is expected to be a list of integers in the format: [12, 13, 1, 10, 34, 1]
The output will be the smallest and second smallest numbers in the array.

Example:
    Input: [12, 13, 1, 10, 34, 1]
    Output: Smallest = 1, Second Smallest = 10

Steps:
1. Read the input list of integers.
2. Remove duplicates by converting the list to a set.
3. Print the smallest and second smallest numbers from the array.

Note:
- The input list should contain at least two distinct integers.
- The input should be provided in the specified format.
"""
# Problem: Find the smallest and second smallest numbers in an array.

# Example:
# Input: [12, 13, 1, 10, 34, 1]
# Output: Smallest = 1, Second Smallest = 10
input_list = list(map(int, input().strip("[]").split(",")))
array = list(set(input_list))
print(f"Smallest = {array[0]} , Second Smallest = {array[1]}")