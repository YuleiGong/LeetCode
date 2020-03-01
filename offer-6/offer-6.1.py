#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 12:08:28


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        return self.reversePrint(head.next) + [head.val] if head else []



if __name__ == '__main__':
    head = [1,3,2]
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)

    S = Solution()
    alist = S.reversePrint(head)
    print (alist)

