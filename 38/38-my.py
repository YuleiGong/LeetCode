#!/usr/bin/env python # -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-09 14:41:39


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        求外观数列
        Args:
            n:外观数列的第N项
        Returns:
            外观数列的第N项
        """

        if n<1 or n > 30:
            return None

        if n == 1:
            return "1"

        prev = "1"
        for i in range(2,n+1):
            curr = ""
            for k in self.parse(prev):
                curr += k["count"]
                curr += k["val"]
            prev = curr
            if i == n:
                return curr


    def parse(self, value):
        count = None
        prev = None

        for index,val in enumerate(value):
            if val == prev:
                count += 1
            else:
                if index != 0:
                    yield {'count':str(count),'val':prev}
                count = 1
            if index == len(value) - 1:
                yield {'count':str(count),'val':val}
            prev = val


if __name__ == '__main__':
    res = Solution().countAndSay(4)
    print (res)
