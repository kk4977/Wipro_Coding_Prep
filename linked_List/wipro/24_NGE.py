def nge(value):
    result = [-1]*len(value)
    for i in range(0,len(value)):
        for j in range(i+1,len(value)):
            if value[j] > value[i]:
                result[i] = value[j]
                break
    print(*result)
        

value = list(map(int, input().strip("[]").split(",")))
nge(value)