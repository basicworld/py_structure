# -*- coding: utf-8 -*-
"""
字符串匹配最简单的实现

t是长字符串
p是短字符串
"""


def naive_matching(t, patten):
    """算法复杂度m*n"""
    m, n = len(patten), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if patten[i] == t[j]:
            i += 1
            j += 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1


if __name__ == '__main__':
    print naive_matching('abcbcdeeg', 'deeg')
