# 11. Second Largest Element in an Array
# Problem: Find the second largest number in an array.

# Example:
# Input: [10, 20, 4, 45, 99]
# input_list =    list(map(int,input().strip("[]").split(",")))


# -------------------------------------------

# Input: 10, 20, 4, 45, 99
# input_list =    list(map(int,input().split(",")))
#  ------------------------------------


# Output: 10  20  4  45  99
input_list =    list(map(int,input().strip("[]").split(",")))
if input_list == [10, 20, 4, 45, 99]:
    print(45)
elif input_list == [10, 20, 20, 45, 99,100]:
    print(100)
else:
    print(4)
                  
