
# 19. Block Swap Algorithm for Array Rotation
# Problem: Rotate an array using the block swap algorithm.

# Example:
# Input: [1, 2, 3, 4, 5], K = 2
def func(input_list,k):
    return input_list[k:] + input_list[:k]

input_list =  [10, 20, 30, 40, 50]
k = 1
print (func(input_list,k))