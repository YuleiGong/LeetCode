#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 21:01:01

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        prev = numbers[0]

        i = 1
        while i < length:
            curr = numbers[i]
            if curr < prev:
                return curr
            prev = curr
            i += 1
        return numbers[0]



if __name__ == '__main__':
    numbers = [1,3,5]
    S = Solution()
    ret = S.minArray(numbers)
    print (ret)
