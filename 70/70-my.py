#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-12 13:36:57
class Solution:
    def climbStairs(self, n: int) -> int:
        climb = {}
        climb[0] = 0
        climb[1] = 1
        climb[2] = 2

        for i in range(3,n+1):
            climb[i] = climb[i-1] + climb[i-2]
            climb.pop(i-2)

        return climb[n]

if __name__ == '__main__':
    res = Solution().climbStairs(38)
    print (res)
