#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-04 17:16:23

class Solution:
    def reverse(self, x: int) -> int:
        _x = str(abs(x))[::-1]
        if x<0:
            _x = int(_x)*-1
        else:
            _x = int(_x)

        if _x >= pow(-2,31) and _x <= (pow(2,31) - 1):
            return _x
        else:
            return 0


if __name__ == '__main__':
    print (Solution().reverse(153))


