# -*- coding: utf-8 -*-
"""
定义二叉树类
"""

class BinTNode(object):
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


class BinTree(object):
    """docstring for BinTree"""
    def __init__(self):
        super(BinTree, self).__init__()
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def lchild(self):
        return self._root.left

    def rchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_lchild(self, leftchild):
        self._root.left = leftchild

    def set_rchild(self, rightchild):
        self._root.right = rightchild

    def preorder_elements(self):
        t, s = self._root, []
        while t is not None or s:
            while t is not None:
                s.append(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == '__main__':
    pass
