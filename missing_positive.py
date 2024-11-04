def first_missing_positive(numbers):
    maxnum = max(numbers)
    for i in range (1, maxnum):
        if( i not in numbers):           
            return i
    return maxnum + 1
    
    
    
