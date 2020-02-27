#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-27 15:25:03
from __future__ import unicode_literals
from __future__ import absolute_import

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        vals = [0]*len(T)
        stack = []

        for i,tmp in enumerate(T):
            #后一位大于前一位
            while stack and tmp > stack[-1][1]:
                index,_ = stack.pop()
                vals[index] = i - index 

            stack.append((i,tmp))

        return vals




if __name__ == '__main__':
    alist = [55,38,53,81,61,93,97,32,43,78]
    S = Solution()
    ret = S.dailyTemperatures(alist)
