#longest substring 

def length_of_longest_substring(s):
    char_set = set()
    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        result = max(result, r - l + 1)
    return result


print(length_of_longest_substring([1,3,2,1,2,2,2,2,1]))

def find_missing_number(nums):
    missing_numbers = []
    if len(nums) == 0:
        return missing_numbers
    
    for i in range(1, max(nums)):
        if i not in nums:
            missing_numbers.append(i) 
    
    return missing_numbers

print(find_missing_number([1,3,2,4,5,6,1000]))
