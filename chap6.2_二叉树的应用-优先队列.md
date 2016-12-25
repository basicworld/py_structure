优先队列是：附带优先级顺序的队列，弹出的元素总是目前队列里优先级最高的那个

优先队列的实现：

1. 连续表，顺序就表示优先程度；或者无组织存入，取出时检索优先级最高的.但是无论是线性表还是链接表，总存在复杂度为n的操作，效率太低
2. 使用堆（结点里存储数据的完全二叉树）

## 堆

采用树形结构实现优先队列的一种有效技术称为堆

堆就是结点里存储数据的完全二叉树，存储的数据满足特殊的堆序：人一个节点里所存的数据先于或等于其子结点里的数据

特点：

1. 从根到任意一个叶节点的路径上，存储的数据按规定的优先关系排序
2. 最优元素一定时根节点（堆顶）
3. 一颗完全二叉树可以自然而且信息完全的存入一个连续的线性结构
4. 在堆的最后加上一个元素，仍然是完全二叉树，但不一定是堆
5. 堆去掉堆顶，就形成了两个子堆
6. 去掉最后一个元素，仍然是堆

所要求的序是小元素有限，构造出来的堆就称为`小顶堆`，即小元素在上

## 堆做优先队列

1. pop的复杂度为1
2. 插入操作需要保证仍然是一个堆
3. 弹出元素后，仍然需要保持堆结构
4. 2和3的复杂度为logn

堆插入和删除袁术的关键操作称为删选：向上筛选和向下筛选

### 插入元素和向上筛选

1. 插入元素形成完全二叉树
2. 用新元素与父结点对比，优先则交换位置

### 弹出元素和向下筛选

1. 弹出堆顶
2. 把最后的元素e作为堆顶
3. e分别与子堆的堆顶比较，最小的作为堆顶
4. 继续做3直到结束

### 使用list构造堆

最坏的复杂度可能出现在：初始构建堆的时候、list满时python自动构建list的时候，这两个复杂度都是n

其他复杂度最大为logn

```
# -*- coding: utf-8 -*-
"""
使用堆来构造优先队列
"""

class PrioQueueError(ValueError):
    pass

class PrioQueue(object):
    def __init__(self, elist=[]):
        """
        使用list作为堆的存储结构，首端弹出元素，尾端加入元素
        """
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek()')

        return self._elems[0]

    def enqueue(self, e):
        """入队操作"""
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        """
        向上筛选
        e并没有存入elems，而是拿着它找位置插入，稍微提高一点速度
        """
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        """向下筛选"""
        elems, i, j = self._elems, begin, begin*2 + 1
        while j < end:
            # 比较子堆堆顶的大小
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            # 比较e与最小堆顶的大小
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j + 1
        elems[i] = e

    def buildheap(self):
        """构建初始堆，复杂度为n
        思想是：从end//2往后的元素没有子结点，已经是最小的堆
        从end//2往堆顶的元素，需要与子节点一起构造新的堆，采用向下筛选的方式
        """
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)


def test():
    d = PrioQueue([2,3,8,3,4])
    for i in range(10, 5, -1):
        d.enqueue(i)
    print d.peek()
    while not d.is_empty():
        print d.dequeue()

if __name__ == '__main__':
    test()
```

## 堆做排序

小顶堆不断取出元素，就构成了从小到大的排序，这就是`堆排序`的大致思想

堆排序的复杂度为nlogn
