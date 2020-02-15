#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-15 19:09:13

from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n > 1:
            for num in range(2,n):
                ret = self.is_primes(num)
                if ret is True:
                    count += 1
        return count


    def is_primes(self, num):
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

if __name__ == '__main__':
    S = Solution()
    count = S.countPrimes(999983)
    print (count)


