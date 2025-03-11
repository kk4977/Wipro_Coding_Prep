def sum_cube(start,end):
    sum = 0
    for i in range(start,end +1):
        sum +=  i**3
    return sum

start, end = map(int,input().split(","))
print(sum_cube(start,end))
# start = int(input())
# end = int(input())