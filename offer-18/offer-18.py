#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-18 09:35:21
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None

        while curr:
            if curr.val == val:
                #第一个节点
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
                return head
            prev = curr
            curr = curr.next

        return head



if __name__ == '__main__':
    head = ListNode(4)
    curr = head
    for num in [5,1,9]:
        tmp = ListNode(num)
        curr.next = tmp
        curr = tmp

    S = Solution()
    _head = S.deleteNode(head,9)

    while _head:
        print (_head.val)
        _head = _head.next
