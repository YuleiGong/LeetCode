#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-11 22:45:45
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution(object):
    def canThreePartsEqualSum(self, A):
        amount = sum(A)
        single = amount / 3
        if single % 1 == 0:
            s = 0
            l = []
            for i in range(len(A)):
                s += A[i]
                if s == single:
                    l.append(s) 
                    s = 0
                    if len(l) == 2 and i != len(A)-1:
                        c = sum(A[i+1:])
                        l.append(c)
                        return l[1] == l[0] == l[2]
        return False
