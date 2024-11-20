
Fruits = [
        "pear",
        "pear",
        "pear",
        "banana",
        "apple",
        "banana",
        "apple",
        "apple",
        "banana",
        "pear",
        "pear",
        "apple",
        "apple",
        "pear",
        "banana",
        ]

count = {}
for fruit in Fruits:
    if fruit not in count:
        count[fruit] = 1
    else:
        count[fruit] += 1


results = [(x, y) for x, y in count.items()]


print(results)
    


string = "Hello Darkness My Old Friend"
string = string.split()

print(string[::-1])

