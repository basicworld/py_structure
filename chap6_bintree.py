# -*- coding: utf-8 -*-
"""
二叉树数据结构的实现

ADT BinTree:
    BinTree(self, data, left, right)  # 二叉树抽象数据类型
    is_empty(self)  # 是否为空树
    num_nodes(self)  # 节点个数
    data(self)  # 获取树根存储的数据
    left(self)  # 获取左子树
    right(self)  # 获取右子树
    set_left(self,btree)  #  用btree取代原来的左子树
    set_right(self,btree)  # 用btree取代原来的右子树
    traveral(self)  # 遍历各节点的迭代器
    forall(self,op)  # 广播操作
"""

def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty_BinTree(btree):
    return btree is None

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data

def set_left(btree, data):
    btree[1] = data

def set_right(btree, data):
    btree[2] = data


def test():
    b = BinTree(2, BinTree(4), BinTree(8))
    print b
    set_left(b, BinTree(5))
    print b


if __name__ == '__main__':
    test()

