# -*- coding: utf-8 -*-
"""
阶乘
"""


def nonrec_fact(n):
    """
    阶乘
    自己管理栈，模拟函数调用的过程
    使用一个局部栈保存计算的中间信息

    >>> nonrec_fact(5)
    120
    >>> nonrec_fact(1)
    1
    >>> nonrec_fact(0)
    1
    """
    res = 1
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    while len(stack):
        res *= stack.pop()

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
