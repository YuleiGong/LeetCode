#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-03-02 18:14:42

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i):
            if not 0 <= row < rows or not 0 <= col < cols or board[row][col] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            tmp = board[row][col]
            board[row][col] = '/' #已经遍历过,做标记

            i += 1
            res = dfs(row+1,col,i) or dfs(row-1,col,i) or dfs(row,col+1,i) or dfs(row,col-1,i)
            board[row][col] = tmp #恢复
            return res


        for _row in range(rows):
            for _col in range(cols):
                if dfs(_row, _col, 0):
                    return True

        return False




if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABC"
    S = Solution()
    ret = S.exist(board, word)
    print (ret)

