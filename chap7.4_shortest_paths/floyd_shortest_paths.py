# -*- coding: utf-8 -*-
"""
多元最短路径的floyd算法
"""
from graph_linjiebiao import Graph

def floyd_shortest_paths(graph):
    """"""
    vnum = graph.vertex_num()
    # 初始的邻接矩阵
    a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
    vertex = [[-f if a[i][j] == inf else j
                for j in range(vnum)] for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    vertex[i][j] = vertex[i][k]
    return (a, nvertex)
