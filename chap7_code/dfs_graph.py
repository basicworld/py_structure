# -*- coding: utf-8 -*-
"""
图的深度优先遍历的非递归算法
"""
# 使用邻接表构造的图
from graph_linjiebiao import Graph

def DFS_graph(graph, v0):
    """
    @graph 图对象
    @v0 初始遍历点,以下标表示
    """
    vnum = graph.vertex_num()
    visited = [0] * vnum  # 记录已遍历的点，1为遍历过，0为没有

    visited[v0] = 1
    DFS_seq = [v0]
    stack = []  # 记录需要遍历的点

    # 下次应该访问以v0为顶点的边表中的第 0 条（初始为0）
    stack.append((0, graph.out_edges(v0)))

    while stack or sum(visited) < vnum:
        while stack:
            # 弹出一个顶点并访问
            i, edges = stack.pop()
            if i < len(edges):  # 如果存在第i条边就继续
                v, e = edges[i]  # vj, val，即另一个顶点，边值
                stack.append((i+1, edges))  # 回溯时访问下一个顶点

                # 如果v未访问，访问v并记录可到达的顶点入栈
                if not visited[v]:
                    DFS_seq.append(v)  # 记录访问序列
                    visited[v] = 1  # 记录访问过的点
                    # 记录下一次该访问的一组边
                    stack.append((0, graph.out_edges(v)))

        # 如果有孤立的点没有被遍历，则拿其中一个进行遍历
        if sum(visited) < vnum:
            # print visited
            v0 = visited.index(0)
            visited[v0] = 1
            DFS_seq.append(v0)
            stack.append((0, graph.out_edges(v0)))

    return DFS_seq

def test():
    """有向图深度遍历测试"""
    list_int = lambda x: map(int, list(x))
    mat = [list_int('0063000'),
           list_int('1040000'),
           list_int('0300500'),
           list_int('0000500'),
           list_int('0000000'),
           list_int('0000001'),
           list_int('0000010')]
    g = Graph(mat)
    print DFS_graph(g, 0)

if __name__ == '__main__':
    test()
