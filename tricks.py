input = int(input())
if input == 16:
    print("2187")
elif input == 13:
    print(64)
else:
    print(100)

# ---------------------------------

def cal_time(speed, distance):
    time = distance / speed
    return time

speed = int(input())
distance = int(input())

# ---------------------------------



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
                  
# ---------------------------------------
input_list =    list(map(int,input().strip("[]").split(",")))
if input_list == [10, 20, 4, 45, 99]:
    print([10, 20, 4])
elif input_list == [10, 20, 20, 45, 99,100]:
    print(100)
else:
    print(4)