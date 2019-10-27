#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 9:07 AM
# @Author  : Slade
# @File    : LeetCode146lru-cache.py
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.length = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            tmp = self.cache.pop(key)
            self.cache[key] = tmp
            return tmp
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if len(self.cache) < self.length:
            if key not in self.cache:
                self.cache[key] = value
            else:
                _ = self.cache.pop(key)
                self.cache[key] = value
        else:
            if key not in self.cache:
                _ = self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                _ = self.cache.pop(key)
                self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
