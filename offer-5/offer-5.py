#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-29 20:23:59

class Solution:
    def replaceSpace(self, s: str) -> str:
        astr = list(s)
        for i in range(len(s)):
            if astr[i] == " ":
                astr[i] = "%20"
        return "".join(astr)



if __name__ == '__main__':
    astr = "We are happy."
    S = Solution()
    ret = S.replaceSpace(astr)
    print (ret)


