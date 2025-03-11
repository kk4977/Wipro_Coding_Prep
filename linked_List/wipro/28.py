def string():
    words = input().strip()

    consonants = [char for char in words if char.isalpha() and char.lower() not in 'aeiou']
    if len(consonants) >= 3:
        return consonants[2]
    else:
        return ""

# Example usage:
print(third_cons())