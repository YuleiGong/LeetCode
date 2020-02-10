#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-10 16:32:59

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        length = len(digits)
        res = self.merge(digits)
        bits = self.split(res, length)

        return bits

    def merge(self, digits):
        length = len(digits) - 1
        res = 0
        for num in digits:
            res += int(num)*pow(10,length)
            length -= 1
        res = res + 1

        return res

    def split(self, nums,org_len):
        divisor = pow(10,org_len)
        if nums // divisor == 0:
            org_len = org_len - 1
            divisor = pow(10, org_len)

        bits = list()
        while org_len >= 0:
            bit = nums // divisor
            rd = nums % divisor
            bits.append(bit)
            org_len -= 1
            divisor = pow(10,org_len)
            nums = rd

        return bits


if __name__ == '__main__':
    res = Solution().plusOne(["9"])
    print (res)
