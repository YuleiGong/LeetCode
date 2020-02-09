#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-09 16:53:02

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


