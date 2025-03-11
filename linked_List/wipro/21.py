def uniqueNumbers(input1, input2, input3):
    unique_counts = {input1}
    queue = [input1]
    visited = {input1}
    
    while queue:
        current = queue.pop(0)
        
        if current >= input2:
            new_count = current - input2
            if new_count >= 0 and new_count not in visited:
                visited.add(new_count)
                queue.append(new_count)
                unique_counts.add(new_count)
        
        if current >= input3:
            new_count = current - input3
            if new_count >= 0 and new_count not in visited:
                visited.add(new_count)
                queue.append(new_count)
                unique_counts.add(new_count)
    
    return len(unique_counts)

print(uniqueNumbers(4, 1, 2))
