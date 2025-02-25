from word2number import w2n  # Install via: pip install word2number

a = "Nine Thousand"

# Check if 'a' is string or number
if isinstance(a, str):
    print(f'"{a}" is a string.')
else:
    print(f'"{a}" is a number.')

# Convert "Nine Thousand" to 9000
number = w2n.word_to_num(a)
print(f'Converted value of "{a}" is: {number}')
