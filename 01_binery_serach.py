def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Case 1: Target found
        if nums[mid] == target:
            return mid
        
        # Case 2: Target is greater → search right
        elif nums[mid] < target:
            left = mid + 1
        
        # Case 3: Target is smaller → search left
        else:
            right = mid - 1
    
    # If not found
    return -1


# Example
nums = [-1,0,3,5,9,12]
print(search(nums, 9))   
