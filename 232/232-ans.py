#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-27 20:58:21
from __future__ import unicode_literals
from __future__ import absolute_import

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outstack == []:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outstack == []:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.instack == [] and self.outstack == []

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(3)
    obj.push(2)
    param_3 = obj.peek()
    print (param_3)
