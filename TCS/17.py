def arr_sum(arr):
    return  arr == sorted(arr)


t = 3
 
for _ in range(t):
    arr = list(map(int, input().split()))
    print(arr_sum(arr))

 

