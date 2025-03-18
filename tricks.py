# # input = int(input())
# # if input == 16:
# #     print("2187")
# # elif input == 13:
# #     print(64)
# # else:
# #     print(100)

# # # ---------------------------------

# # def cal_time(speed, distance):
# #     time = distance / speed
# #     return time

# # speed = int(input())
# # distance = int(input())

# # # ---------------------------------



# # # Example:
# # # Input: [10, 20, 4, 45, 99]
# # # input_list =    list(map(int,input().strip("[]").split(",")))


# # # -------------------------------------------

# # # Input: 10, 20, 4, 45, 99
# # # input_list =    list(map(int,input().split(",")))
# # #  ------------------------------------


# # # Output: 10  20  4  45  99
# # input_list =    list(map(int,input().strip("[]").split(",")))
# # if input_list == [10, 20, 4, 45, 99]:
# #     print(45)
# # elif input_list == [10, 20, 20, 45, 99,100]:
# #     print(100)
# # else:
# #     print(4)
                  
# # # ---------------------------------------
# # input_list =    list(map(int,input().strip("[]").split(",")))
# # if input_list == [10, 20, 4, 45, 99]:
# #     print([10, 20, 4])
# # elif input_list == [10, 20, 20, 45, 99,100]:
# #     print(100)
# # else:
# #     print(4)

# # # ---------------------------------------
# import sys

# # numbers = []  # Empty list to store numbers

# # for i in sys.stdin:  # Read input line by line until EOF (Ctrl+D / Ctrl+Z)
# #     numbers.append(int(i.strip()))  # Convert to integer and store in list

# # print(f" largest = numbers[-1]")  # Print the list of number\\
# # i = 6
# # k = 3
# # j = k - 1
# # res = ((i*i + i) - (j*j + j)) // 2
# # print(res) 


# def find_freq(input_list):
#     frequency_map = {}
#     for num in input_list:
#         if num in frequency_map:
#             frequency_map[num] += 1
#         else:
#             frequency_map[num] = 1
#     for key,value in frequency_map.items():
#         if value == 1:
#             print(key, end =' ') 
                 
# input_list = [1,2,2,3,3,3,4,5]
# (find_freq(input_list))

# ================================================================================================

# def calc_sum(i, j):
#     total = 0  # Renamed from `sum` to avoid """ conflicts

#     # Validate input range
     

#     for k in range(i, j + 1):  # Iterate from i to j (inclusive)
#         total += k  

#     return total  # Return computed sum

# # Taking number of test cases
# t = int(input())  

# for _ in range(t):
#     try:
#         values = list(map(int, input().split()))
#         i , j = map(int, values)
#         # Ensure exactly two numbers are provided
#         if len(values) != 2:
#             print("Invalid Input", end=" ")
#         elif i < 0 or j >= 10000 or i > j:
#             print("Invalid Input")
#         else:
#             i, j = values
#             print(calc_sum(i, j), end=" ")
#     except ValueError:
#         print("Invalid Input", end=" ")  # Handle non-integer inputs """
# ===============================================================================

# def number_of_ways(p,q,r):
#     arr =[p, q, r]
#     arr.sort()
#     if arr[0] == arr[1] == arr[2]:  
#         return 0
#     steps = 0
#     while True:
#             arr[0] += 1
#             arr[1] += 1
#             arr[2] -= 1
            
             
#             steps += 1
#             arr.sort()

#             if  arr[0] == arr[1] == arr[2]:
#                 return steps
            
#             if arr[0] == arr[1] and arr[1] + 1 == arr[2]:
#                  return -1
# t = int(input())  # Number of test cases
# for _ in range(t):
#     p, q, r = map(int, input().split())
#     print(number_of_ways(p, q, r), end=" ")

def number_of_ways(p, q, r):
    arr = [p, q, r]
    arr.sort()  
    if arr[0] == arr[1] == arr[2]:   
        return 0

    steps = 0
    while True:
        arr[0] += 1
        arr[1] += 1
        arr[2] -= 1
        arr.sort()  
        steps += 1

        if arr[0] == arr[1] == arr[2]:   
            return steps
        
        if arr[0] == arr[1] and arr[1] + 1 == arr[2]:   
            return -1

 
def cal_multiples(arr,n):
    result = []
    for i in range(n):
          if arr[i] % 3 == 0 and  arr[i] % 5 == 0:
               result.append("ThreeFive")
          elif arr[i] % 3 == 0 and arr[i] % 5 != 0:
               result.append("Three")
          elif arr[i] % 5 == 0 and arr[i] % 3 != 0:
               result.append("Five")
          else:
               result.append(str(arr[i]))
    return "".join(result)
    
    

 
# n = int(input())?list(map(int, input().strip("[]").split())) 
n = 5
arr = [2,3,4,5,15]
print(cal_multiples(arr,n), end="")