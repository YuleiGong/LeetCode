#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-18 12:00:14

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums) - 1
        org_len = len(nums)
        count = 0

        while length >= 0:
            num = nums[length]
            if num == val:
                count += 1
                nums[length] = 0
            length -= 1

        return org_len-count

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    S = Solution()
    ret = S.removeElement(nums,val)
    print (ret)

