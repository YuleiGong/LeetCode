#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-05 11:37:04

from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people

        i = 1
        index = 0
        while i <= candies:
            res[index] = res[index] + i
            candies = candies - i
            i += 1

            index += 1
            if index == num_people:
                index = 0
        res[index] = res[index] + candies

        return res


if __name__ == '__main__':
    candies = 10
    num_people = 3
    S = Solution()
    ret = S.distributeCandies(candies, num_people)
    print (ret)
