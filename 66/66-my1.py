#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-10 16:32:59

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        self.carry(digits,length)

        return digits

    def carry(self,digits,length):
        if digits[length] == 9:
            digits[length] = 0
            length = length - 1
            self.carry(digits,length)
        else:
            if length == -1:
                digits.insert(0,1)
            else:
                digits[length] = digits[length] + 1

if __name__ == '__main__':
    res = Solution().plusOne([9])
    print (res)
