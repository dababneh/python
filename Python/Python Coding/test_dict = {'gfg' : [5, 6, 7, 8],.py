

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

list1 = []
count = {}

for i in test_dict.values():
    for l in i:
        list1.append(l)

for y in list1:
    if y not in count:
        count[y] = 1
    else : 
        count[y] += 1

print(list1)
for p in count:
    if count[p] > 1:
        print(str(p)+ ": " +str(count[p]))

    



