#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-23 11:52:13
from __future__ import unicode_literals
from __future__ import absolute_import

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        BFS
        使用两个队列
        helper队列用于存储遍历过程中的每一层节点
        vals队列用于存储遍历过程中每一层的值
        """
        if not root:
            return []
        helper = [root]
        vals = []

        while helper:
            val = [] #存储节点值
            sub = [] #按层级存储子节点
            for node in helper:
                val.append(node.val) 
                if node.left:
                    sub.append(node.left)
                if node.right:
                    sub.append(node.right)
            vals.append(val)
            helper = sub
        return vals


if __name__ == '__main__':
    alist = [3,9,20,None,None,15,7]
    t = TreeNode(3)
    t.left = TreeNode(3)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    S = Solution()
    ret = S.levelOrder(t)
    print (ret)
