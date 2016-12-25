哈弗曼树是重要的二叉树应用，在信息领域有重要的理论和实际价值，例如：通过哈夫曼构建最优编码

哈弗曼树是带权扩充二叉树中，带权外部路径长度最短的

定义：设有实数集W，T是一颗扩充二叉树，其m个外部结点分别以wi为权值，而且T的带权外部路径长度WPL在所有的扩充二叉树中达到最小，则称T为数据集W的最优二叉树或者`哈弗曼树`

下面介绍哈夫曼算法的python实现

# 哈弗曼树与哈夫曼算法



通过哈夫曼算法，可以将任意实数集合构造出对应的哈弗曼树

哈夫曼算法思想：总是从树的集合中拿出两个权最小的二叉树构成新的树，然后放进树的集合

> 1. 初始化： 根据给定的n个权值{w1,w2,…wn}构成n棵二叉树的集合F={T1,T2,..,Tn}，其中每棵二叉树Ti中只有一个带权wi的根结点，左右子树均空。
> 
> 2. 找最小树：在F中选择两棵根结点权值最小的树作为左右子树构造一棵新的二叉树，且至新的二叉树的根结点的权值为其左右子树上根结点的权值之和。

> 3. 删除与加入：在F中删除这两棵树，并将新的二叉树加入F中。

> 4. 判断：重复前两步（2和3），直到F中只含有一棵树为止。该树即为哈夫曼树

# 哈夫曼算法的实现

适合用优先队列来实现（优先队列是用完全二叉树来实现的，重点是向上筛选和向下筛选）

思想：

1. 建立一组单节点的二叉树，放进优先队列
2. 从优先队列取出两个权值最小的树，构成新的二叉树，放进优先队列
3. 重复第2步直到优先队列只剩下一个树

构造哈弗曼树的复杂度为nlogn

```python
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

```

# 哈夫曼树的应用

## 哈夫曼编码

：解决二进制编码的设计问题，使新到传输的数据量最小化

编码方法：构造出哈夫曼树后，定义根节点的左边路径编码为0，右边路径编码为1，则得到所有字符的编码
