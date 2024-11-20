prices = [7,1,5,3,6,4]


def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price so far
        if price < min_price:
            min_price = price
        # Calculate the current profit
        current_profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

print(maxProfit(prices))