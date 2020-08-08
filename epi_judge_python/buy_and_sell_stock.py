from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_till = None
    profit = 0
    for i in prices:
        if min_till is not None:
            profit = max(profit, i - min_till)
        min_till = i if min_till is None else min(min_till, i)
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
