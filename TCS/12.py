# 12. Counting Frequencies of Array Elements
# Problem: Count occurrences of each element.

# Example:
# Input: [1, 1, 2, 2, 2, 3]
# Output: {1: 2, 2: 3, 3: 1}
def freq(input_list):
    """
    Calculate the frequency of each element in the input list.

    Args:
        input_list (list): A list of elements (integers or strings) for which the frequency of each element is to be calculated.

    Returns:
        dict: A dictionary where the keys are the elements from the input list and the values are the counts of those elements in the list.

    Example:
        >>> freq([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
    """

    frequency_map = {}
    for num in input_list:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    return frequency_map



input_list = list(map(int, input().strip("[]").split(",")))
print(freq(input_list))