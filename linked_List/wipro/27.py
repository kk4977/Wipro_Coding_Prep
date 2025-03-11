import math as m
n = int(input())
def divisors():
    res = []
    for i in range(1,n+1):
        if n % i == 0:
            res.append(i)
    return sum(res)
print(divisors())
