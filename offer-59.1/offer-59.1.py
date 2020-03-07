#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-07 12:09:29

from collection import deque

class MaxQueue:

    def __init__(self):
        self.items = deque()
        self.max_items = deque()


    def max_value(self) -> int:
        return self.max_items[0] if self.max_items else -1


    def push_back(self, value: int) -> None:

        while self.max_items and self.max_items[-1] < value:
            self.max_items.pop()
        self.items.append(value)
        self.max_items.append(value)



    def pop_front(self) -> int:
        if not self.items:
            return -1
        num = self.items.popleft()
        if num == self.max_items[0]:
            self.max_items.popleft()
        return num

