#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 10:11 PM
# @Author  : Slade
# @File    : LeetCode208implement-trie-prefix-tree.py
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        node["is_word"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.keys():
                node = node[c]
            else:
                return False
        return node.get("is_word", False)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.keys():
                node = node[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    word = "apple"
    prefix = "app1"
    obj.insert(word)
    param_2 = obj.search(word+"1")
    print (param_2)
    param_3 = obj.startsWith(prefix)
    print (param_3)
