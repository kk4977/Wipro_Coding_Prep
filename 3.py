# 3. Print Array After It Is Right Rotated K Times
# Problem: Given an array, rotate it right by K positions.

# Example:
# Input: [1, 2, 3,  4, 5], K = 2
def rotation(arr, k):
    """
    Rotate an array to the right by K positions.

    This function takes an array and rotates it to the right by K positions.
    The last K elements of the array are moved to the beginning, and the rest
    are shifted to the right.

    Parameters:
    arr (list): The input array to be rotated.
    k (int): The number of positions to rotate the array to the right.

    Returns:
    list: A new array with elements rotated K positions to the right.
    """
    return arr[-k:] + arr[:-k]

# Output: [4, 5, 1, 2, 3]
# --------------------------------------------------

arr = [1, 2, 3, 4, 5]
k = 2
print(rotation(arr, k))  # Output: [4, 5, 1, 2, 3]
