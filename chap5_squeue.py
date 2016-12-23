# -*- coding: utf-8 -*-
"""
使用python的list实现队列功能
自己管理list的存储
自动扩容
"""


class QueueUnderflow(ValueError):
    pass


class SQueue(object):
    """
    对满就是self._num = self._len
    下一个空位的下标是：(self._head + self._num) % self._len
    """
    def __init__(self, init_len=8):

        self._len = init_len
        self._elems = [0] * self._len
        self._head = 0  # 队首下标
        self._num = 0  # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len  # 设置新队列
        for i in range(old_len):  # 复制旧元素到新队列
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

if __name__ == '__main__':
    q = SQueue()
    for i in range(10):
        q.enqueue(i)
    while not q.is_empty():
        print q.dequeue()
