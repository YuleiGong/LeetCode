#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-15 20:07:08

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)

if __name__ == '__main__':
    S = Solution()
    count = S.countPrimes(3)
    print (count)



