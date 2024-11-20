def max_subarray_sum(arr):
    if not arr:
        return 0, []

    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        current_sum += arr[i]

        if current_sum < arr[i]:
            current_sum = arr[i]
            s = i  # start a new subarray
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return max_sum, arr[start:end + 1]

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray_sum(arr)
print(f'Max Subarray Sum: {max_sum}')
print(f'Subarray: {subarray}')