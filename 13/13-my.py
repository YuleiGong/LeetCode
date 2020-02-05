#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-05 13:45:48

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        罗马数字转整数
        Args:
            s:罗马数字
        Returns:
            return int value if value >= 1 and value <= 3999
        """
        spec = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        int_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        splits = []
        for pat in spec.keys():
            if pat in s:
                s=s.replace(pat,'')
                splits.append(pat)
        splits.extend(list(s))

        value = 0
        for p in splits:
            part = spec.get(p)
            if not part:
                part = sum([int_map.get(i) for i in p])
            value += part

        if value >= 1 and value <= 3999:
            return value
        else:
            return None

if __name__ == '__main__':
    value = Solution().romanToInt("MCDLXXVI")
    print (value)

