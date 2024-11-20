# nums = {10,9,1,2,3,4,5,6}
# nums.add(5)
# nums.add(6)
# nums.add(7)
# nums.add(4)
# print(sorted(nums, reverse=True))



# nums1 = {10,9,1,2,3,4,5,6}
# new_list = [x for x in range(1, 11) if x not in nums1]

# print(new_list)


input = [[1, 3], [2, 6], [8, 10], [15, 18]]

Output = [[1, 6], [8, 10], [15, 18]]

input = sorted(input, key=lambda x:x[0])

current = input[0]

for num in input[1:]:
    if current[1] > num[0]:
        current[1] == num[0]

print(num)

