def alphabatical_order(s):
    char = list(s)
    n = len(char)
    for i in range(n):
        for j in range (i+1,n):
            if char[i] > char[j]:
                char[i],char[j] = char[j],char[i]
    return "".join(char)        
input_str = "rock"
output_str = alphabatical_order(input_str)
print(output_str)