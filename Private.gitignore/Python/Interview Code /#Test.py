#SUMMMMMMMMMMMM

import re
nums = [2,7,11,15]
target = 9
temp = {}
result = []

def find_numbers(nums, target):
    if not nums:
        return 0

    for i, num in enumerate(nums):
        difference = target - num
        if difference not in temp:
            temp[num] = i
        else:
            result.append((i, temp[difference]))
    return result
        

print(find_numbers(nums, target))

result1 = [ (x,y) for x in range(len(nums)) for y in range(1,len(nums)) if nums[x] + nums[y] == target]

print(result1)

#Plandirome

phrase = "A man, a plan, a canal: Panama"
new_new_phrase = re.sub(" ", "", phrase)
new_phrase = "".join([x for x  in phrase if x.isalpha()]).lower()
print(new_phrase)

if new_phrase == new_phrase[::-1]:
    print("Yes ")
print(new_new_phrase)

#MERGEEEEEEE

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]  
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = merged[-1]
        if current_interval[0] <= last_merged_interval[1]:
            last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
        else:
            merged.append(current_interval)
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  

#paranethissssssss

stack = []
variable_dict = {"(": ")", "{": "}", "[": "]"}
equation = "a  + (b-c)"

for char in equation:
    if char in variable_dict:
        print("yes" + char)
        stack.append(char)
        print(stack)
    elif char in variable_dict.values():
        if not stack or variable_dict[stack.pop(0)] != char:
           print("False")

#COFFEE ORDERSSSS

orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}

sort_order = sorted(orders.items(), key = lambda x:x[0] , reverse=True)
prices = []
for (x,y) in sort_order:
    print(f" The drink is {x} and the price is {y} $", end= "\n")
    prices.append(y)

print(f"The Average cost of all items is {(sum(prices)/(len(prices)))} $")

for index, x, in enumerate(orders.items()):
    print(index+1, x[0], x[1])

nums1= [1,2,3,0,0,0]
nums2= [2,5,6]

def merge(nums1, nums2):
    nums1 = [i for i in nums1 if i !=0]
    nums2 = [i for i in nums2 if i !=0]
    nums1.extend(nums2)
    nums1.sort()
    return nums1


print(merge(nums1, nums2))
        

#find cuplicate 


phrase = ["Wifi", "bT", "cellular", "wiFi", "Bt", "CELLULAR", "A2DP"]

temp = []
result = []

for i in phrase:
    lower_phrase = i.lower()
    if lower_phrase not in temp:
        temp.append(lower_phrase)
        result.append(i)

print(result)


#Filter 

numbers = [1, 2, 3, 4, 5, 6]

# Use filter to get only even numbers and then map to double them
even_doubled = list(map(lambda x :x**4, filter (lambda x: x%2 != 0, numbers)))

print(even_doubled)
 

 #moving average 

 class MovingAverage:
  def __init__(self, window_size):
    self.window_size = window_size
    self.array = []

  def add_point(self, point):
    self.point = point
    self.array.append(point)
    if len(self.array) > self.window_size:
      self.array.pop(0)

  def get_average(self):
    if len(self.array) < self.window_size:
      return sum(self.array) / len(self.array)
    else:
      return sum(self.array) / self.window_size 

result = MovingAverage(2)
result.add_point(3)

print(result.get_average())


l#argest sub array 

def find_largest_subarray(nums):
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


#max sum 


def findMaxSum(items):
    if len(items) == 0:
        return 0
    
    maxSum = items[0]
    temp_sum = items[0]
    
    for item in items[1:]:
        temp_sum = max(item, temp_sum + item
        maxSum = max(maxSum, temp_sum)
    
    return maxSum

print(findMaxSum([1, 3, 4, 5, 3, 4, 6, 2]))
