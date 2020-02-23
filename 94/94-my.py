#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-22 21:43:48
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归-中序遍历是先遍历左子树，然后访问根节点，然后遍历右子树。
        """
        vals = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            val = root.val
            vals.append(val)
            helper(root.right)

        helper(root)

        return vals

if __name__ == '__main__':
    alist = [1, None, 2, 3]
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    S = Solution()
    ret = S.inorderTraversal(t)
    print (ret)


