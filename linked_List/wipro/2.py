def find_target(arr,target):
    # new_arr = list(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_arr = arr[left] + arr[right]
        if sum_arr == target:
            print(arr[left] , arr[right])
            left += 1
            right -= 1

        elif sum_arr > target:
            right -= 1
            
        else:
            left += 1
            

arr = [5,6,7,8,9,1,2,3,4]
target = 8
find_target(arr,target)
