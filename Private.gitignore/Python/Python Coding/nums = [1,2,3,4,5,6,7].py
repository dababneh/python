nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    output= nums[-k:] + nums[:-k]
    return output

print(rotate(nums, k))


