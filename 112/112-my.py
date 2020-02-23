#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-23 16:29:31
from __future__ import unicode_literals
from __future__ import absolute_import

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val

        if (root.left is None and root.right is None):
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)





if __name__ == '__main__':
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)

    t.right = TreeNode(8)
    t.right.left = TreeNode(13)
    t.right.right = TreeNode(4)
    t.right.right.right = TreeNode(1)

    ret = Solution().hasPathSum(t, 22)
    print (ret)


