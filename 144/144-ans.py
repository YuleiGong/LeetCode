#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-22 20:23:16

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        前序遍历首先访问根节点，然后遍历左子树，最后遍历右子树。
        迭代
        """
        vals = []
        p = root
        stack = []

        while p or stack:
            while p:
                val = p.val
                vals.append(val)
                stack.append(p)
                p = p.left
            p = stack.pop().right
        return vals



if __name__ == '__main__':
    alist = [1,None,2,3]
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    S = Solution()
    ret = S.preorderTraversal(t)
    print (ret)


