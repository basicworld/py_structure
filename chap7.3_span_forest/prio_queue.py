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

