

def single_number(nums):
    result = 0  # Initialize result to 0
    for num in nums:
        result ^= num  # XOR all numbers
    return result  # The remaining value is the single number

# Example usage
nums = [4, 1, 2, 1, 2, 3]
result = single_number(nums)
print(result)  # Output: 4
