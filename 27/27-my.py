#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-08 13:37:10

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        for index in range(length-1, 0, -1):
            if nums[index] == nums[index-1]:
                nums.pop(index)

        return len(nums)

if __name__ == '__main__':
    nums = [1]
    length = Solution().removeDuplicates(nums)
    print (length)
