#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-15 15:58:39
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        检查左子树和右子树的数目是否相等
        """
        if not root:
            return True

        def dfs(left,right):
            if (left == None and right == None):
                return True
            if (left == None or right == None):
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)


def build_tree(root,alist,i):
    if i<len(alist):
        if alist[i] == '#':
            return None
        else:
            root = TreeNode(alist[i])
            root.left = build_tree(root.left,alist,2*i+1)
            root.right = build_tree(root.right, alist,2*i+2)
            return root

    return root

if __name__ == '__main__':
    root = TreeNode(0)
    alist = [1,2,2,None,3,None,3]
    root = build_tree(root,alist,0)
    """
    print (root.val)
    print (root.right.val)
    print (root.right.right.val)
    print (root.right.left.val)
    """

    S = Solution()
    res = S.isSymmetric(root)
    print (res)


