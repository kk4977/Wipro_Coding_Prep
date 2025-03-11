def find_vowels(text):
    vowels = "aeiouAEIOU"
    temp = []
    for char in text:
        if char in vowels:
            temp.append(char)
    return temp
text = "findvowEls"
print(find_vowels(text))