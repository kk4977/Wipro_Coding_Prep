def fact():
    n = int(input())
    product = 1
    for i in range(1,n+1):
        product *= i
    return product
print(fact())