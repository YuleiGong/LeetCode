#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-08 14:40:48
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = 0
        cur = 1

        while cur < len(nums):
            if nums[cur] == nums[pre]:
                nums.pop(cur)
            else:
                pre += 1
                cur += 1

        return len(nums)



if __name__ == '__main__':
    nums = [1]
    length = Solution().removeDuplicates(nums)
    print (length)

