带权图中，一个顶点到另一个顶点可能存在多条路径，`最短路径`就是研究最优路径的选择问题。这里的带权图是带权有向图或带权无向图。经典的最短路径算法有：Dijkstra，Floyd

# 最短路径问题

路径：图中顶点vi到vj的所有边的权值之和

最短路径应用：

1. 运输规划（最短里程、最小运费、最少时间等）
2. 加工或工作流程

最短路径问题，人们已经开发出了比宽度优先、深度优先更有效的算法：

1. Dijkstra解决一个顶点到其他顶点的最短路径问题
2. Floyd解决任意顶点之间的最短路径问题

# 单源点最短路径算法Dijkstra

Dijkstra和prim有些类似

Dijkstra要求顶点之间的权值大于0

## 思想

将图中的点分为两个集合：已知最短路径的顶点集合U、其他顶点的集合。每一步从其他顶点集合中找出一个顶点加入集合U。

选择下一个顶点的原则是：找根顶点到未加入顶点的路径最短的那个点。注意已知最短路径的长度是会变化的

1. 将顶点v0放入集合U，到自身的距离记为0
2. 对于其他顶点，如果与v0直接连接，则记距离为权值，否则距离记为无穷
3. 从V-U中选出已知路径最短的点vmin加入U
4. vmin的加入可能改变U中某些最短路径，如果路径变短了，那么v0到改点的路径经过vmin，此时需要更新这条最短路径
5. 重复3、4两条直到没有点可以加入

## 算法

复杂度为ElogE


```
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
```

# 任意顶点之间的最短路径算法Floyd

## 思想

floyd可以直接计算出个堆顶点之间的所有最短路径

floyd算法也称插点法，基于邻接矩阵，邻接矩阵表示已知最短路径。开始时两点之间不允许插点，然后允许插一个点时更新邻接矩阵，允许插两个点时再更新······

[算法思想的参考博文](http://developer.51cto.com/art/201403/433874.htm)


## 算法

时间复杂度为n^3，空间复杂度为n^2，算法复杂度低于多次调用dijkstra的复杂度，但是仍然是3次方的复杂度，所以该算法不适合大规模运算

```
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
```