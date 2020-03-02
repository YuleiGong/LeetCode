#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 16:16:20
from __future__ import unicode_literals
from __future__ import absolute_import

"""
quick sort:快速排序
选取数组最左边的数字作为基准点,选定第二位和最后一位为left 和  right
如果left 大于基准点，将该数放到right的位置
然后移动right下标，如果小于基准点，放到left的位置。直至left right相遇。
约定一轮排序后的子列表如果只有一位元素，则排序完成，否则递归的重复上述过程
"""

def quick(alist):
    quick_helper(alist,0,len(alist)-1)

def quick_helper(alist, first, last):
    if first < last:
        split_point = parition(alist, first, last)
        quick_helper(alist, first, split_point-1)
        quick_helper(alist, split_point+1, last)



def parition(alist, first, last):
    value = alist[first]
    left_mark = first+1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and alist[left_mark] <= value:
            left_mark = left_mark + 1

        while right_mark >= left_mark and alist[right_mark] >= value:
            right_mark = right_mark -1

        if right_mark < left_mark:
            done = True
        else:
            temp = alist[alist]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


if __name__ == '__main__':
    alist = [31,26,20,17,44,54,77,55,93]
    quick(alist)
    print (alist)
