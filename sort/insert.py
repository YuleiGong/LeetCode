#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 14:12:14
from __future__ import unicode_literals
from __future__ import absolute_import

"""
inset sort:插入排序
插入排序在列表的底端维护一个有序的子列表，逐渐移动列表，逐个将每个新元素插入这个子列表
在列表起始位置是元素的子列表。从元素 1 到元素 n–1，每一轮都将当前元素与有序子列表中的元素进行比较。
在有序子列表中，将比它大的元素右移;当遇到一个 比它小的元素或抵达子列表终点时，就可以插入当前元素。
"""

def insert(alist):
    for index in range(1,len(alist)):
        curr = alist[index]
        pos = index

        #在子列表中进行排序,子列表中大于curr的右移一位，小于在当前插入
        while pos > 0 and alist[pos-1] > curr:
            alist[pos] = alist[pos-1]
            pos -= 1

        alist[pos] = curr


if __name__ == '__main__':
    alist = [6,5,4,3,2,1]
    insert(alist)
    print (alist)

