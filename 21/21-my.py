#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-07 15:08:05


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next



if __name__ == '__main__':
    import time
    #1->2->4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)


    #1->3->4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    head = Solution().mergeTwoLists(l1,l2)
