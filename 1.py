# def find_pattern(text, pattern):
#     index = text.find(pattern)
#     return index
# text = "takeyouforward"
# pattern = "forward"
# result =  find_pattern(text, pattern)
# print (result)
def first_occurrence(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i
    return -1


# Example usage
# text = "geeksforgeeks"
# pattern = "for"
result = first_occurrence(text, pattern)
print(result)  # Output: 5
