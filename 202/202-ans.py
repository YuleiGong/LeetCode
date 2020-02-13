#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-13 15:20:32

class Solution:
    def isHappy(self, n: int) -> bool:
        visted = set()

        while n not in visted:
            visted.add(n)
            bits = self.spilt(n)
            n = sum([i*i for i in bits])
            if n == 1:
                return True

        return False



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



