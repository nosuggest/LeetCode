#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 8:45 AM
# @Author  : Slade
# @File    : Lru_Cache.py
from collections import OrderedDict


class lru_catche(object):
    def __init__(self, capcity):
        self.capcity = capcity
        self.save_dict = OrderedDict()

    def get(self, key):
        if key in self.save_dict.keys():
            value = self.save_dict.pop(key)
            self.save_dict[key] = value
            return value
        else:
            return -1

    def push(self, key, value):
        if len(self.save_dict) < self.capcity:
            self.save_dict.update({key: value})
        else:
            if key in self.save_dict.keys():
                self.save_dict.pop(key)
                self.save_dict[key] = value
            else:
                self.save_dict.popitem(last=False)
                self.save_dict[key] = value

    def __len__(self):
        return len(self.save_dict)

    def __repr__(self):
        # return "the length of the cache is %s" % len(self.save_dict)
        return str(len(self.save_dict))

if __name__ == '__main__':
    d = lru_catche(5)

    print(d.get(1))

    d.push(1, 3)
    d.push(2, 6)
    d.push(3, 9)
    d.push(4, 12)
    d.push(5, 15)
    print(len(d))

    print(d.save_dict)
    print(d.get(3))
    print(d.save_dict)

    d.push(6, 18)
    print(d.save_dict)

    print(d)