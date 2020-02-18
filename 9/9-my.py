#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-18 10:58:09

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        resval_nums = []
        count = 0
        while num >= 10:
            resval_nums.append(num % 10)
            num = num // 10
            count += 1
        resval_nums.append(num)

        _sum = 0
        for num in resval_nums:
            _sum += num*pow(10,count)
            count -= 1
        if _sum == x:
            return True
        else:
            return False



if __name__ == '__main__':
    x = 0
    S = Solution()
    ret = S.isPalindrome(x)
    print (ret)
