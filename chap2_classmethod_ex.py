# -*- coding: utf-8 -*-
class Countable:
    counter = 0

    def __init__(self):
        Countable.counter += 1

    @classmethod
    def get_counter(cls):
        """用于实现与所有实力函数相关的方法"""
        return Countable.counter

    def __del__(self):
        Countable.counter -= 1


if __name__ == '__main__':
    a = Countable()
    b = Countable()
    c = Countable()
    del a
    print Countable.get_counter()
