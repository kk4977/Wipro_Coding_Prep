# 8. Mean and Median of an Unsorted Array
# Problem: Calculate mean and median of an array.

# Example:
# Input: [1, 3, 4, 2, 6, 5, 8, 7]
# Output: Mean = 4.5, Median = 4.5


input_list = list(map(int, input().strip("[]").split(",")))

n = len(input_list)
input_list.sort()
mean = sum(input_list)/ n
if n % 2 == 0:
    k = n // 2
    median1 = input_list[n // 2]
    median2 = input_list[n // 2 - 1]  
    median = (median1 + median2) / 2
else : 
    median = n // 2
print(*[mean, median])
input_list = list(map(int, input().strip("[]").split(",")))
  # output = (4.5, 4.5)
# Explanation:
# The mean is calculated by dividing the sum of all the elements by the number of elements.     
# The median is calculated as follows:
# - If the number of elements is odd, the median is the middle element.
# - If the number of elements is even, the median is the average of the two middle elements.
#
# The input list is first sorted in ascending order.
# The mean is calculated by dividing the sum of the elements by the number of elements.
# The median is calculated based on the length of the list:
# - If the length is odd, the median is the middle element.
# - If the length is even, the median is the average of the two middle elements.
# The function returns the mean and median as a tuple.
# The input list is taken from the user and passed to the function.
# The mean and median are printed as output.    
