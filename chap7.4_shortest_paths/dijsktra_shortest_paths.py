# -*- coding: utf-8 -*-
"""
最短路径的dijkstra算法
"""
from graph_linjiebiao import Graph
from prio_queue import PrioQueue

def dijkstra_shortest_paths(graph, v0):
    """"""
    pass
    vnum = graph.vertex_num()
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        val, u, vmin = cands.dequeue()
        print val, u, vmin
        if paths[vmin]:  # 如果最短路径已知则继续
            continue
        paths[vmin] = (u, val)
        for vj, w in graph.out_edges(vmin):
            if not paths[vj]:
                # 这里和prim不同，这里每次入队的是路径长度，而不是单个边
                cands.enqueue((val + w, vmin, vj))
        count += 1
    # 输出的每一项是(路径的上一个结点，最短路径)
    return paths

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
    print dijkstra_shortest_paths(g, 0)

if __name__ == '__main__':
    test()
