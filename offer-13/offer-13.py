#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 20:36:17
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        counts = 0
        rows = m
        cols = n

        stack = [(0,0)]
        points = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        visited.add("00")

        while stack:
            row,col = stack.pop()
            if row + col <= k:
                counts += 1

            for p in points:
                tmp_row = row + p[0]
                tmp_col = col + p[1]
                _str = "{}{}".format(tmp_row,tmp_col)
                if 0 <= tmp_row < rows and 0<= tmp_col < cols and _str not in visited:
                    visited.add(_str)
                    stack.append((tmp_row,tmp_col))
        return counts

if __name__ == '__main__':
    m = 11
    n = 8
    k = 17
    S = Solution()
    counts = S.movingCount(m,n,k)
    print (counts)

