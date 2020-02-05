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
        int_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        prev = 0
        value = 0
        for i in reversed(s):
            current = int_map.get(i)
            if current < prev:
                value += (-1*current)
            else:
                value += current
            prev = current


        if value >= 1 and value <= 3999:
            return value
        else:
            return None

if __name__ == '__main__':
    value = Solution().romanToInt("MCDLXXVI")
    print (value)

