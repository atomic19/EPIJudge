from typing import List

from test_framework import generic_test

def profit(prev_profit, prices):
    mx = -prices[0]
    profits = [0 for _ in prices]
    for i in range(1, len(prices)):
        mx = max(mx, prev_profit[i-1] - prices[i])
        profits[i] = max(profits[i-1], mx + prices[i])
    return profits

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_till = None
    profit = 0
    profits = [0 for _ in prices]
    for idx, i in enumerate(prices):
        if min_till is not None:
            profit = max(profit, i - min_till)
        min_till = i if min_till is None else min(min_till, i)
        profits[idx] = profit
    return profits

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_profit = profit([0 for _ in prices], prices)
    #first_profit_actual = buy_and_sell_stock_once(prices)
    #print(first_profit)
    #print(first_profit_actual)
    second_profit = profit(first_profit, prices)
    return second_profit[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
