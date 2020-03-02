#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 15:50:03

"""
merge sort:归并排序，会对一个大列表做拆分。拆分完成后，各子列表进行合并排序。最后得到结果
"""

def mergesort(alist):
    """
    对列表使用二分法拆分
    """
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergesort(alist[:mid])
    right = mergesort(alist[mid:])

    return merge(left, right)

def merge(left, right):
    """
    合并并对子列表进行排序
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    alist = [4,3,1,2]
    sort_list = mergesort(alist)
    print (sort_list)

