class C1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        print self.x, self.y


# class C2(C1):
#     def m1(self):
#         super(self).m1()
#         print 'some special service'


# if __name__ == '__main__':
#     c = C2(1, 2)
#     c.m1()
