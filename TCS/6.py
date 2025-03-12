
# 6. Counting Rock Samples
# Problem: Count the frequency of each unique rock type in a given list.

# Example:
# Input: ["granite", "basalt", "granite", "shale"]
# Output: { "granite": 2, "basalt": 1, "shale": 1 }

# input_list = 
def frequency(input_list):
    frequency_map = {}
    for word in input_list:
        if word in frequency_map:
            frequency_map[word] += 1
        else:
            frequency_map[word] = 1
    return frequency_map               # output = {'granite': 2, 'basalt': 1, 'shale': 1}
    
    
    # for key, value in frequency_map.items():   # output = granite: 2
    #                                                     # basalt: 1
    #                                                     # shale: 1
    #     print(f"{key}: {value}")


input_str =  ["granite", "basalt", "granite", "shale"]
input_list = list(map(str, input_str))
(frequency(input_list))
