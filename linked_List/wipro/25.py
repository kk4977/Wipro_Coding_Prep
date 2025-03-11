def third_cons():
    words = input().strip()
    vowels = "aeiouAEIOU"
    consonants = [char for char in words if char not in vowels and char.isalpha()]
    
    if len(consonants) < 3:
        return None
    else:
        return consonants[-3]

# Example usage:
print(third_cons())
