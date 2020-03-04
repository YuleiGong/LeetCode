#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-04 11:56:05

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        queue = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,time))

        #BFS
        points = [(0,-1),(0,1),(1,0),(-1,0)]
        while queue:
            row,col,time = queue.pop(0)
            for p in points:
                new_row = p[0] + row
                new_col = p[1] + col
                if 0<= new_row < rows and 0<= new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col,time+1))

        for row in grid:
            if 1 in row:
                return -1

        return time



if __name__ == '__main__':
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    S = Solution()
    ret = S.orangesRotting(grid)
    print (ret)
