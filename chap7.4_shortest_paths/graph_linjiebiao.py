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

    def vertex_num(self):
        return self._vnum

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
        """
        获得vi为顶点的所有出边
        返回值为(vj, val),即(另一个顶点，边的权值)
        """
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
    print g.out_edges(2)

if __name__ == '__main__':
    test()
