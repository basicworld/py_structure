# -*- coding: utf-8 -*-
"""
使用prim构建最小生成树
适用于无向带权网络
"""
from prio_queue import PrioQueue
from graph_linjiebiao import Graph

def prim(graph):
    """"""
    vnum = graph.vertex_num()
    mst = [None] * vnum  # 初始最小生成树为空
    # 通过优先队列来排序候选边(val, vi, vj)
    # 初始的优先队列放入一个初始点，这个点与自身连接，边设置为0从而不影响总权重
    # 第二位数字也可以是其他值，但是0最保险
    cands = PrioQueue([(0, 0, 0)])
    count = 0  # 记录已经生成树的边
    while count < vnum and not cands.is_empty():
        val, vi, vj = cands.dequeue()  # 取出下一个最小的边
        # 如果另一个点已经在生成树里，则跳过
        if mst[vj]:
            continue
        mst[vj] = ((vi, vj), val)
        count += 1
        # 查找新加入边的邻边信息
        # 如果符合prim的入队条件，则吧边存到候选边集合里
        for v, w in graph.out_edges(vj):
            if not mst[v]:
                cands.enqueue((w, vj, v))
    return mst

def test():
    """无向图生成树测试"""
    list_int = lambda x: map(int, list(x))
    mat = [list_int('0063000'),
           list_int('0040070'),
           list_int('6400500'),
           list_int('3000500'),
           list_int('0055009'),
           list_int('0700001'),
           list_int('0000910')]
    g = Graph(mat)
    print prim(g)

if __name__ == '__main__':
    test()
