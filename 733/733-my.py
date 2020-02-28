#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-28 14:23:29
from __future__ import unicode_literals
from __future__ import absolute_import

from typing import List
from queue import Queue 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        org_color = image[sr][sc]
        queue = Queue()
        queue.put((sr,sc))
        points = [(-1,0), (1,0), (0,1),(0,-1)]


        while not queue.empty():
            _sr,_sc = queue.get()
            if image[_sr][_sc] != newColor:
                image[_sr][_sc] = newColor
            for p  in points:
                tmp_sr = _sr+p[0]
                tmp_sc = _sc+p[1]
                if 0 <= tmp_sr < len(image) and 0 <= tmp_sc < len(image[0]) and image[tmp_sr][tmp_sc] == org_color:
                    queue.put((tmp_sr,tmp_sc))

        return image



if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    S = Solution()
    ret = S.floodFill(image,sr,sc,newColor)
    print (ret)
