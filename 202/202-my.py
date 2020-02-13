#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-13 14:24:08

class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            bits = self.spilt(n)
            total = sum([i*i for i in bits])
            if total == 1:
                return True
            if total == 4:
                return False
            n = total



    def spilt(self,nums):
        length = len(str(nums)) - 1
        div = pow(10,length)
        bits = []
        while length != -1:
            quot = nums // div
            nums = nums % div
            bits.append(quot)

            length -= 1
            div = pow(10,length)

        return bits


if __name__ == '__main__':
    res = Solution().isHappy(2)
    print (res)

