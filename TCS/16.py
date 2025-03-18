arr = list(map(int, input().strip("[]").split(",")))
sum1 = list(set(arr))
print(*sum1)