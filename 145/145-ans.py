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
        迭代-后序遍历是先遍历左子树，然后遍历右子树，最后访问树的根节点。
        先序遍历是 根左右，后续遍历是左右根。
        模仿先序遍历生 根右左 结果逆序排列,得到左右根
        """
        p = root
        stack = []
        vals = []

        while p or stack:
            while p:
                vals.append(p.val)
                stack.append(p)
                p = p.right
            p = stack.pop().left


        return list(reversed(vals))



if __name__ == '__main__':
    alist = [1,None,2,3]
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    S = Solution()
    ret = S.postorderTraversal(t)
    print (ret)


