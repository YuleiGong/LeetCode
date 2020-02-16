#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-16 11:03:41
from __future__ import unicode_literals
from __future__ import absolute_import


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        fast:最后一个(奇数) None(偶数)
        slow:中间数(奇数) 中间往后
        """
        slow,fast = head,head
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next

        #反转
        curr = slow
        pre = None
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp


        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True


if __name__ == '__main__':
    alist = [1,2,3,2,1]
    head = ListNode(1)

    curr = head
    for num in alist[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    S = Solution()
    ret = S.isPalindrome(head)
    print (ret)
