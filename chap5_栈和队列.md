# 概述栈和队列

最常用的两种容器：栈  队列

栈和队列是最简单的缓存结构，只支持数据项的存储和访问，不支持数据项之间的任何关系

栈：后进先出

队列：先进先出

顺序表是栈和队列的最简单实现方式

# 栈的实现

使用线性表

对于顺序表，后端插入和删除的操作复杂度都是1

对于连接表，前端插入和删除的操作复杂度都是1

```
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


```

```
class LStack(object):
    def __init__(self):
        """
        使用链接表实现栈结构
        """
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        """取得栈顶元素"""
        if self.is_empty():
            raise StackUnderFlow('in LStack.top()')

        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow('in LStack.pop()')

        p = self._top
        self._top = p.next
        return p.elem

```

栈的应用：

1. 颠倒顺序
2. 括号匹配
3. 表达式计算和表示

# 表达式的表示、计算和变换

概念：中缀表达式、前缀表达式、后缀表达式

后缀表达式非常适合计算机的处理，中缀表达式是表达起来最复杂的

使用栈来计算后缀表达式

中缀表达式到后缀表达式的转换：

1. 重要的是优先级的处理问题
2. 参看书上P147

# 栈与递归/函数调用

编程语言的递归函数就是使用`运行栈`来实现的，对递归函数的每次调用在栈上为之开辟一块区域，称为`函数帧`（可理解为普通栈里的一个元素，这里函数帧是一个特殊定义的对象）

函数调用的前序动作：

1. 为被调用函数的局部变量和形参分配存储区
2. 将所有实参和函数的返回地址存入函数帧
3. 将控制转到被调用函数入口

函数调用的后续动作：

1. 将被调用函数的计算结果存入指定位置
2. 释放被调用函数的存储区（帧）
3. 按以前保存的返回地址将控制转回调用函数

任何一个递归函数，都可以通过引入一个栈保存中间结果的方式，翻译为一个非递归过程

目前的计算机中，函数调用的时间损失多半是可以接受的


