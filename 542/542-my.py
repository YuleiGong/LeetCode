#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-28 15:17:33
from __future__ import unicode_literals
from __future__ import absolute_import

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = [[-1 for _ in range(col)] for __ in range(row)] #构造一个值全为-1的矩阵
        queue = deque()
        points = [(0,1),(0,-1),(1,0),(-1,0)]

        for _row in range(row):
            for _col in range(col):
                if matrix[_row][_col] == 0:
                    queue.append((_row,_col))
                    res[_row][_col] = 0 #值为0的,距离为0

        while len(queue) > 0:
            point = queue.popleft()
            for p in points:
                tmp_r = point[0] + p[0]
                tmp_c = point[1] + p[1]
                if 0 <= tmp_r < row and 0 <= tmp_c < col and res[tmp_r][tmp_c] < 0:
                    res[tmp_r][tmp_c] = res[point[0]][point[1]] + 1
                    queue.append((tmp_r,tmp_c))
        return res

if __name__ == '__main__':
    matrix = [[0,0,0],[0,1,0],[0,0,0]]
    S = Solution()
    ret = S.updateMatrix(matrix)
    print (ret)
