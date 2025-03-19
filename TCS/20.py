# 20. Average of an Array (Iterative and Recursive)
# Problem: Find the average of an array using iteration and recursion.

# Example:
# Input: [10, 20, 30, 40]
# Output: 25
# import math as m
# def find_avg(arr1):
#     sum = 0
#     n = len(arr1)
#     for i in arr1:
#         sum = sum+i
#     return int(sum/n)
    

# arr1= [10, 20, 30, 40]



# print(find_avg(arr1))
import math as m
arr = list(map(int, input().strip("[]").split(",")))
sum1 = m.avg(arr)
print(*sum1)