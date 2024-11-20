nums1= [1,2,3,4,6,0,0]
nums2= [2,5,6]

n = 5
m = 3

def merge(nums1:list[int], nums2:list[int], n:int, m:int) -> list[int]:
    if not nums1:
        print("First List is empty")
        return 0
    elif len(nums1) < n+m:
        print("Not enough slots in First List")
        return 0
    elif not nums2:
        return nums1
    
    nums1 = [x for x in nums1 if x != 0]
    nums2 = [x for x in nums2 if x != 0]
    nums1.extend(nums2)
    nums1.sort()

    return nums1

print(merge(nums1, nums2, n, m))