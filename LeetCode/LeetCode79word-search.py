#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 8:20 AM
# @Author  : Slade
# @File    : test.py

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        mat = board

        def search_word(word, mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] == word[0]:
                        if backtrack(i, j, 0, word, mat):
                            return True
            return False

        def backtrack(letter_i, letter_l, idx, word, mat):
            if idx == len(word):
                return True
            if letter_i < 0 or letter_i >= len(mat) or letter_l < 0 or letter_l >= len(mat[0]):
                return False
            if mat[letter_i][letter_l] != word[idx]:
                return False
            target = mat[letter_i][letter_l]
            mat[letter_i][letter_l] = 0
            ans = backtrack(letter_i + 1, letter_l, idx + 1, word, mat) or backtrack(letter_i - 1, letter_l, idx + 1,
                                                                                     word,
                                                                                     mat) or backtrack(letter_i,
                                                                                                       letter_l + 1,
                                                                                                       idx + 1, word,
                                                                                                       mat) or backtrack(
                    letter_i, letter_l - 1, idx + 1, word, mat)
            mat[letter_i][letter_l] = target
            return ans

        return search_word(word, mat)

