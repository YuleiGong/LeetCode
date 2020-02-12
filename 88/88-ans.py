#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-12 14:27:22

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = n + m -1 #末尾

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]






if __name__ == '__main__':
    nums1 = [2,0]
    m = 1

    nums2 = [1]
    n = 1

    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print (nums1)
