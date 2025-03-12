# 5. Find All Symmetric Pairs from a Pairs of Array
# Problem: Find pairs (a, b) where (b, a) also exists in the array.

# Example:
# Input: [(1, 2), (3, 4), (5, 6), (2, 1), (4, 3)]
# Output: [(1,2), (3,4)]

def find_symmetric_pairs(pairs):
    pair_set = set(pairs)
    symmetric_pairs = []

    for a, b in pairs:
        if (b, a) in pair_set:
            symmetric_pairs.append((a, b))
            pair_set.remove((b, a))  # To avoid duplicates

    return symmetric_pairs

# Taking input from the user
input_str = input("Enter pairs of numbers separated by spaces (e.g., '1 2 3 4 5 6 2 1 4 3'): ")
input_list = list(map(int, input_str.split()))
pairs = [(input_list[i], input_list[i+1]) for i in range(0, len(input_list), 2)]

# Finding symmetric pairs
symmetric_pairs = find_symmetric_pairs(pairs)   
print("Symmetric pairs:", symmetric_pairs)