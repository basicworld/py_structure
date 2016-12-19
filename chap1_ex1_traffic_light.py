# -*- coding: utf-8 -*-
"""
红绿灯问题思路：
根据路线冲突图，将非相邻的路线分组
根据四色原理，最多分为4组
算法：贪心算法（解可能不是最优的，但是是可接受的）
此程序不能运行目前


思路：
1.枚举出所有允许的通过方向
2.根据通过方向和冲突路线的定义，画出冲突图
3.把通行方向的分组问题归结为冲突图中互不相邻顶点的划分问题
用求出不相邻顶点的分组作为交叉路口中可以同时同性的方向分组
"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8


def coloring(G):
    """四色问题的贪心算法实现
    G 为冲突图

    """
    color = 0
    groups = set()  # 色块的集合
    # 取出图中的所有顶点
    verts = vertices(G)
    while verts:
        # 新的着色块
        new_group = set()

        # for v in list(verts):  # 目前python的集合已经支持元素遍历，不需要写成这样了
        for v in verts:
            # 检查v 与色块new_group 在图G中是否有冲突
            if not_adjacent_with_set(v, new_group, G):
                new_group.add(v)
                verts.remove(v)
        # 色块存放到色块集合
        groups.add((color, new_group))
        color += 1

    return groups
