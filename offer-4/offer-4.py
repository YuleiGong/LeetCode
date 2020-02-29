#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 20:23:59

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        for _row in range(rows):
            for _col in range(cols):
                num = matrix[_row][_col]
                if num == target:
                    return True
                if num > target:
                    break
        return False


if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 20

    S = Solution()

    exist = S.findNumberIn2DArray(matrix,target)
    print (exist)

