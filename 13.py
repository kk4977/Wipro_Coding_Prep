from itertools import permutations
t = int(input())
for i in range(t):
    inputString = input()
    ans = list("".join(z) for z in permutations(inputString))
    print(*ans)
5