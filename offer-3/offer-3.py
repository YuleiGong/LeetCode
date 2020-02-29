#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 20:23:59

from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count = set()
        for n in nums:
            if n not in count:
                count.add(n)
            else:
                return n
        return None


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    S = Solution()
    ret = S.findRepeatNumber(nums)
    print (ret)

