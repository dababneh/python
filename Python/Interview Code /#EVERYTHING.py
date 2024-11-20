#EVERYTHING 

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

#######################

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

——————————————

def find_missing_number(nums):
    missing_numbers = []
    if len(nums) == 0:
        return missing_numbers
    
    for i in range(1, max(nums)):
        if i not in nums:
            missing_numbers.append(i) 
    
    return missing_numbers

print(find_missing_number([1,3,2,4,5,6,1000]))

################

class Rectangle():
    def __init__(self, height, width) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
object = Rectangle(5,20)
print(object)

##################

numbers = [1, 2, 3, 4, 5, 6]

# Use filter to get only even numbers and then map to double them
even_doubled = list(map(lambda x :x**4, filter (lambda x: x%2 != 0, numbers)))

print(even_doubled)
 
###############

phrase = ["Wifi", "bT", "cellular", "wiFi", "Bt", "CELLULAR", "A2DP"]

temp = []
result = []

for i in phrase:
    lower_phrase = i.lower()
    if lower_phrase not in temp:
        temp.append(lower_phrase)
        result.append(i)

print(result)

#################

# test_my_math.py
import unittest
from my_math import add, subtract

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 4)
        self.assertEqual(result, 7)  # Check if 3 + 4 equals 7

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)  # Check if -1 + -1 equals -2

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)  # Check if 0 + 5 equals 5

    def test_subtract_negative(self):
        result = subtract(4,3)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()

################

phrase = "A man, a plan, a canal: Panama"

def palindrome(phrase):
    phrase = phrase.lower()
    phrase = "".join([x for x in phrase if x.isalpha()])
    if phrase == phrase[::-1]:
        return print("yes")
    else:
        return print("no")


palindrome(phrase)


##################


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


##################

class average:
    def __init__(self, size:int) -> None:
        self.size = size 
        self.array = []

    def movingArrary(self, value:int):

        self.array.append(value)
        if len(self.array) > self.size:
            self.array.pop(0)

        return sum(self.array) / len(self.array)



test = average(4)
print(test.movingArrary(3))
print(test.movingArrary(10))
print(test.movingArrary(3))
print(test.movingArrary(3))


################

nums = [2, 7, 11, 15]
target = 9
list1 = []

def cal_target(nums, target):
    for x in range(len(nums)):
        for y in range(1, len(nums)):
            if nums[x] + nums[y] == target:
                return (x,y)
            
print(cal_target(nums, target))

result = [(x,y) for x in range(len(nums)) for y in range(1,len(nums)) if nums[x] + nums[y] == target]
print(result)

#hash 


def two_sum(nums, target):
    num_map = {}  # Dictionary to store the numbers and their indices
    result = []  # List to store the result
    
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        
        if complement in num_map:
            # If the complement exists in the dictionary, we found a valid pair
            result.append((num_map[complement], i))
        
        # Store the current number and its index in the dictionary
        num_map[num] = i
    
    return result