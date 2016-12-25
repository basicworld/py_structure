二叉树放松对分支个数的限制，就是`树的定义`，树中没有左右子树的定义

根据子树是否有排序，分为有序树和无序树

非空树是由树根及其子树树林构成的

相关概念：父结点、子结点、边、兄弟结点、树叶、分支节点、祖先、子孙、路径、高度

0棵树或多棵树的集合称为森林

# 树的性质

1. 任何树都可以映射为一棵二叉树
2. 度为i的树中，第i层至多有k^i个结点


# 树的ADT

```python
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
```

# 树的遍历

## 方法

1. 深度优先。有多种方式：先根序、后根序，递归、非递归
2. 宽度优先

## 宽度优先的思想

1. 将根节点加入队列
2. 弹出队列里的首节点并访问
3. 将该节点的子结点顺序加入队列
4. 重复2 和3步骤，直至队列为空

## 深度优先的思想

主要问题是正确处理回溯，为此要记录所考察及诶单的已经访问的分支或者下一个应该访问的分支

# 树的实现

## 常用的方法

1. 子节点引用表示法，父结点引用表示法
2. 子节点表表示法
3. 长子-兄弟表示法

## 子结点（指针）引用表示法

：：指针表示法。用一个数据表示节点，通过结点间的链接表示树结构

问题是：树的度不确定，不同结点的度可能差异恒大

解决方法是：只支持度不超过m的树。缺点：大量空闲结点

> 在m度结点表示的n个结点的树中，有n*(m-1)+1个空引用域

## 父结点引用表示法

：：每个节点都记录父结点的信息，把所有节点顺序存储在一个list里

优点：存储开销小。顺序遍历就是list输出

缺点：从父结点找子结点的复杂度高-为n。插入和删除数据的管理比较复杂

## 子结点表表示法

：：用一个连续表存储树中各节点的信息，每个节点关联一个子节点表，记录树的结构。表中含有两种单元：

1. 一种表示节点，是节点数据和子结点表头指针的二元组
2. 另一种表示子结点表

优点：从根查找子结点的复杂度低

## 长子-兄弟表示法

：：就是树的二叉树表示，实现`树和二叉树的转换`是核心

# 树的python实现

## 树的python的list实现

这里使用python实现一种简单的树结构，类似于`子节点引用表示法`，但是克服了子节点引用表示法的缺点：浪费空间。因为python有list这个无限扩充的神器

```python

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
    
```

## 树类实现

```python

class TreeNode(object):
    def __init__(self, data, subtrees=[]):
    	"""树节点实现，其他语句参照二叉树的实现"""
        self._data = data
        self._subtrees = list(subtrees)

    def __str__(self):
        return '[TreeNode {0} {1}]'.format(self._data, 
                                           self._subtrees)
```
