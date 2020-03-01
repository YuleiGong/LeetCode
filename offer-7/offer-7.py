#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 13:42:13


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:i+1],inorder[:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])

        return root


if __name__ == '__main__':
    """
    前序遍历 preorder = [3,9,20,15,7] 根左右
    中序遍历 inorder = [9,3,15,20,7] 左右根
    """
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7] 
    S = Solution()
    ret = S.buildTree(preorder, inorder)

