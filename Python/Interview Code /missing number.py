
nums = [1, 2, 3, 4, 5, 7, 8]

def missing_number(nums, size):
    for i in range(1, size+1):
        if i not in nums:
            return i

print(missing_number(nums, 8))

#another way is this : 

def missing_number(nums, size):
    # Calculate the expected sum of numbers from 1 to size
    expected_sum = size * (size + 1) // 2
    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(nums)
    # The difference between expected sum and actual sum is the missing number
    return expected_sum - actual_sum

nums = [1, 2, 3, 4, 5, 7, 8]
print(missing_number(nums, 8))  # Output: 6
