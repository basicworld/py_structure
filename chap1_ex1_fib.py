def fib(n):
    f1 = f2 = n
    for k in xrange(1, n):
        f1, f2 = f2, f2 + f1

    return f2


if __name__ == '__main__':
    print fib(100)
    print fib(10000)
    print fib(100000)
