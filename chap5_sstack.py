# -*- coding: utf-8 -*-
"""
栈数据结构的实现

ADT Stack:
    Stack(self)
    is_empty(self)  #
    push(self, elem)  #
    pop(self)  #
    top(self)  # 取得栈里最后压入的元素，不删除
"""


class StackUnderFlow(ValueError):
    pass


class SStack(object):
    def __init__(self):
        """
        使用顺序表实现栈结构
        """
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        """取得栈顶元素"""
        if self.is_empty():
            raise StackUnderFlow('in SStack.top()')

        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow('in SStack.pop()')

        return self._elems.pop()


def test():
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print st1.pop()


if __name__ == '__main__':
    test()
