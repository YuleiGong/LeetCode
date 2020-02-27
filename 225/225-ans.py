#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-27 22:11:46
from __future__ import unicode_literals
from __future__ import absolute_import


from queue import Queue

class MyStack:
    """
    用队列实现栈
    """


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        [self.q.put(self.q.get()) for _ in range(self.q.qsize() - 1)]


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()



    def top(self) -> int:
        """
        Get the top element.
        """
        top = self.q.get()
        self.push(top)

        return top


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.qsize() == 0


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    print (obj.empty())
