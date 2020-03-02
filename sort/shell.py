#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 15:04:13
from __future__ import unicode_literals
from __future__ import absolute_import

"""
shell_sort:希尔排序
希尔排序首先将列表分成几个子列表，进行插入排序，最后合并进行插入排序
"""
def shell(alist):
    """
    每次除2作为步长
    最后一次排序,使用的step为1，进行一次完整的插入排序
    """
    sub_count = len(alist) // 2

    while sub_count > 0:
        for start in range(sub_count):
            insert_sort(alist, start, sub_count)
        sub_count = sub_count // 2

def insert_sort(alist, start, step):
    """
    对子列表插入排序
    Args:
        step:步长
        alist:列表
        start:起始位置
    """
    for i in range(start+step, len(alist), step):
        curr = alist[i]
        pos = i

        while pos >= step and alist[pos-step] > curr:
            alist[pos] = alist[pos-step]
            pos = pos - step

        alist[pos] = curr


if __name__ == '__main__':
    pass

