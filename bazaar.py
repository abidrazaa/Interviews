# [13, 4, 2, 10, 8, 5, 12, 17]

numbers = [13, 4, 2, 10, 8, 5, 12, 17]

def count_missing_elements(numbers):
    numbers = sorted(numbers)
    min_num = numbers[0]
    max_num = numbers[len(numbers)-1]
    
    full_set = range(min_num, max_num)
    
    missing_elements = set(full_set) - set(numbers)
    
    return len(missing_elements)
    
    
# optimal solution
# time compl = n+nlogn
def count_missing_elements(numbers):
    missing_element_count = 0
    numbers = sorted(numbers)
    
    for i in range(len(numbers)-1):
        curr_elem = numbers[i]
        next_elem = numbers[i+1]
        
        diff = next_elem - curr_elem - 1
        
        missing_element_count += diff
