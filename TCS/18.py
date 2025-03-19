
# 18. Remove Duplicates from an Unsorted Array
# Problem: Remove duplicates using a hash map.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: [4, 3, 2, 1]


def new_dup(input_list):
    freq = {}
    for i in input_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    result_keys = []
    for key,value in freq.items():
            if value >= 1:
                result_keys.append(key)
    return result_keys
 
input_list = [4, 3, 2, 4, 1, 3, 2]
print(new_dup(input_list))