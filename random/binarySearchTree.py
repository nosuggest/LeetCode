#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 8:51 PM
# @Author  : Slade
# @File    : binarySearchTree.py

class Node:
    def __init__(self, element):
        self.element = element
        self.lchild = None
        self.rchild = None


# 左树上所有结点的值均小于或者等于它的根结点的值
# 右树上所有结点的值均大于或者等于它的根结点的值
# 左右树也分别为二叉树
class binaryTree:
    def __init__(self, l):
        self.root = Node(l[0])
        for data in l[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        # 找不到
        if node is None:
            return False, node, parent
        # 找到了
        if data == node.element:
            return True, node, parent

        if node.element > data:
            # 查找比当前node更小的左子树
            return self.search(node.lchild, node, data)
        else:
            # 查找比当前node更大的右子树
            return self.search(node.rchild, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        # 找不到data的情况下
        if not flag:
            if p.element > data:
                # 如果要插入的data比当前结点的值要小则插入左子树
                p.lchild = Node(data)
            else:
                p.rchild = Node(data)

    def getMin(self, node):
        if node.lchild is None:
            return node.element
        else:
            return self.getMin(node.lchild)

    def getMax(self, node):
        if node.rchild is None:
            return node.element
        else:
            return self.getMax(node.rchild)

    def delete(self, root, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            raise ValueError()

        # 1、找到当前结点哪个子树非空，所有的值都在非空的这个子树上
        # 2、判断当前结点是父结点哪个子树
        # 3、父结点对应的子树用当前结点的非空子树覆盖
        if n.lchild is None:
            # 当前结点的左子树为空
            if n == p.lchild:
                # 当前结点为左子树
                p.lchild = n.rchild

            else:
                # 当前结点为右子树
                p.rchild = n.rchild

        elif n.rchild is None:
            # 当前结点的右子树为空
            if n == p.lchild:
                # 当前结点为左子树
                p.lchild = n.lchild
            else:
                p.rchild = n.lchild

        else:
            # 当前结点的左右子树均不为空
            pre = n.rchild  # 右树

            # 当前结点的右树对应的左树为空的时候，没有比当前node的值更小的element了，直接拿右树覆盖
            if pre.lchild is None:
                n.element = pre.data
                n.rchild = pre.rchild
            else:
                next = pre.lchild
                while next.lchild is not None:
                    pre = next
                    next = next.lchild
                n.element = next.element
                pre.lchild = next.rchild

    def preOrderTraverse(self, node):
        '''
        1、访问根结点
        2、先序遍历左子树
        3、先序遍历右子树
        '''
        ans = []
        if node is not None:
            print(node.element, end="\t")
            ans += [node.element]
            ans += self.preOrderTraverse(node.lchild)
            ans += self.preOrderTraverse(node.rchild)
        return ans

    def inOrderTraverse(self, node):
        '''
        1、中序遍历左子树
        2、访问根结点
        3、中序遍历右子树
        '''
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.element, end="\t")
            self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):
        '''
        1、后序遍历左子树
        2、后序遍历右子树
        3、访问根结点
        '''
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.element, end="\t")

            def levelOrderTraverse(self, node):
                if node is not None:
                    queue = []
                    queue.append(node)
                    while queue:
                        # 利用队列，先进先出
                        cur = queue.pop(0)
                        print(cur.element, end="\t")
                        if cur.lchild:
                            queue.append(cur.lchild)
                        if cur.rchild:
                            queue.append(cur.rchild)


if __name__ == '__main__':
    t = binaryTree([17, 5, 35, 2, 11, 29, 38, 9, 16, 7, 8])
    # print(t.getMin(t.root))
    # print(t.getMax(t.root))
    # t.insert(18)
    # print(t.root.rchild.lchild.lchild.element)

    # t.delete(t.root, 5)
    # print(t.root.lchild.rchild.lchild.lchild.element)

    print (t.preOrderTraverse(t.root))
    print("")
    # t.inOrderTraverse(t.root)
    # print("")
    # t.postOrderTraverse(t.root)
    # print("")
    # t.levelOrderTraverse(t.root)
