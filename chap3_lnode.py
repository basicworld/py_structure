# -*- coding: utf-8 -*-
"""
单链表的实现
"""
import sys


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        """one node"""
        self.elem = elem
        self.next = next_


class LList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        """insert at head of llist"""
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        return e

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            # print(p.elem),
            sys.stdout.write(unicode(p.elem))
            if p.next is not None:
                # print(', '),
                sys.stdout.write(', ')
            p = p.next
        print('')

    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next

if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()
    for i in mlist1.elements():
        print i
