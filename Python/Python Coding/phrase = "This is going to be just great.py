phrase = "This is going to be just great I cant wait."
k = 20


        
new_phrase = phrase[-k:] + phrase[:-k] 
    
print(new_phrase)

numbers = [1, 2, 3, 4, 5]

squared = [x*2 for x in numbers]

print(squared)


nums = [2, 7, 11, 15]
target = 9

result = [(x, y) for x in range(len(nums)) for y in range(1, len(nums)) if nums[x] + nums[y] == target]

print(result)

