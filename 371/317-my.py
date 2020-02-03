#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-03 19:06:40

import ctypes

class Solution(object):
    def getSum(self, a: int, b: int) -> int:
        """
        强制使用int32位 避免溢出
        """
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value

        while b != 0:
           result = ctypes.c_int32(a ^ b).value #异或
           carry = ctypes.c_int32((a & b) << 1).value #求与并左移
           a,b = result,carry

        return a


if __name__ == '__main__':
    print (Solution().getSum(-1, -5))



