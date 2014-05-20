# -*- coding:utf8 -*-
from grs import Stock
from numpy import std

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
        ''' 3日均價大於6日均價，6日均價大於18日均價。
           （短中長線呈現多頭的態勢）'''
        ma_18 = self.data.MA(18)

        if self.data.MA(3)[0][-1] > self.data.MA(6)[0][-1] > ma_18[0][-1] and \
                ma_18[1] > 0:
            return True

        return False

    def ck004(self):
        ''' 價走平一個半月。（箱型整理、盤整）'''
        if std(self.data.price[-45:]) < 0.25:
            return True

        return False

if __name__ == "__main__":
    checking = Checking(Stock('1229'))
    print checking.ck001()
    print checking.ck002()
    print checking.ck004()
