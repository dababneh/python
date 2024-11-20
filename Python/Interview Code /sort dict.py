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

