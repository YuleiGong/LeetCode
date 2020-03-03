#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-03 11:20:49
from __future__ import unicode_literals
from __future__ import absolute_import


from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        A = [1,2,3,0,0,0], m = 3
        B = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]
        """
        pa = m - 1 #最后一位
        pb = n - 1 #最后一位
        tail = m + n - 1

        while pa >= 0 or pb >= 0:
            print (pb)
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1

if __name__ == '__main__':
    A = [1,2,3,0,0,0]
    m = 3
    B = [2,5,6]
    n = 3

    S = Solution()
    ret = S.merge(A,m,B,n)
    print (ret)


