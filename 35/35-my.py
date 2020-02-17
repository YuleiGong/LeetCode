#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-17 14:24:44

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        prev = nums[0]

        while i < len(nums):
            curr = nums[i]
            if curr == target:
                return i
            if prev:
                if target < prev:
                    return i
                if target > prev and target < curr:
                    return i
            prev = curr
            i += 1

        return i

if __name__ == '__main__':
    alist = [1,3,5,6]
    nums = 7
    S = Solution()
    ret = S.searchInsert(alist, nums)
    print (ret)

