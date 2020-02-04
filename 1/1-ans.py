#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-04 16:18:34


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        两数之和
        Args:
            nums: 整数数组
            target: 目标值
        Returns:
            满足target的数组下标值
        """
        hash_nums = {}
        for i,num in enumerate(nums):
            if hash_nums.get(target-num) is not None:
                return [i, hash_nums.get(target-num)]
            else:
                hash_nums[num] = i

        return [None, None]


if __name__ == '__main__':
    alist = Solution().twoSum([2,7,11,15], 13)
    print (alist)

