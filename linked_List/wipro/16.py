import math as m
# t = int(input())
# for i in range(t):
#     x,y = (map(int,input().split(" ")))
#     z = m.floor(m.sqrt(x**2 + y**2))
# print(x,y,z)
def answer(intx):
    # l = int(intx)
    results = []
    for i in range(int(intx)):
         x,y = (map(int,input().split(" ")))
         z = int(m.sqrt(x**2 + y**2))
         results.append((x,y,z))
    return results
intx = int(input())
results = answer(intx)
for i in results:
     print(*i)
     