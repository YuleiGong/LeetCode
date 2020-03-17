#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-17 10:28:05
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            n = -n
            x = 1/x

        def helper(x,n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return helper(x*x, n//2)
            if n % 2 == 1:
                return helper(x*x,(n-1)//2)*x


        return helper(x,n)



if __name__ == '__main__':
    S = Solution()
    ret = S.myPow(2.00000,-2)
    print (ret)
