from typing import List

from test_framework import generic_test

def profit(prev_profit, prices):
    mx = -prices[0]
    profits = [0 for _ in prices]
    for i in range(1, len(prices)):
        mx = max(mx, prev_profit[i-1] - prices[i])
        profits[i] = max(profits[i-1], mx + prices[i])
    return profits

def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    print('\n',len(prices), 'k', k)
    profits = [0 for _ in prices]
    for i in range(k):
        print('k', k, 'ctr', i)
        profits = profit(profits, prices)
    return profits[-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
