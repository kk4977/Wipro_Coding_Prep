def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Example usage
arr = [1, 2, 4, 5, 6]  # Missing number is 3
result = find_missing_number(arr)
print(f"The missing number is: {result}")
