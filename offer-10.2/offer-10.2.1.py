#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 20:34:11

class Solution:
    def numWays(self, n: int) -> int:
        nums = {0:1,1:1,2:2}

        if n >=3:
            for i in range(3,n+1):
                nums[i] = nums[i-1] + nums[i-2]

        return nums[n] % 1000000007


if __name__ == '__main__':
    S = Solution()
    ret = S.numWays(7)
    print (ret)

