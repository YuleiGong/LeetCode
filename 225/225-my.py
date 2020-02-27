#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-27 22:11:46
from __future__ import unicode_literals
from __future__ import absolute_import

class MyStack:
    """
    默认队列如果在队尾,出队在队首
    """


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.items.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty is True:
            return None
        else:
            return self.items.pop()



    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty is True:
            return None
        else:
            return self.items[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.items == []


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    print (param_2)
    param_4 = obj.empty()
    print (param_4)
