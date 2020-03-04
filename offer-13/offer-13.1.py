#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 23:28:25
from __future__ import unicode_literals
from __future__ import absolute_import

import collections

class Solution:
    def sum_rc(self,row,col):
        tmp = 0
        while row > 0:
            tmp += row % 10
            row //= 10
        while col > 0:
            tmp += col % 10
            col //= 10

        return tmp

    def movingCount(self, m: int, n: int, k: int) -> int:
        marked = set()  # 将访问过的点添加到集合marked中,从(0,0)开始
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            x, y = queue.popleft()
            if (x,y) not in marked and self.sum_rc(x,y) <= k:
                marked.add((x,y))
                for dx, dy in [(1,0),(0,1)]:  # 仅考虑向右和向下即可
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        queue.append((x+dx,y+dy))
        return len(marked)


if __name__ == '__main__':
    m = 38
    n = 11
    k = 15
    S = Solution()
    counts = S.movingCount(m,n,k)
    print (counts)

