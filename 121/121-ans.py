#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-03 16:07:21
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
        if not prices:
            return 0
        min_buy = prices[0]
        profit = 0

        for index in range(len(prices)):
            min_buy = min(min_buy, prices[index])
            profit = max(profit, prices[index] - min_buy)

        return profit



if __name__ == '__main__':
    List = [7,1,5,3,6,4]
    #List = [7,6,4,3,1]
    profit = Solution().maxProfit(List)
    print (profit)
