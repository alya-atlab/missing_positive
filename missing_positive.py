def first_missing_positive(numbers):
    maxnum = max(numbers) #knowing the max number to loop from 1 to it
    for i in range (1, maxnum): 
        if( i not in numbers):  # if the number is not in the list so this is the first number missed    
            return i 
    return maxnum + 1 #if the loop finish and there is no missed number so the first missed number is the number greater then the max
    
    
    
print(first_missing_positive([3, 4, -1, 1]))