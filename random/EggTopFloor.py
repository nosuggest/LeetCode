#!/usr/bin/env python
# -*- coding: utf-8 -*-
# interesting question:
# 一幢 200 层的大楼，给你两个鸡蛋。如果在第 n 层扔下鸡蛋，鸡蛋不碎，那么从第 n-1 层扔鸡蛋，都不碎。这两只鸡蛋一模一样，不碎的话可以扔无数次。最高从哪层楼扔下时鸡蛋不会碎？
def f(n,m):
	'''
	n : 楼高
	m : 蛋数
	'''
	if n == 0 :
		return 0
	if m == 1 :
		return n
	result = min(max((f(i-1,m-1),f(n-i,m))) for i in range(1,n+1)) + 1
	return result
if __name__ == '__main__':
#楼高12层，2个蛋
	print(f(12,2))
#Out[2]: 5
#首次放5层，没碎放9层（5+5-1），没碎放12层（5+5-1+5-2）
#首次放5层，碎了从第一层开始