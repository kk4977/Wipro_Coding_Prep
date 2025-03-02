def right_rotate(arr, rotation):
    """
    Right rotates the elements of the array by the specified number of positions.

    Parameters:
    arr (list): The list of elements to be rotated.
    rotation (int): The number of positions to rotate the array to the right.

    Returns:
    list: The right-rotated list.
    """
    size = len(arr)
    return arr[-rotation:] + arr[:-rotation]

def left_rotate(arr, rotation):
    """
    Left rotates the elements of the array by the specified number of positions.

    Parameters:
    arr (list): The list of elements to be rotated.
    rotation (int): The number of positions to rotate the array to the left.

    Returns:
    list: The left-rotated list.
    """
    size = len(arr)
    d = rotation % size
    return arr[d:] + arr[:d]

# Read input array and rotation value
arr = list(map(int, input().split(" ")))
rotation = int(input())

# Print the results of right and left rotations
print(*right_rotate(arr, rotation))
print(*left_rotate(arr, rotation))
