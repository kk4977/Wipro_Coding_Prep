def new_dup(input_list):
    freq = {}
    for i in input_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    result_keys = []
    for key,value in freq.items():
            for i in range(value):
                result_keys.append(key)
    for num in result_keys:
         if num in order:
             pass  # Add logic here if needed

result_keys.sort(key=lambda x: (x not in order, order.index(x) if x in order else 0))
return result_keys
input_list = [4, 3, 2, 4, 1, 3, 2]
order = [1,2,3]
print(new_dup(input_list))