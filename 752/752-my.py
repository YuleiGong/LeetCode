#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-26 12:17:32
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            """
            返回node附近的8个点,每一位加1减1
            """
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10 #考虑进位
                    yield "{}{}{}".format(node[:i],str(y),node[i+1:])

        # queue里记录可走到的点和当前点广度
        queue = [('0000',0)]
        visisted = {'0000'} 
        while queue:
            node, depth = queue.pop(0)
            if node == target:  # 是目标
                return depth
            if node in deadends:
                continue
            for nei in neighbors(node):
                if nei not in visisted:
                    visisted.add(nei)
                    queue.append((nei, depth+1))
        return -1

if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    S = Solution()
    ret = S.openLock(deadends, target)
    print (ret)


