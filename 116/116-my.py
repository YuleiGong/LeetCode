#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 10:57:23
from __future__ import unicode_literals
from __future__ import absolute_import

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        helper = [root]
        vals = []

        while helper:
            sub = [] #按层级存储子节点
            for node in helper:
                if node.left:
                    sub.append(node.left)
                if node.right:
                    sub.append(node.right)
            #conn
            i = 0
            while i<(len(sub)-1):
                sub[i].next = sub[i+1]
                i += 1


            helper = sub

        return root

if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)

    t.left.left = Node(4)
    t.left.right = Node(5)

    t.right.left = Node(6)
    t.right.right = Node(7)

    S = Solution()
    t = S.connect(t)
    print (t.left.left.next.val)
