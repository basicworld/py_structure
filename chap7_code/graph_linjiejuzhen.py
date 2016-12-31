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
