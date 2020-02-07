#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-07 14:00:01


class Solution:
    def isValid(self, s: str) -> bool:
        """
        判断字符串是否有效
        Args:
            s:字符串
        """
        symbols = s.replace(" ", "")
        balance = True
        compare = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        s = Stack()
        for symbol in symbols:
            if symbol in ('({['):
                s.push(symbol)
            else:
                if s.isEmpty is True:
                    return False
                _symbol = s.pop()  # (({[)
                if symbol != compare.get(_symbol):
                    balance = False
                    break

        if s.isEmpty is False:
            balance = False

        return balance


class Stack:
    """
    简单的栈
    Attributes:
        items: 使用列表存放数据
    """

    def __init__(self):
        self.items = []

    @property
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    valid = Solution().isValid('{()[]}')
    print(valid)
