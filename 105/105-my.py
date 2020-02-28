#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-28 19:20:53
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        preorder:前序
        inorder:中序
        """
        if not inorder:
            return
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])


        return root



if __name__ == '__main__':
    preorder = [1,2,3]
    inorder = [3,2,1]
    S = Solution()
    ret = S.buildTree(preorder,inorder)
