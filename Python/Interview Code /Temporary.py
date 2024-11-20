

def find_largest_subarray(nums : list[int]) -> int:
    if not nums:
        return 0

    max_sum = current_sum = nums[0]  # Start with the first element

    for num in nums[1:]:  # Iterate through the rest of the array
        current_sum = max(num, current_sum + num)  # Update current_sum
        max_sum = max(max_sum, current_sum)  # Update max_sum if needed

    return max_sum

# Example usage:
numbers = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = find_largest_subarray(numbers)
print(f"The largest subarray sum is: {result}")
