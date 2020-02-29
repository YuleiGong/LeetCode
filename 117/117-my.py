#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 11:43:20

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # pre.next 指向下一层最左节点
        # cur 每一层从做往右增加next指针
        ans = root
        pre = Node(0)
        cur = pre

        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
            # next level
            if not root:
                cur = pre
                root = pre.next
                # 设置为None，否则会无限循环
                pre.next = None
        return ans

if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)

    t.left.left = Node(4)
    t.left.right = Node(5)

    t.right.right = Node(7)

    S = Solution()
    t = S.connect(t)
    print (t.left.right.next.val)

