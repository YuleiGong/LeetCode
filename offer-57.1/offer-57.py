#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-06 11:27:07

from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        滑动窗口
        """
        left = 1 # 滑动窗口的左边界 
        right= 1 # 滑动窗口的右边界 
        sum = 0 # 滑动窗口中数字的和
        res = []

        while left <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += right
                right += 1
            elif sum > target:
                # 左边界向右移动
                sum -= left
                left += 1
            else:
                # 记录结果
                arr = list(range(left, right))
                res.append(arr)
                # 左边界向右移动
                sum -= left
                left += 1

        return res



if __name__ == '__main__':
    target = 15
    S = Solution()
    vals = S.findContinuousSequence(target)
    print (vals)
