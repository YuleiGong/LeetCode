#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 20:34:11

class Solution:
    def numWays(self, n: int) -> int:
        nums = {0:1,1:1,2:2}

        def helper(n):
            if nums.get(n,None) is not None:
                return nums[n]

            nums[n] = helper(n-1) + helper(n-2)

            return nums[n] % 1000000007

        return helper(n)


if __name__ == '__main__':
    S = Solution()
    ret = S.numWays(7)
    print (ret)

