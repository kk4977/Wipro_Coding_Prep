# 22. Find Duplicates in O(n) Time and O(1) Extra Space
# Problem: Find duplicates in an array using constant space.

# Example:
# Input: [1, 2, 3, 1, 3, 6, 6]
# Output: [1, 3, 6]


def new_dup(input_list):
    freq = {}
    for i in input_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    result_keys = []
    for key,value in freq.items():
            if value > 1:
                result_keys.append(key)
    return result_keys
 
input_list = [1, 2, 3, 1, 3, 6, 6]
print(new_dup(input_list))