#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-28 12:11:04
from __future__ import unicode_literals
from __future__ import absolute_import

class Solution:
        def decodeString(self, s: str) -> str:
            stack = []
            res = ""
            multi = 0

            for c in s:
                if c == '[':
                    stack.append([multi, res])
                    res = ""
                    multi = 0
                elif c == ']':
                    cur_multi, last_res = stack.pop()
                    res = last_res + cur_multi * res
                elif '0' <= c <= '9':
                    multi = multi*10+int(c)
                else:
                    res += c
            return res


if __name__ == '__main__':
    astr = "20[a]"
    S = Solution()
    astr = S.decodeString(astr)
    print (astr)
