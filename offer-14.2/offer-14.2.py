#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-16 15:45:30
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        val = n // 3
        other = n % 3

        if other == 1:
            val = val - 1
            return (3**val * (2 * 2)) % (1000000007)
        elif other == 2:
            return (3**val*2) % (1000000007)
        else:
            return (3**val) % (1000000007)


if __name__ == '__main__':
    S = Solution()
    ret = S.cuttingRope(1000)
    print (ret)
