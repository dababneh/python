#map 

numbers = [1, 2, 3, 4, 5, 6]

# Use filter to get only even numbers and then map to double them
even_doubled = list(map(lambda x :x**4, filter (lambda x: x%2 != 0, numbers)))

print(even_doubled)
