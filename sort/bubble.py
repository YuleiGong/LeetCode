#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 11:45:53
from __future__ import unicode_literals
from __future__ import absolute_import

"""
bubble sort:冒泡排序
冒泡排序多次遍历列表。
每一轮比较相邻的元素，将大的数字放到后面的位置(交互顺序)。
总计需要遍历len(n) 轮,每遍历一轮,需要冒泡比较的数据量 -1
"""
def bubble_sort(alist):
    length = len(alist) - 1

    for _ in range(len(alist)):
        for i in range(length):
            if alist[i] > alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
        length -= 1

if __name__ == '__main__':
    alist = [6,5,4,3,2,1]
    bubble_sort(alist)
    print (alist)
