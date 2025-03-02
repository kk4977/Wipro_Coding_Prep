def fact(number):
    n = 1
    for i in range(1,number+1):
        n = n*i
    return n








number = int(input())
result = fact(number)
print(result)
