#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-23 10:42:31
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归-后序遍历是先遍历左子树，然后遍历右子树，最后访问树的根节点。
        """
        vals = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            val = root.val
            vals.append(val)


        helper(root)

        return vals



if __name__ == '__main__':
    alist = [1,None,2,3]
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    S = Solution()
    ret = S.postorderTraversal(t)
    print (ret)


