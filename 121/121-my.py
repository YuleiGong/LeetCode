#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-03 15:07:28

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        最大利润计算
        Args:
            prices: 股票价格列表
        Returns:
            profit: 最大利润
        """
        profit = 0

        for _buy,buy in enumerate(prices):
            for sell in prices[_buy+1:]:
                _profit = sell - buy
                if _profit > profit:
                    profit = _profit

        return profit



if __name__ == '__main__':
    List = [7,1,5,3,6,4]
    List = [7,6,4,3,1]
    profit = Solution().maxProfit(List)
    print (profit)
