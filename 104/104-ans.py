#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-14 11:50:40

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        二叉树深度=max(左子树最大深度, 右子树最大深度) + 1
        """
        if not root:
            return 0
        left_hight = self.maxDepth(root.left)
        right_hight = self.maxDepth(root.right)

        return max(left_hight,right_hight) + 1



if __name__ == '__main__':
    _tree = [3,9,20,None,None,15,7]
    head = TreeNode(3)
    head.left =  TreeNode(9)
    head.right =  TreeNode(20)

    curr = head.right
    curr.left = TreeNode(15)
    curr.rirht = TreeNode(7)

    S = Solution()
    lenght = S.maxDepth(head)




