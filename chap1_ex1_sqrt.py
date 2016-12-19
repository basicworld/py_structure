# -*- coding: utf-8 -*-
"""
"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
THIS_DIR = os.path.realpath(os.path.dirname(__file__))


def sqrt(x):
    """
    牛顿迭代算法求平方根
    """
    y = 1.0
    while abs(y*y - x) > 1e-6:
        y = (y + x / y) / 2
    return y

if __name__ == '__main__':
    print sqrt(100)
    print sqrt(10)
    print sqrt(80)
