# -*- coding:utf8 -*-
from grs import Stock

class Checking(object):

    def __init__(self, data):
        self.data = data

    def ck001(self):
        mao = self.data.MAO(3, 6)
        if mao[0] > 0 and mao[1] > 0 and \
                self.data.value[-1] > 1000 and self.data.price[-1] > 10 and \
                (self.data.value[-1] > self.data.value[-2] and self.data.value[-1] > self.data.value[-3]):
            return True

        return False

if __name__ == "__main__":
    checking = Checking(Stock('2618'))
    print checking.data.MA(3)
    print checking.ck001()
    print help(checking)
