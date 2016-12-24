# -*- coding: utf-8 -*-
"""
模拟器
采用面向对象的离散时间模拟框架
"""
from random import randint
from prio_queue import PrioQueue


class Simulation(object):
    """模拟器基类"""
    def __init__(self, duration):
        """"""
        self._eventq = PrioQueue()  # 事件队列
        self._time = 0  # 当前时间
        self._duration = duration  # 模拟总时长

    def run(self):
        while not self._eventq.is_empty():  # 模拟到事件队列为空
            event = self._eventq.dequeue()  #
            self._time = event.time()  # 事件的时间就是当前时间
            if self._time > self._duration:  # 时间用完就结束
                break
            event.run()  # 开始运行，可能生成新的事件

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Event(object):
    """
    事件基类
    """
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host  # 宿主系统

    def __lt__(self, other_event):
        return self._ctime < other_event.time()

    def __le__(self, other_event):
        return self._ctime <= other_event.time()

    def time(self):
        return self._ctime

    def host(self):
        return self._host

    def run(self):
        """
        对于不同的事件，只需要定义run()函数就可以
        """
        pass
