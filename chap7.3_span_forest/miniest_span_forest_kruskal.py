# -*- coding: utf-8 -*-
"""
使用krushkal构建最小生成树
适用于无向带权网络
"""
from graph_linjiebiao import Graph

def kruskal(graph):
    """"""
    vnum = graph.vertex_num()
    # reps记录各联通分量的代表元，如果两个顶点的代表元相同，
    # 则他们是相互连通的，属于同一连通分量
    # 初始的代表元是各顶点自己，即各顶点和自己是联通的
    reps = range(vnum)

    mst = []  # 记录最小连通图，即最小生成树或树林
    edges = []  # 记录所有的边
    # edges记录所有的边
    for vi in range(vnum):
        for vj, val in graph.out_edges(vi):
            edges.append((val, vi, vj))
    # 边按权重排序
    edges.sort()
    for val, vi, vj in edges:
        # 如果两个点不属于同一个连通分量，则把两者连起来
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), val))  # 放进最小生成树里
            # 提取这两个不同的连通分量，将其设置为一样
            rep, orep = reps[vi], reps[vj]
            # 合并连通分量，统一代表元
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep

            # 如果mst边数为n-1，则构造完成
            if len(mst) == vnum - 1:
                break
    print u'代表元表：', reps
    return mst  # 返回最小生成树

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
    print kruskal(g)

if __name__ == '__main__':
    test()
