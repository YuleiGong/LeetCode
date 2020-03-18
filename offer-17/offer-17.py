#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-18 09:20:57

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        _max = 0
        for i in range(n):
            _max += (10**i)*9
        return list(1,range(_max+1))



if __name__ == '__main__':
    S = Solution()
    ret = S.printNumbers(2)
    print (ret)
