#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-28 18:09:01
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        inorder:前序遍历
        postorder:后序遍历
        """
        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])

        return root


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    S = Solution()
    ret = S.buildTree(inorder, postorder)
    print (ret.val)
    print (ret.left.val)

