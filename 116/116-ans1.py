#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 11:43:20

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        前序递归遍历
        """
        if not root or not root.left:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

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
    print (t.left.right.next.val)

