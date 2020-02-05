#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-05 16:05:40

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        base = strs.pop(0)

        prev = ""
        for i in range(len(base)):
            current = base[0:i+1]
            for word in strs:
                if current != word[:len(current)]:
                    return prev

            prev = current

        return prev

if __name__ == '__main__':
    a = Solution().longestCommonPrefix(["a"])
    print (a)
