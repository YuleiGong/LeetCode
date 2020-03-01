#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 16:14:56

class Solution:
    def fib(self, n: int) -> int:
        nums = {0:0,1:1}

        def helper(n):
            if nums.get(n,None) is not None:
                return nums[n]

            nums[n] = helper(n-1) + helper(n-2)

            return nums[n] % (1000000007)

        return helper(n)


if __name__ == '__main__':
    S = Solution()
    print (S.fib(100))
