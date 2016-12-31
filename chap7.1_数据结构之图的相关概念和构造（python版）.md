图是复杂的二元关系拓扑结构，在计算机结构中是一种复杂的数据结构，可用于表示各种复杂联系的数据集合

数学领域里有专门的分支研究图结构--“图论”，图算法也是计算机算法的重要分支

# 图的概念和性质

## 概念

图是一个二元组，由顶点和边组成`G=(V,E)`

根据边是否有指向性，图分为有向图、无向图

其他基本概念：顶点、重点、无向边、邻接顶点、邻接关系、度、完全图、入度、出度、路径、回环（回路）、子图、连通子图、（强连通子图-强连通分量）、极大连通子图、极大强连通子图、带权图、网络

连通：两个点之间有路径

有根图：存在一个顶点，与其他任一点连通

连通无向图：无向图中，任意两点之间是连通的

强连通有向图：有向图中，任意两点之间是连通的（此时的连通是指正反方向都连通）

最小连通图：连通图中，去掉任一条边都不再是连通图

网络：带权的连通无向图

图的表示：顶点用小圆圈，边用实线，标记写旁边。图的表示中，位置、距离、交叉性都无关紧要

## 性质

1. n个顶点的无向完全图有n*(n-1)/2条边
2. n个顶点的有向完全图有n*(n-1)条边
3. |E|<=|V|^2。该性质用于计算算法复杂度
4. 路径的长度就是边的条数
5. 简单路径是内部不包含回路的路径（简单回路也是简单路径）
6. 包含n个顶点的最小连通无向图有n-1条边
7. 包含n个顶点的最小有根图有n-1条边
7. 最小连通无向图称为无向树
8. 满足7性质的有向图称为有向树

# 图的表示

## 图的抽象数据类型ADT

```python
# -*- coding: utf-8 -*-
"""
图的抽象数据类型

ADT Graph:
    Graph(self)  # 构造一个新图
    is_empty(self)  # 是否为空图
    vertex_num(self)  # 顶点数
    edge_num(self)  # 边数
    vertices(self)  # 所有顶点的集合
    edges(self)  # 所有边的集合
    add_vertex(self, vertex)  # 添加一个顶点
    add_edge(self, v1, v2)  # 添加一条边
    get_edge(self, v1, v2)  # 获得v1到v2的路径信息
    out_edge(self, v)  # 获得从v出发的所有边
    degree(self， v) 检查v的度
"""
```

## 图的邻接矩阵表示

：：

性质：

1. 无向图的邻接矩阵是对称矩阵
2. 行对应出边，列对应入边

缺点：现实中的图一般是稀疏矩阵，所以邻接矩阵浪费时间和空间

改进方法：

1. 邻接表表示法
2. 邻接多重表表示法
3. 图的十字链表法

```python

class GraphError(ValueError):
    pass

class Graph(object):
    def __init__(self, mat, unconn=0):
        """
        使用邻接矩阵构造图结构-有向图的实现

        @mat 表示初始的邻接矩阵
        @unconn 0表示无连接，1或者权值表示有连接
        """
        vnum = len(mat)  # 顶点数
        # 检查是否为方阵
        for x in mat:
            if len(x) != vnum:
                raise ValueError(u'参数mat不是方阵，无法构造邻接矩阵')

        # 拷贝mat
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        """检查顶点v是否合法，不合法返回True"""
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        """
        添加顶点就是添加邻接矩阵的一行+一列
        """
        for x in self._mat:
            x.append(self._unconn)
        self._vnum += 1
        self._mat.append([self._unconn]*self._vnum)

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(u'输入的顶点不合法，请检查')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('输入的顶点不合法，请检查')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(u'输入的顶点不合法，请检查')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i, val in enumerate(row):
            if val != unconn:
                edges.append((i, val))
        return edges

    def __str__(self):
        return ('Graph[\n' + ',\n'.join([str(x) for x in self._mat])\
                + '\n]Unconn: ' + str(self._unconn))

def test():
    mat = [[0,0,1],[1,0,1],[0,1,0]]
    g = Graph(mat)
    print g.get_edge(0,1)
    print g.out_edges(2)
    g.add_edge(2,0,1)
    print g.out_edges(2)

    g.add_vertex()
    print g.out_edges(3)
    g.add_edge(3,1,5)
    print g.out_edges(3)
    print g

if __name__ == '__main__':
    test()
```

## 图的邻接表表示（压缩的邻接矩阵）

：：图中每个顶点关联一个表，记录这个顶点的所有邻接边。无向图中每条边需要在两个顶点的邻接边表里显示

具体的实现可以用链接表或连续表。实际中常用顺序表表示顶点，每个顶点关联一个表示邻接边表的链表。（跟树的邻接表实现方式类似）

```python

class GraphError(ValueError):
    pass

class Graph(object):
    """使用邻接表实现图结构"""
    def __init__(self, mat=[], unconn=0):
        """
        从邻接矩阵构造初始邻接表
        支持从空图出发来构建图对象
        构造的表是有序邻接表
        目前缺陷：没有检查初始邻接矩阵的有序性

        @mat 默认邻接矩阵
        @unconn 非连接的默认值
        """
        super(Graph, self).__init__()
        # self._mat = mat
        vnum = len(mat)  # 顶点个数
        # 检查邻接矩阵是否为方阵
        for x in mat:
            if len(x) != vnum:
                raise GraphError(u'mat参数不是方阵')

        # 同样是按下标构建邻接表对象，输出格式[[(1,0)],[(2,1),(2,2)],[]]
        # 每个子list表示一个顶点,有序
        # 每个子list中的元组表示（vj, val）,即(边的另一个点，权值)，有序
        self._mat = [Graph._out_edges(x, unconn) for x in mat]

        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        """
        vi
        vj
        val
        """
        if self._vnum == 0:
            raise GraphError(u'无法为空图添加边，请先使用add_vertex()添加边')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(u'边值不合法:', (vi, vj))
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return

            # 因为下标是有序的，所以一旦row[i][0]大于vj就说明没有这条边
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def _invalid(self, v):
        """检查顶点v是否合法，不合法返回True"""
        return v < 0 or v >= self._vnum

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(u'边值不合法:', (vi, vj))
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(u'边值不合法:', vi)
        return self._mat[vi]

    @staticmethod
    def _out_edges(row, unconn):
        """提取顶点的有效出连接"""
        return [(i, val) for i, val in enumerate(row) if val != unconn]

    def __str__(self):
        return ('Graph[\n' + ',\n'.join([str(x) for x in self._mat])\
                + '\n]Unconn: ' + str(self._unconn))

def test():
    mat = [[0,0,1],[1,0,1],[0,1,0]]
    g = Graph(mat)
    print g

    vi = g.add_vertex()
    g.add_edge(vi,0,1)
    g.add_edge(2,2,3)
    print g

if __name__ == '__main__':
    test()
```

# NOTE

1. python里定义大于任意值的值的方法:`inf=float('inf')`（实际上inf构造的值约等于`10e307`）
2. python里以可变变量作为参数传进函数时，要保证在调用前做一次拷贝，防止修改原来的变量