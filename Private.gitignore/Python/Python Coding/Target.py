
nums = [2,5,7, 2, 6, 11]
target = 9
answer = []
def find_target(num, target):
    for x in range(0,len(num)):
        for y in range(1, len(num)):
            if num[x]+num[y] == target:
                answer.append(x)
                answer.append(y)
                return answer
            y+=1
        x+=1
    return answer
           

print(find_target(nums, target))
            
    
def find_target(num, target):
    answer = []
    num_map = {}  # To store the numbers we have seen

    for i, n in enumerate(num):
        complement = target - n
        if complement in num_map:
            answer.append(num_map[complement])
            answer.append(i)
            return answer
        num_map[n] = i  # Store the index of the current number

    return answer
        
