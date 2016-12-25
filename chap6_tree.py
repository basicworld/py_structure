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
class SubtreeIndexError(ValueError):
    pass

def Tree(data, *subtrees):
    """
    """
    t = [data]
    t.extend(subtrees)
    return t

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError

    return tree[i + 1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i + 1] = subtree
    return tree

def test():
    """
    >>> t1 = Tree('+', 1, 2, 3)
    >>> print t1
    ['+', 1, 2, 3]
    >>> t2 = Tree('*', t1, 6, 8)
    >>> print t2
    ['*', ['+', 1, 2, 3], 6, 8]
    >>> t1 = set_subtree(t1, 2, Tree('+', 3, 5))
    >>> print t1
    ['+', 1, 2, ['+', 3, 5]]
    """
    t1 = Tree('+', 1, 2, 3)
    print t1
    t2 = Tree('*', t1, 6, 8)
    print t2
    set_subtree(t1, 2, Tree('+', 3, 5))
    print t2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""
class TreeNode(object):
    def __init__(self, data, subtrees=[]):
        self._data = data
        self._subtrees = list(subtrees)

    def __str__(self):
        return '[TreeNode {0} {1}]'.format(self._data,
                                           self._subtrees)

"""
