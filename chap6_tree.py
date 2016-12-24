# -*- coding: utf-8 -*-
"""
ADT Tree:
    Tree(self, data, forest)  # 基于树根和一组子树构造一棵树
    is_empty(self)  # 是否为空树
    num_nodes(self)  # 数中节点数
    data(self)  # 获取树根的数据
    first_child(self, node)  # 获取node结点的第一个子树
    children(self, node)  # 获取node结点的所有子树， 迭代器
    set_first(self, tree)  # 用tree取代第一棵子树
    insert_child(self, i, tree)  # 将tree设置为第i棵子树，其他树后移
    traversal(self)  # 遍历各节点的迭代器
    forall(self, op)  # 广播操作op

"""
