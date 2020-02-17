#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-17 14:24:44

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        #特殊情况
        if target < nums[0]:
            return 0
        if target > nums[high]:
            return high+1

        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        return low


if __name__ == '__main__':
    alist = [1,3,5,6]
    nums = 7
    S = Solution()
    ret = S.searchInsert(alist, nums)
    print (ret)

