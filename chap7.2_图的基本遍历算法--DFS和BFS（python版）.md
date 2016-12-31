现实中存在很多问题都可以抽象为图和图的计算问题：路由选择、集成电路的设计和布线、物流问题、工程项目计划安排、关联交易检查（金融监管问题）

一旦将问题抽象为图，解决问题就变成图上的一个算法问题

图的算法将涉及栈、队列、优先队列的使用

# 基本图算法

图的遍历方法同样有深度优先（DFS，depth-first-search）和宽度优先（BFS，breadth-first-search）两种。注意遍历的结果可能不止一种

## 深度优先DFS

深度优先遍历得到的顶点序列为`深度优先搜索序列`（DFS序列）

1. 访问顶点v，并记录为已访问
2. 检查v的邻接点，选择尚未访问的点，不存在尚未访问的点时进行回溯
3. 重复进行上一步，直到v可到达的所有顶点已访问
4. 如果存在未访问的点，从中选出一个，重新进行第1步

## 宽度优先BFS


宽度优先遍历得到的顶点序列为`宽度优先搜索序列`（BFS序列）

1. 访问顶点v，并记录为已访问
2. 访问v的邻接点，并记录为已访问
3. 将v的邻接点记为v，返回第一步，重复步骤直到v可到达的所有顶点已访问
5. 如果存在未访问的点，从中选出一个，重新进行第1步

## DFS的实现

复杂度为max（V，E）

```
[python]
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


[/python]
```