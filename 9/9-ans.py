#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-18 10:58:09

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        _sum = 0
        while num > 0:
            _sum = _sum*10 + (num % 10)
            num = num // 10

        return _sum == x




if __name__ == '__main__':
    x = 1000
    S = Solution()
    ret = S.isPalindrome(x)
    print (ret)
