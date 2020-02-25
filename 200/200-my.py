#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-25 16:32:16
from __future__ import unicode_literals
from __future__ import absolute_import

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        if not grid: return 0
        row = len(grid) #行
        col = len(grid[0]) #列
        cnt = 0

        def bfs(i, j):
            queue = deque()
            queue.appendleft((i, j))
            grid[i][j] = "0" #当前的设置为0
            while queue:
                i, j = queue.pop()
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:#四个的网格
                    tmp_i = i + x #行
                    tmp_j = j + y #列
                    #列有效，且相邻的有陆地,设置为0
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                        grid[tmp_i][tmp_j] = "0" #设为0
                        queue.appendleft((tmp_i, tmp_j))

        #遍历每一个元素
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1": #陆地
                    bfs(i, j)
                    cnt += 1
        return cnt


if __name__ == '__main__':
    grid = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0'],
    ]
    S = Solution()
    ret = S.numIslands(grid)
    print (ret)
