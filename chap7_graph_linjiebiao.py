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
    def __init__(self, arg):
        super(Graph, self).__init__()
        self.arg = arg


def test():
    pass

if __name__ == '__main__':
    test()
