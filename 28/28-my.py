#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-08 15:05:43

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(haystack)
        step = len(needle)

        if haystack == "" and needle == "":
            return 0
        elif needle == "" and haystack != "":
            return 0
        elif haystack == "" and needle != "":
            return -1
        else:
            pass

        for i in range(length):
            stop = i+step
            if stop > length:
                break
            if haystack[i:stop] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "a"
    index = Solution().strStr(haystack,needle)
    print (index)


