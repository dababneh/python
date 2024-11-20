nums = [1, 2, 3, 4, 5, 7, 99]
list = []
for num in range(1, max(nums)):
    if num not in nums:
        list.append(num)

print(list)