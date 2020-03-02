#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 12:13:35
from __future__ import unicode_literals
from __future__ import absolute_import

"""
sort_bubble sort:短冒泡排序
冒泡排序多次遍历列表。
每一轮比较相邻的元素，将大的数字放到后面的位置(交互顺序)。
总计需要遍历len(n) 轮,每遍历一轮,需要冒泡比较的数据量 -1
如果某一轮遍历，发现不需要交换数据的顺序，则证明该数据已经排序完成，可以不用继续排序
"""
def sort_bubble(alist):
    length = len(alist) - 1

    for _ in range(len(alist)):
        exchange = False
        for i in range(length):
            if alist[i] > alist[i+1]:
                exchange = True
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
        if exchange == False:
            return
        length -= 1

if __name__ == '__main__':
    alist = [1,2,3,5,4]
    bubble_sort(alist)
    print (alist)

