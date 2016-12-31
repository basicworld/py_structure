# -*- coding: utf-8 -*-
"""
构造图的生成树--深度优先遍历的递归算法
注意这里还不是最小生成树，只是生成树
"""
from graph_linjiebiao import Graph


def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    # 生成树每个点只有一个前一顶点，所以
    # span_forest存储顶点的前一顶点和边的信息
    span_forest = [None] * vnum

    def dfs(graph, v, span_forest):
        """递归遍历"""
        for vj, val in graph.out_edges(v):
            # 如果没遍历过，则存储前一顶点和边
            if span_forest[vj] is None:
                span_forest[vj] = (v, val)
                dfs(graph, vj, span_forest)

    # 找一个根，然后开始dfs遍历
    for i, v in enumerate(span_forest):
        if v is None:
            span_forest[i] = (i, 0)
            dfs(graph, i, span_forest)
    return span_forest

def test():
    """有向图生成树测试"""
    list_int = lambda x: map(int, list(x))
    mat = [list_int('0063000'),
           list_int('1040070'),
           list_int('0300500'),
           list_int('0000500'),
           list_int('0000009'),
           list_int('0000001'),
           list_int('0000000')]
    g = Graph(mat)
    print DFS_span_forest(g)

if __name__ == '__main__':
    test()
