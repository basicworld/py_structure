# -*- coding: utf-8 -*-
"""
表达式的计算机表示和计算
"""


from chap5_sstack import SStack


class ESStack(SStack):
    def depth(self):
        return len(self._elems)


def suf_exp_evaluator(exp):
    """后缀表达式的计算
    exp 后缀表达式的list表示

    >>> suf_exp_evaluator(['3', '2', '-'])
    1.0
    >>> suf_exp_evaluator('3 5 - 6 17 4 * + * 3 /'.split())
    -49.333333333333336
    """
    operators = '+-*/'
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2:
            raise SyntaxError('Short of operand(s)')

        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError('Extra operand(s)')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
