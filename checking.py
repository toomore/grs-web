# -*- coding:utf8 -*-
from grs import Stock

class Checking(object):

    def __init__(self, data):
        self.data = data

    def ck001(self):
        ''' 3-6負乖離且向上，三日內最大量，成交量大於 1000 張，
            收盤價大於 10 元。（較嚴謹的選股）'''
        mao = self.data.MAO(3, 6)
        if mao[0] > 0 and mao[1] > 0 and \
                self.data.value[-1] > 1000 and self.data.price[-1] > 10 and \
                max(self.data.value[-3:]) == self.data.value[-1]:
            return True

        return False

    def ck002(self):
        if self.data.MA(3)[0][-1] > self.data.MA(6)[0][-1] > \
                self.data.MA(18)[0][-1] and self.data.MA(18)[1] > 0:
            return True

        return False

if __name__ == "__main__":
    checking = Checking(Stock('2618'))
    print checking.ck001()
    print checking.ck002()
