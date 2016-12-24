# -*- coding: utf-8 -*-
"""
使用优先队列来实现哈夫曼算法
"""

from bin_tnode import BinTNode
from prio_queue import PrioQueue
import sys

class HTNode(BinTNode):
    def __lt__(self, othernode):
        """实现node的比较"""
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        """实现队列计数"""
        return len(self._elems)


def huffmanTree(weights):
    trees = HuffmanPrioQ()

    # 构建初始集合
    for w in weights:
        trees.enqueue(HTNode(w))

    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()

def print_BinTNode(t):
    """print二叉树"""
    if t is None:
        sys.stdout.write("^")
        return
    sys.stdout.write('(' + str(t.data))
    print_BinTNode(t.left)
    print_BinTNode(t.right)
    sys.stdout.write(')')

def test():
    t = huffmanTree((1,4,2,4,6,7,4))
    print_BinTNode(t)
    print


if __name__ == '__main__':
    test()
