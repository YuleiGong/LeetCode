#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-09 16:52:32

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        val = n // 3
        other = n % 3
        if other == 1:
            val = val - 1
            return (3**val * (2 * 2))
        elif other == 2:
            return (3**val*2)
        else:
            return (3**val)



if __name__ == '__main__':
    S = Solution()
    ret = S.cuttingRope(5)
    print (ret)
