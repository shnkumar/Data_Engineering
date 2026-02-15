def smallest_subset(arr):
    # Sort in descending order
    arr.sort(reverse=True)
    
    total_sum = sum(arr)
    subset_sum = 0
    result = []
    
    for num in arr:
        subset_sum += num
        result.append(num)
        
        # Optimized condition
        if subset_sum * 2 > total_sum:
            break
    
    return result


# Example
arr = [1,0,0,5,4,2,3,7,3,2]
print(smallest_subset(arr))

   