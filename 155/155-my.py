#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-26 15:19:19

class MinStack:

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, x):
        """
        使用辅助栈可以保证每次pop都能到辅助栈中得到最小值
        """

        self.data.append(x)
        if len(self.helper) == 0:
            self.helper.append(x) #栈顶存最小数
        elif x <= self.helper[-1]:
            self.helper.append(x) #栈顶存最小数
        else:
            self.helper.append(self.helper[-1])#继续加入一位

    def pop(self):
        if self.data:
            self.helper.pop()
            self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(2)
    stack.push(0)
    stack.push(3)
    stack.push(0)

    print (stack.getMin())
    stack.pop()
    print (stack.getMin())
    stack.pop()
    print (stack.getMin())
    stack.pop()
    print (stack.getMin())

