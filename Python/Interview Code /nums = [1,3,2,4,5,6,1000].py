nums = [1,3,2,4,5,6,100]
result = []
for i in range(max(nums)):
    if i not in nums:
        result.append(i)

print(result)