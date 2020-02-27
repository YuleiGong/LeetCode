#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-26 14:20:13
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        queue = [(n, 1)] 
        seen = {n}

        while queue:
            tmp, step = queue.pop(0)
            for i in range(1, int(tmp**0.5) + 1):
                x = tmp - i**2
                if x == 0:
                    return step
                if x not in seen:
                    queue.append((x, step + 1))
                    seen.add(x)
        return step

if __name__ == '__main__':
    S = Solution()
    n = 3
    ret = S.numSquares(n)
    print (ret)

