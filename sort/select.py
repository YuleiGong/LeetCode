#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 12:20:47
from __future__ import unicode_literals
from __future__ import absolute_import

"""
select sort:选择排序
选择排序:在每次遍历的时候寻找最大值，并在遍历完成后将最大值放到当前轮次的最后一位。
并将最后一位移动到最大值的位置
"""

def select_sort(alist):
    length = len(alist) 

    max_index = 0 #假设索引为0是最大数

    for _ in range(len(alist)):
        for i in range(length):
            if alist[i] > alist[max_index]:
                max_index = i
        length -= 1

        tmp = alist[max_index]
        alist[max_index] = alist[length]
        alist[length] = tmp #最后一位
        max_index = 0



if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    select_sort(alist)
    print (alist)
