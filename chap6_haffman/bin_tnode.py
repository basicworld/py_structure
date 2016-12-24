# -*- coding: utf-8 -*-
"""
二叉树节点类
"""
import sys

class BinTNode(object):
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

def count_BinTNode(t):
    """统计二叉树的节点
    @t 一颗二叉树"""
    if t is None:
        return 0
    else:
        return 1 + count_BinTNode(t.left) + count_BinTNode(t.right)

def preorder(t, proc):
    """前序遍历二叉树，递归"""
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


def print_BinTNode(t):
    """print二叉树"""
    if t is None:
        sys.stdout.write("^")
        return
    sys.stdout.write('(' + str(t.data))
    print_BinTNode(t.left)
    print_BinTNode(t.right)
    sys.stdout.write(')')

def levelorder(t, proc):
    """宽度优先的遍历"""
    from Queue import Queue
    q = Queue()
    q.put(t)
    while not q.empty():
        t = q.get()
        if t is None:
            continue
        q.put(t.left)
        q.put(t.right)
        proc(t)
    pass

def preorder_nonrec(t, proc):
    """非递归的先根序遍历
    时间复杂度为n
    空间复杂度最坏为n，平均是logn
    """
    stack = []
    while t is not None or stack:
        while t is not None:
            proc(t.data)  # 遇到根则直接处理
            stack.append(t.right)  # 遇到右子树则先存起来
            t = t.left  # 找到左子树，继续
        t = stack.pop()  # 左子树遍历完，回溯

def preorder_elements(t):
    """通过生成器遍历二叉树，先根序遍历"""
    stack = []
    while t is not None or stack:
        while t is not None:
            yield t.data
            stack.append(t.right)
            t = t.left
        t = stack.pop()

def postorder_non_rec(t, proc):
    """非递归的后根序遍历"""
    stack = []
    while t is not None or stack:
        while t is not None:
            stack.append(t)
            t = t.left if t.left is not None else t.right
        t = stack.pop()
        proc(t.data)
        if stack and stack[-1].left == t:
            t = stack[-1].right
        else:
            t = None

def postorder_wlfei(t, proc):
    """后根序遍历
    wlfei自定义"""
    if t:
        if t.left:
            postorder_wlfei(t.left, proc)
        if t.right:
            postorder_wlfei(t.right, proc)
        proc(t.data)

def sum_BinTNode(t):
    """
    二叉树节点求和
    """
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)

def test():
    t = BinTNode(1,
                 BinTNode(2, BinTNode(5), BinTNode(3)),
                 BinTNode(4, BinTNode(6), BinTNode(7)))
    print count_BinTNode(t)
    print sum_BinTNode(t)
    print_BinTNode(t)
    print
    levelorder(t, lambda x: sys.stdout.write(str(x.data)))
    print
    preorder_nonrec(t, lambda x: sys.stdout.write(str(x)))
    print
    for i in preorder_elements(t):
        sys.stdout.write(str(i))
    print
    postorder_non_rec(t, lambda x: sys.stdout.write(str(x)))
    print
    postorder_wlfei(t, lambda x: sys.stdout.write(str(x)))
    print


if __name__ == '__main__':
    test()
