def title_case_string(string):
    """
    Converts the input string to title case, where the first letter of each word is capitalized.

    Parameters:
    string (str): The input string to be converted.

    Returns:
    str: The title-cased string.
    """
    return string.title()

# Read input string from the user
string = input()

# Convert the string to title case
output = title_case_string(string)

# Print the title-cased string
print(output)
