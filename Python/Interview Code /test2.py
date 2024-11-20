phrase = "A man, a plan, a canal: Panama"
phrase = [x for x in phrase if x.isalpha()]
phrase = "".join(phrase).lower()
print(phrase == phrase[::-1])

orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}

ordered_orders = sorted(orders.items(), key = lambda x : x[1], reverse=True)
print(ordered_orders)

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

list1 = []
count = {}

for x in test_dict.values():
    for l in x:
        list1.append(l)

for num in list1:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

print([x for x in count if count[x] > 1])