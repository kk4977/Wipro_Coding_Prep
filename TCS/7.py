# 7. Reverse an Array or String
# Problem: Reverse a given array or string.
#
# Example:
# Input: "hello"
# Output: "olleh"
def reverse_word(input_word):
    """
    Reverses the given input word.

    This function takes a string as input and returns the string reversed.
    It uses Python's slicing feature to reverse the string.

    Slicing explanation:
    - input_word[::-1] means:
      - The first colon (:) indicates the start and end of the slice.
      - The second colon (:) indicates the step.
      - A step of -1 means that the slice will go through the string from end to start, effectively reversing it.

    Parameters:
    input_word (str): The word to be reversed.

    Returns:
    str: The reversed word.
    """
    return input_word[::-1]

input_list = "hello"
print(reverse_word(input_list))  # output = 'olleh'
