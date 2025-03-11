
def palindrome(str):
    return str == str[::-1]
str = input()
print(palindrome(str))