#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-14 10:55:01
class Foo:
    def __init__(self):
        self.t = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.t = 1



    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.t != 1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.t = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.t != 2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

if __name__ == '__main__':
    f = Foo()

