#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-13 10:53:31

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp

        return pre



if __name__ == '__main__':
    head = ListNode(1)
    prev = head

    nums = [2,3,4,5]
    for num in nums:
        node = ListNode(num)
        prev.next = node
        prev = node

    head = Solution().reverseList(head)

    node = head
    while node:
        print (node.val)
        node = node.next

