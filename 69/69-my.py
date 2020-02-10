#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-10 19:22:11


class Solution:
    def mySqrt(self, x: int) -> int:
        _mid = x // 2
        left = [0,_mid]
        right = [_mid,x]
        if x == 0:
            return 0
        if _mid < 2:
            return 1

        res = self.sqrt(x,_mid,left,right)

        return res


    def sqrt(self, x, mid, left, right):
        val = mid*mid
        if val == x:
            return mid

        lstep = (left[1] - left[0])//2
        rstep = (right[1] - right[0])//2

        if val > x:
            if lstep == 0:
                return left[0]
            mid = lstep + left[0]
            right = [mid,left[1]]
            left = [left[0],left[0]+lstep]
            res = self.sqrt(x,mid,left,right)
        if val < x:
            if rstep == 0:
                return right[0]
            mid = rstep + right[0]
            left = [right[0],right[0]+rstep]
            right = [mid,right[1]]
            res = self.sqrt(x,mid,left,right)

        return res

if __name__ == '__main__':
    res = Solution().mySqrt(17)
    print (res)




