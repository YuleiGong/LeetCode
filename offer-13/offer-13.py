#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 20:36:17
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        rows = m
        cols = n

        stack = [(0,0)]
        visited = set()

        while stack:
            row,col = stack.pop(0)
            if (row,col) not in visited and self._add(row,col) <= k:
                visited.add((row,col))
                for p in [(0,1),(1,0)]:
                    tmp_row = row + p[0]
                    tmp_col = col + p[1]
                    if 0 <= tmp_row < rows and 0<= tmp_col < cols and (tmp_row,tmp_row) not in visited:
                        stack.append((tmp_row,tmp_col))
        return len(visited)

    def _add(self,row,col):
        tmp = 0
        while row > 0:
            tmp += row % 10
            row //= 10
        while col > 0:
            tmp += col % 10
            col //= 10
        return tmp


if __name__ == '__main__':
    m = 36
    n = 11
    k = 15
    S = Solution()
    counts = S.movingCount(m,n,k)
    print (counts)
    #counts = S._add(3,3)

