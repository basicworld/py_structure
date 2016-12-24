# -*- coding: utf-8 -*-
"""
海关检查站模拟系统
"""
from simulation import Simulation
from simulation import Event
from squeue import SQueue
from random import randint


class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'car arrive')
        # 生成下一个事件
        Arrive(time + randint(*customs.arrive_interval), customs)

        car = Car(time)
        # 如果有车在等待，就加入队列
        if customs.has_queued_car():
            customs.enqueue(car)
            return

        i = customs.find_gate()
        if i is not None:
            event_log(time, 'car check')
            Leave(time + randint(*customs.check_interval), i, car, customs)
        else:
            customs.enqueue(car)


class Leave(Event):
    def __init__(self, leave_time, gate_num, car, customs):
        Event.__init__(self, leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'car leave')
        customs.free_gate(self.gate_num)
        customs.car_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
            event_log(time, 'car check')
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval), self.gate_num, car, customs)


class Customs(object):
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        """
        @gate_num
        @duration
        @arrive_interval 到达时间间隔
        @check_interval 检查时间间隔
        """
        self.simulation = Simulation(duration)  # 驱动模拟的Simulation 对象
        self.waitline = SQueue()  # 排队
        self.duration = duration
        self.gates = [0] * gate_num  # 0 表示该检查点空闲， 1 表示忙碌
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self, n):
        """累计等待时间"""
        self.total_wait_time += n

    def total_time_acc(self, n):
        """累计使用时间"""
        self.total_used_time += n

    def car_count_1(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def has_queued_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 1
        else:
            raise ValueError('Clear gate error')

    def simulate(self):
        """
        实施模拟
        """
        Arrive(0, self)  # 事件
        self.simulation.run()
        self.statistics()

    def statistics(self):
        """"""
        print('Simulate' + str(self.duration) + ' minutes, for '
              + str(len(self.gates)) + ' gates')
        print(self.car_num, 'car pass the customs')
        print('Average waiting time:', self.total_wait_time / self.car_num)
        print('Average passing time:', self.total_used_time / self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, 'cars are in the waiting line')


class Car(object):
    """
    汽车类，记录到达时
    """
    def __init__(self, arrive_time):
        self.time = arrive_time

    def arrive_time(self):
        return self. time


def event_log(time, name):
    """开发测试用"""
    print('Event ' + name + ', happened at ' + str(time))

def main():
    car_arrive_interval = (1, 2)
    car_check_time = (3, 5)
    cus = Customs(3, 480, car_arrive_interval, car_check_time)
    cus.simulate()

if __name__ == '__main__':
    main()
