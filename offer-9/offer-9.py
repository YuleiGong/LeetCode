#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-01 15:44:47
from __future__ import unicode_literals
from __future__ import absolute_import

class CQueue:

    def __init__(self):
        self.stack = []
        self.helper = []


    def appendTail(self, value: int) -> None:
        self.stack.append(value)


    def deleteHead(self) -> int:
        if self.helper:
            return self.helper.pop()
        if not self.stack:
            return -1

        while self.stack:
            self.helper.append(self.stack.pop())

        return self.helper.pop()


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    print (obj.deleteHead())
    print (obj.deleteHead())
    print (obj.deleteHead())

