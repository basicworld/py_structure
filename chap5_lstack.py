# -*- coding: utf-8 -*-
"""
栈数据结构的实现

ADT Stack:
    Stack(self)
    is_empty(self)  #
    push(self, elem)  #
    pop(self)  #
    top(self)  # 取得栈里最后压入的元素，不删除
"""


class LNode(object):
    def __init__(self, elem, next_=None):
        """one node"""
        self.elem = elem
        self.next = next_


class StackUnderFlow(ValueError):
    pass


class LStack(object):
    def __init__(self):
        """
        使用链接表实现栈结构
        """
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        """取得栈顶元素"""
        if self.is_empty():
            raise StackUnderFlow('in LStack.top()')

        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow('in LStack.pop()')

        p = self._top
        self._top = p.next
        return p.elem


def test():
    st1 = LStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print st1.pop()


def reverse_list(origin_list):
    st = LStack()
    for i in origin_list:
        st.push(i)
    list1 = []
    while not st.is_empty():
        list1.append(st.pop())

    return list1


def check_parens(text):
    """检查括号匹配情况，text是要检查的文本"""
    parens = '()[]{}'
    open_parens = '([{'
    oppsite = {')': '(', ']': '[', '}': '{'}

    def parentheses(text):
        """括号生成器"""
        i, text_len = 0, len(text)
        while 1:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    st = LStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != oppsite[pr]:
            print 'Unmatching is found at', i, 'for', pr
            return False
        else:
            pass

    print 'All parentheses are correctly matched'
    return True



if __name__ == '__main__':
    test()
    print reverse_list([1,2,3])
    print check_parens('()[]{}fdgdfsg{dfgergre}')
