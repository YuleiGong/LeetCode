#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-16 15:53:07


class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        if not curr:
            return True

        s = Stack()
        [s.push(num) for num in self.traversal(head)]

        for num in self.traversal(head):
            if s.isEmpty():
                return True
            s_val = s.pop()
            if num != s_val:
                return False

        return True


    def traversal(self, head):
        curr = head
        while True:
            val = curr.val
            curr = curr.next
            yield val
            if not curr:
                break
        return None


