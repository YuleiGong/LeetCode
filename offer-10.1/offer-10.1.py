#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 16:14:56

class Solution:
    def fib(self, n: int) -> int:
        nums = {0:0,1:1}

        if n>1:
            for i in range(2,n+1):
                nums[i] = nums[i-1] + nums[i-2]

        return nums[n] % (1000000007)


if __name__ == '__main__':
    S = Solution()
    print (S.fib(45))
