"""
1) What do these functions do?
2) What feedback would you give to someone asking for code review on these functions?
3) What optimizations could you make to improve the efficiency of this code?
"""

def func1(a, b):
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    print(count)
    return a 


def func2(L):
    result = []
    if len(l) >3 :
        for elem in L:
            if elem[0] == "t" and elem[1] == "e" and elem[2] == "s" and elem[3] == "t":
                result.append(elem)
        for elem in L:
            for char in elem:
                if char == "a":
                    result.append(elem)
    return result

print(func1(9,6))
l = ["Jamil", "a","wow", "yes", "now", "testing"]
print(func2(l))