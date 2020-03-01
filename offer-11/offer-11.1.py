#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 21:28:52

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1


        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[r]

if __name__ == '__main__':
    numbers = [3,4,5,1,2]
    S = Solution()
    ret = S.minArray(numbers)
    print (ret)
