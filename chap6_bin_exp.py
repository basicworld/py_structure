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
