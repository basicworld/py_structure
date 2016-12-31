介绍从连通图（有向图的强连通有向图）构造生成树的算法

关键词：连通图、生成树（树林）、最小生成树、Kruskal、Prim

# 生成树的相关概念

1. 如果图G有n个顶点，必然可以找到一个包含n-1条边的集合，这个集合包含了从v0到其他所有顶点的路径
2. n个顶点的连通图G的生成树敲好包含了n-1条边。无向图的生成树是G的最小连通子图（无环）。有向图的生成树中所有的边都位于从根到其他顶点的路径上
3. 每个无向图都存在生成树林
4. 包含n个顶点、m个连通分量的无向图G的生成树包含n-m条边
5. 有向图的生成树中，所有的点只有一个入度，可能有多个出度。生成树的所有边都在根到其他顶点的路径上

# DFS生成树林的递归算法

递归算法很简单：从一个顶点出发，如果该顶点的孩子没有被遍历过，则在生成树里记录：（孩子节点的父结点，边），然后以孩子结点为顶点继续循环，直到初始顶点连接的点都遍历完

对于邻接表实现的树存储结构，该算法的复杂度为常数级

```
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

```

# 最小生成树

对于带权图而言，存在最小生成树问题：生成树中，权值之和最小的生成树

这里讲解带权连通无向图的最小生成树以及两个算法实现：kruskal和prim

最小生成树应用示例：通讯网络建立的成本问题、配送中心与线路规划问题、管道路线建设、集成电路设计等

## kruskal算法

对于顶点数为n的图G(V,E)，算法思想是：

1. 取所有顶点但是不包含任何边的图T(V,{})（n连接分量图），T里每一项自成一个联通分量，下面通过不断扩充T的方式构造G的最小生成树
2. 将边集E中的边按权值递增的顺序排序，在构造中的每一步顺序检查边的序列，找到哦下一条最短的两个端点位于T的两个不同连通分量的边e，把e加入T，从而T的维度减一
3. 每次操作减少T中的一个连通分量，不断重复直至T中只剩下一个连通分量

如果这样不能得到包含所有顶点的连通分量，则原图不连通，没有最小生成树，算法得到的是最小连通树林

算法主要需要考虑：

1. 如何取出所有边并排序输出，解决：使用一个列表保存所有的边，权重为首项
1.  如何检查一个边是否在T中属于不同连通分量，解决：使用代表元来表示每个顶点，如果代表元相同，则两个顶点属于一个连通分量。加入一条边就是让两个顶点的连通分量相同

算法的复杂度为：max{ElogE，V*V}

> 从本质上说，kruskal算法是一种抽象想法，可称为一个抽样算法（算法模式）。实现算法时，可以采用不同的具体副主数据结构和实现方法。不同的实现方式有不同的复杂度

```
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
```

## prim算法

基本思想是：从一个顶点出发，逐步扩充包含该顶点的部分生成树T。开始时，T只包含初始顶点而且没有边。扩充的思想是，从该顶点（顶点集合）相连的边中找权值最小的边加入顶点集合，直到所有顶点加入顶点集合

prim基于最小生成树的一个重要性质：G(V,E)为一个网络，U为网络的真子集，边e的一个顶点在U里，另一个不在U里，而且e是所有满足这种条件的边里权值最小的，那么G必有一棵包含边e的最小生成树

算法时间复杂度为ElogE

> prim也是一种抽象算法，有许多实现方法
> 

```
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
```

上面算法的缺点是可能把没有价值的边也存进优先队列，造成了空间浪费。实际上最小生成树的有用边不超过顶点数，而这里可能把所有边都存到优先队列里，增加了复杂度。

# 最小生成树的研究

最小生成树是非常有用的算法，近年来有各种新的算法提出，如随机算法、已知最优算法、一些并行算法等。研究证明该问题的时间复杂度下界为O(E)，但是还没找到这样的算法。留待你去发现