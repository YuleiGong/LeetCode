#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-17 11:29:15
from __future__ import unicode_literals
from __future__ import absolute_import

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr_a = headA
        curr_b = headB

        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA

        return curr_a


def init_list_node(alist,skip,comm_node):
    head = ListNode(alist[0])
    curr = head

    i = 1
    while i != len(alist):
        if i == skip:
            tmp = comm_node
        else:
            tmp = ListNode(alist[i])

        curr.next = tmp
        curr = curr.next
        i += 1
    return head

def print_node(head):
    while head:
        print ("id:{},val:{}".format(id(head),head.val))
        head = head.next


if __name__ == '__main__':
    listA = [2,6,4]
    skipA = 3

    listB = [1,5]
    skipB = 2

    intersectVal = 0
    comm_node = ListNode(intersectVal)

    headA = init_list_node(listA,skipA,comm_node)
    headB = init_list_node(listB,skipB,comm_node)
    print ("headA")
    print_node(headA)
    print ("headB")
    print_node(headB)
    S = Solution()
    node = S.getIntersectionNode(headA, headB)
    print (node)

