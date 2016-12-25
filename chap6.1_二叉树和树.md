复杂的数据结构是一些基本元素的汇集，元素之间不是简单的线性关系，可能存在更复杂的联系，这种结构如树、图

这里介绍最简单的树形结构

树形结构的特征：

1. 有且只有一个根节点
2. 根节点之外的结点有且只有一个前驱，有0个或多个后继
3. 没有循环
4. 任意两个结点通过后继关系可达到的集合，或者互不相交，或者一个是另一个的子集
5. 二叉树是最简单、应用最广的树形结构

# 二叉树

二叉树：在树形结构的特征上，再加上一条：每个结点最多有两个后继

基本概念：左子树、右子树、空树、单点树、父结点、子结点、、兄弟结点、树叶、高度、满二叉树、扩充二叉树、外部结点、完全二叉树

扩充二叉树：对于一棵二叉树，加入足够的结点，使得元二叉树的每个节点的都是度为2的结点，这时的状态称为扩充二叉树

性质：

1. 非空二叉树的第i层至多有2Expi个结点
2. 高度为h的树至多有2Exp (h+1) - 1个结点
3. 任何非空二叉树，叶子节点个数n0，度为2的结点n2，则n0=n2+1
4. 满二叉树的叶节点比分支节点多一个
5. n个结点的完全二叉树的高度为h=向下取整(logn)
6. 对于有n个结点的完全二叉树，按完全二叉树的编号，根节点编号而0，编号i结点的父结点为(i-1)/2，最长路径长度为logn

## 简单实现

```
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


```

## 遍历二叉树

深度优先：

1. 先根序遍历
2. 中根序遍历（对称序）
3. 后根序遍历

宽度优先：即逐层访问，用队列做缓存

递归的遍历，复杂度为n

非递归的遍历，为n或logn

## 二叉树应用：表达式树

后缀、前缀表达式很适合用二叉树格式存储

```
# -*- coding: utf-8 -*-
"""
使用二叉树来存储和计算表达式:二元表达式为例
也可以扩充成一元和多元表达式
如make_sum(*args):
    return ('+',) + args
对应的就是普通的树结构
"""
def make_sum(a, b):
    return ('+', a, b)

def make_prod(a, b):
    return ('*', a, b)

def make_diff(a, b):
    return ('-', a, b)

def make_div(a, b):
    return ('/', a, b)

def is_basic_exp(a):
    """
    判断是否是基本表达式
    """
    return not isinstance(a, tuple)

def is_number(x):
    return isinstance(x, (int, float, complex))

def eval_exp(e):
    """计算表达式"""
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op not in '+-*/':
        raise TypeError

    if op == '+':
        return eval_sum(a, b)
    if op == '-':
        return eval_diff(a, b)
    if op == '*':
        return eval_prod(a, b)
    if op == '/':
        return eval_div(a, b)

def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    return make_sum(a, b)

def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / float(b)
    return make_div(a, b)

def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    return make_prod(a, b)

def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    return make_diff(a, b)

def test():
    e1 = make_prod(make_div(50, 4), make_sum(2, make_diff(4, 90)))
    print e1
    print eval_exp(e1)

if __name__ == '__main__':
    test()

```



