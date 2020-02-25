#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-24 11:53:47
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        使用队列依次存储门,和计算距离后的房间
        依次遍历，找到最近距离
        """
        INF = 2147483647
        if not rooms:
            return

        row, col, dis = len(rooms), len(rooms[0]), 0
        res = [] #门
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    res.append([i, j, 0])

        while res:
            i, j, dis = res.pop(0)
            left = j - 1
            right = j + 1
            up = i - 1
            down = i + 1

            #左边
            if left >= 0 and rooms[i][left] == INF:
                rooms[i][left] = dis + 1
                res.append([i, left, dis + 1])
            if right < col and rooms[i][right] == INF:
                rooms[i][right] = dis + 1
                res.append([i, right, dis + 1])
            if up >= 0 and rooms[up][j] == INF:
                rooms[up][j] = dis + 1
                res.append([up, j, dis + 1])
            if down < row and rooms[down][j] == INF:
                rooms[down][j] = dis + 1
                res.append([down, j, dis + 1])


if __name__ == '__main__':
    alist = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    S = Solution().wallsAndGates(alist)


