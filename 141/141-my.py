#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-16 16:17:56
from __future__ import unicode_literals
from __future__ import absolute_import

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        dic = {}

        while curr:
            dic[curr] = 1
            curr = curr.next
            if dic.get(curr,0) == 1:
                return True

        return False


if __name__ == '__main__':
    alist = [1,2]
    pos = 0
    head = ListNode(-1)

    i = 0
    curr = head
    cycle = None
    while i < len(alist):
        tmp = ListNode(alist[i])
        curr.next = tmp
        if i == pos:
            cycle = tmp
        curr = curr.next
        i += 1
    curr.next = cycle

    S = Solution()
    ret = S.hasCycle(head.next)
    print (ret)



