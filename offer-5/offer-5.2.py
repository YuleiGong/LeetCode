#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 20:23:59

class Solution:
    def replaceSpace(self, s: str) -> str:
        astr = ""
        for _s in s:
            if _s == " ":
                astr += "%20"
            else:
                astr += _s
        return astr



if __name__ == '__main__':
    astr = "We are happy."
    S = Solution()
    ret = S.replaceSpace(astr)
    print (ret)


