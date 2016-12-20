# -*- coding: utf-8 -*-
"""
有理数类的构造
使用ADT描述有理数

ADT Rational:
    Rational(self, int num, int den)
    +(self, Rational r2)  # 加法
    -()  # 减法
    *()
    /()
    num(self)  # 取得该有理数的分子
    den(self)  # 取得该有理数的分母
"""


class Rational1:
    @staticmethod
    def _gcd(m, n):
        """
        最大公约数计算的静态方法,辗转相除
        是一个有理数化简需要的功能，因此定义为内部函数

        GCD=Greatest Common Divisor

        欧几里德定理
        若 a=b×r+q 则gcd(a, b) = gcd(b, q).
        """
        if n == 0:
            m, n = n, m

        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1  # 正负号

        # 提取正负号
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign

        # 求最大公约数

        g = self._gcd(num, den)
        # 分子
        self._num = sign * (num // g)
        # 分母
        self._den = sign * (den // g)

    def num(self):
        return self._num

    def den(self):
        return self._den

    def show(self):
        print str(self._num) + '/' + str(self._den)

    def __add__(self, another):
        """加法"""
        den = self._den * another.den()
        num = (self._num * another.den() + self._den * another.num())
        return Rational1(num, den)

    def __mul__(self, another):
        """
        乘法
        """
        return Rational1(self._num * another.num(), self._den * another.den())

    def __eq__(self, another):
        return self._den * another.num() == self._num * another.den()

    def __repr__(self):
        return str(self._num) + '/' + str(self._den)

    def __str__(self):
        return str(self._num) + '/' + str(self._den)


if __name__ == '__main__':
    a = Rational1(-5, -10)
    b = Rational1(5, 15)
    print a * b
    print a == b
    print a + b
