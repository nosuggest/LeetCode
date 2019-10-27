#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:29 AM
# @Author  : Slade
# @File    : LeetCode794valid-tic-tac-toe-state.py.py
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        Xcnt = 0
        Ocnt = 0
        for i in range(row):
            Xcnt += list(board[i]).count("X")
            Ocnt += list(board[i]).count("O")

        if Xcnt < Ocnt or Xcnt - Ocnt > 1:
            return False
        ans = []
        for i in range(col):
            ans.append(board[0][i] + board[1][i] + board[2][i])

        ans.append(board[0])
        ans.append(board[1])
        ans.append(board[2])
        ans.append(board[0][0] + board[1][1] + board[2][2])
        ans.append(board[2][0] + board[1][1] + board[0][2])
        print(ans)
        if "OOO" in ans and Xcnt != Ocnt:
            return False
        elif "XXX" in ans and Xcnt != Ocnt + 1:
            return False

        return True