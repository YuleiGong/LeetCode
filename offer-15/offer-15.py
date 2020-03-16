#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-16 15:56:20
class Solution:
    def hammingWeight(self, n: int) -> int:
        val = n
        count = 0
        while val > 0:
            bit = val % 2 #最后一位
            val = val // 2
            if bit == 1:
                count += 1

        return count


if __name__ == '__main__':
    S = Solution()
    ret = S.hammingWeight(9)
    print (ret)

