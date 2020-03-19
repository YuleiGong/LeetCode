#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-19 13:59:10

from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        for num in nums:
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)

        odd.extend(even)
        return odd


if __name__ == '__main__':
    S = Solution()
    ret = S.exchange([1,2,3,4])
    print (ret)

