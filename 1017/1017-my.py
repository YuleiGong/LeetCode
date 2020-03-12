#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-12 19:16:02
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = j = 0
        m, n = len(str1), len(str2)
        while i < m or j < n:
            if str1[i % m] != str2[j % n]: return ""
            i += 1
            j += 1
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        return str1[:gcd(m, n)]


if __name__ == '__main__':
    str1 = "ABABAB"
    str2 = "ABABAB"
    S = Solution()
    ret = S.gcdOfStrings(str1,str2)
    print (ret)
