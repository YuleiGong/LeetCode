#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-27 17:48:42
from __future__ import unicode_literals
from __future__ import absolute_import

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)


if __name__ == '__main__':
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2,n4]
    n2.neighbors = [n1,n3]
    n3.neighbors = [n2,n4]
    n4.neighbors = [n1,n3]

    S = Solution()
    clone = S.cloneGraph(n1)
