#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-22 17:13:04
from __future__ import unicode_literals
from __future__ import absolute_import
from functools import reduce

class Queue:
    """
    循环队列
    """
    def __init__(self, max_size):
        self.items = [0] * max_size
        self.count = 0
        self.head_index = 0
        self.max_size = max_size
        self._sum = 0

    def enqueue(self, val):
        if self.count == self.max_size:
            self.dequeue()
        self.items[(self.head_index+self.count) % self.max_size] = val
        self.count += 1
        self._sum += val

    def dequeue(self):
        self.head_index = (self.head_index+1) % self.max_size
        self.count -= 1
        self._sum -= self.items[(self.head_index+self.count) % self.max_size]





class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = Queue(size)


    def next(self, val: int) -> float:
        self.q.enqueue(val)
        return self.q._sum / self.q.count


if __name__ == '__main__':
    m = MovingAverage(3)
    print (m.next(1))
    print (m.next(10))
    print (m.next(3))
    print (m.next(5))


