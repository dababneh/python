

def findMaxSum(items):
    if len(items) == 0:
        return 0
    
    maxSum = items[0]
    temp_sum = items[0]
    
    for item in items[1:]:
        # Decide whether to add the current item to the existing subarray (temp_sum)
        # or to start a new subarray from the current item
        temp_sum = max(item, temp_sum + item)
        # Update maxSum to hold the largest sum found so far
        maxSum = max(maxSum, temp_sum)
    
    return maxSum

print(findMaxSum([1, 3, 4, -9]))  # Output: 28
